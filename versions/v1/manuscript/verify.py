import argparse
from fractions import Fraction
import json
from math import comb, isqrt, prod
from pathlib import Path


def factorization(value):
    remaining = value
    prime = 2
    factors = {}
    while prime * prime <= remaining:
        while remaining % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            remaining //= prime
        prime += 1
    if remaining > 1:
        factors[remaining] = 1
    return factors


def chebyshev_rows(maximum):
    previous = [1]
    yield previous
    if maximum == 0:
        return
    current = [0, 1]
    yield current
    for polynomial_index in range(1, maximum):
        following = [0] * (len(current) + 1)
        for degree, coefficient in enumerate(current):
            following[degree + 1] += 2 * coefficient
        for degree, coefficient in enumerate(previous):
            following[degree] -= coefficient
        yield following
        previous, current = current, following


def binomial_row(polynomial_index):
    if polynomial_index == 0:
        return [1]
    coefficients = [0] * (polynomial_index + 1)
    for summation_index in range(polynomial_index // 2 + 1):
        degree = polynomial_index - 2 * summation_index
        coefficient = Fraction(
            (-1) ** summation_index
            * polynomial_index
            * comb(polynomial_index - summation_index, summation_index)
            * 2 ** degree,
            2 * (polynomial_index - summation_index),
        )
        assert coefficient.denominator == 1
        coefficients[degree] = coefficient.numerator
    return coefficients


def integral_formula(polynomial_index):
    if polynomial_index == 0:
        return Fraction(1)
    if polynomial_index % 2 == 0:
        return Fraction(-1, polynomial_index ** 2 - 1)
    if polynomial_index % 4 == 1:
        return Fraction(1, polynomial_index + 1)
    return Fraction(-1, polynomial_index - 1)


def floor_difference(integer, modulus):
    return integer // modulus - (integer - 1) // modulus


def check(maximum, general_maximum, exponent_maximum):
    fixtures = json.loads(Path(__file__).with_name('source-fixtures.json').read_text())
    integrals = []
    integrated_rows = []
    coefficient_pairs = 0
    for polynomial_index, coefficients in enumerate(chebyshev_rows(maximum + 1)):
        assert coefficients == binomial_row(polynomial_index)
        integrated = [Fraction(coefficient, degree + 1)
                      for degree, coefficient in enumerate(coefficients)]
        integral = sum(integrated, Fraction(0))
        assert integral == integral_formula(polynomial_index)
        if polynomial_index % 2:
            assert integral == Fraction(
                (-1) ** ((polynomial_index - 1) // 2),
                2 * (2 * ((polynomial_index - 1) // 4) + 1),
            )
        for integrated_degree, coefficient in enumerate(integrated, start=1):
            corrected = coefficient * Fraction(integrated_degree, 2 ** (integrated_degree - 1))
            assert corrected == Fraction(coefficients[integrated_degree - 1],
                                         2 ** (integrated_degree - 1))
            coefficient_pairs += 1
        integrals.append(integral)
        integrated_rows.append(integrated)

    assert [str(integral) for integral in integrals[:11]] == fixtures['A164660']['rational_examples']
    assert [integral.numerator for integral in integrals[:11]] == fixtures['A164660']['numerators']
    assert [integral.denominator for integral in integrals[:11]] == fixtures['A164661']['values']
    assert [[str(coefficient) for coefficient in row] for row in integrated_rows[:5]] == fixtures['A164658_A164659']['rational_rows']
    assert [sum(coefficient.numerator for coefficient in row) for row in integrated_rows[:11]] == fixtures['A164662']['values']
    assert [sum(coefficient.denominator for coefficient in row) for row in integrated_rows[:11]] == fixtures['A164663']['values']
    assert integrated_rows[0][0] * 2 != Fraction(1)
    assert integrated_rows[7][5] == Fraction(-56, 3)
    assert integrated_rows[7][5] != Fraction(56, 3)
    for source in fixtures['root_counts']['sources']:
        exponent = source['exponent']
        counts = []
        for modulus in range(1, len(source['values']) + 1):
            counts.append(sum(integer ** exponent % modulus == 0 for integer in range(modulus)))
        assert counts == source['values']

    target_pairs = 0
    for modulus in range(1, maximum + 1):
        factors = factorization(modulus)
        radical = prod(factors)
        count = 0
        floor_product = 1
        for integer in range(1, modulus + 1):
            power = integer ** modulus
            indicator = floor_difference(power, modulus)
            assert indicator == int(power % modulus == 0)
            assert bool(indicator) == (integer % radical == 0)
            count += indicator
            floor_product *= 1 - 2 * indicator
            target_pairs += 1
        assert count == modulus // radical
        assert floor_product == (-1) ** count == integrals[modulus + 1].numerator
        assert floor_product == (1 if modulus % 4 == 0 else -1)

    shifts = [-257, -13, -1, 0, 7, 257]
    general_pairs = 0
    interval_count = 0
    square_indicator_moduli = 0
    for modulus in range(1, general_maximum + 1):
        factors = factorization(modulus)
        radical = prod(factors)
        for exponent in range(1, exponent_maximum + 1):
            divisor = prod(prime ** ((multiplicity + exponent - 1) // exponent)
                           for prime, multiplicity in factors.items())
            expected_count = modulus // divisor
            if factors:
                assert (expected_count == modulus // radical) == (exponent >= max(factors.values()))
            else:
                assert expected_count == 1
            if modulus < 2 ** (exponent + 1):
                assert expected_count == modulus // radical
            if exponent == 2:
                square_count = sum(isqrt(modulus * integer) ** 2 == modulus * integer
                                   for integer in range(1, modulus + 1))
                assert square_count == expected_count
                square_indicator_moduli += 1
            for shift in shifts:
                count = 0
                floor_product = 1
                for integer in range(shift + 1, shift + modulus + 1):
                    power = integer ** exponent
                    indicator = floor_difference(power, modulus)
                    assert indicator == int(power % modulus == 0)
                    assert bool(indicator) == (integer % divisor == 0)
                    count += indicator
                    floor_product *= 1 - 2 * indicator
                    general_pairs += 1
                assert count == expected_count
                assert floor_product == (-1) ** expected_count
                if exponent >= 2:
                    assert floor_product == integral_formula(modulus + 1).numerator
                else:
                    assert floor_product == -1
                interval_count += 1

    return {
        'status': 'all finite checks passed',
        'arithmetic': 'Python integers and fractions.Fraction; no floating-point arithmetic',
        'chebyshev_polynomial_indices': [0, maximum + 1],
        'coefficient_methods': ['three-term recurrence', 'explicit binomial expansion'],
        'integral_formula_indices': [0, maximum + 1],
        'target_indices': [1, maximum],
        'target_floor_divisibility_pairs': target_pairs,
        'general_moduli': [1, general_maximum],
        'general_exponents': [1, exponent_maximum],
        'interval_shifts': shifts,
        'general_intervals': interval_count,
        'general_floor_divisibility_pairs': general_pairs,
        'column_normalization_pairs': coefficient_pairs,
        'source_example_indices': [0, 10],
        'rational_triangle_example_rows': [0, 4],
        'root_count_source_example_moduli': [1, 16],
        'square_indicator_moduli_checked': square_indicator_moduli,
        'source_corrections': {
            'A164658_column_multiplier': 'j/2^(j-1), rather than j/2^(j-2)',
            'A164660_linked_table_integrated_coefficient_b_7_6': '-56/3, rather than 56/3',
        },
        'proof_scope': {
            'written_proofs': 'All-index integral, root-count, translated-product, sharp exponent threshold, and coefficient identities are proved in note.tex.',
            'lean_declaration': 'D5.S3.ArithSums.BrowneA164660ChebyshevFloorProduct.result proves the original two equalities for all positive n at the source revision cited in note.tex.',
            'finite_checks': 'The ranges and counts above concern this program; finite checks do not establish the all-index statements.',
        },
    }


def main():
    parser = argparse.ArgumentParser(description='Exact finite checks for Chebyshev integrals and floor products.')
    parser.add_argument('--maximum', type=int, default=300)
    parser.add_argument('--general-maximum', type=int, default=128)
    parser.add_argument('--exponent-maximum', type=int, default=12)
    arguments = parser.parse_args()
    if arguments.maximum < 10 or arguments.general_maximum < 1 or arguments.exponent_maximum < 2:
        parser.error('Use maximum >= 10, general-maximum >= 1 and exponent-maximum >= 2.')
    print(json.dumps(check(arguments.maximum, arguments.general_maximum, arguments.exponent_maximum), indent=2))


if __name__ == '__main__':
    main()
