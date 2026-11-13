# OEIS A164660: Chebyshev numerators and floor products

**Authors:** Haobo Ma (ChronoAI Pte Ltd, Singapore), followed by Wenlin Zhang
(National University of Singapore; ChronoAI Pte Ltd, Singapore).

**License:** Creative Commons Attribution 4.0 International, CC BY 4.0
(`cc-by-4.0`).

## Contents

- `note.tex` is the complete mathematical source, with an embedded bibliography.
- `metadata.json` gives the note identity, creators, license, and formal source URL.
- `verify.py` performs independent exact finite checks using the Python standard library.
- `source-fixtures.json` contains short attributed numerical examples from the cited OEIS records.
- `MANIFEST.sha256` identifies the files in the source archive.

## Build the PDF

Use Tectonic **0.17.0**:

```sh
tectonic --untrusted note.tex
```

Alternatively, with a standard LaTeX distribution:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is part of `note.tex`; no external bibliography database or
figures are required. Both commands produce `note.pdf`.

## Reproduce the finite checks

Use Python 3.8 or later, without third-party packages:

```sh
python3 verify.py > verification.json
sha256sum verification.json
```

The default output has SHA-256
`9265aa0b76ff9f11badf90d7f6fce343ed259b98953e5b00a4a1798436f1df7d`.
It reports:

- Chebyshev polynomials and rational integrals for indices 0 through 301,
  with recurrence coefficients compared against an explicit binomial expansion.
- Both original floor-product equalities for 1 through 300, including 45,150
  individual floor/divisibility pairs.
- General exponents 1 through 12 and moduli 1 through 128, on intervals shifted
  by -257, -13, -1, 0, 7, and 257: 9,216 intervals and 594,432 individual pairs.
- The corrected coefficient-column identity on 45,753 coefficients; the two
  specified source discrepancies; the published numerical examples; and
  Fried's square-indicator identity for 1 through 128.

## Mathematical and formal scope

Theorem 1 is Browne's final FORMULA in OEIS A164660 (29 May 2016), with both
equalities and the case n = 1. Proposition 2 proves the integral formula,
its numerator, and its denominator sequence A164661. Proposition 3 gives
the exact root count for every positive exponent and the sign identity
for every exponent at least two on any translated interval of n consecutive
integers. Section 4 supplies the coefficient corrections and source coverage.

At source revision `122c987d276498783de7d873378a28b27ced8761`, the declaration
`D5.S3.ArithSums.BrowneA164660ChebyshevFloorProduct.result` proves the original
two equalities for every positive natural n:

https://github.com/the-omega-institute/trureturing/blob/122c987d276498783de7d873378a28b27ced8761/D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.lean

Its `rowSum` is the literal rational coefficient sum in the note, its `a` is
the reduced signed numerator, and its `floorProduct` uses rational floors.
The consumed `row_sum_evaluation` lemma gives the integral branches at
polynomial indices at least two. The arbitrary-exponent formulas,
translated-interval formulas, initial integrals, and coefficient corrections
have the written proofs in the note. The finite checks above concern only
their stated ranges and do not replace the all-index proofs.

The nilpotent count, Browne's earlier floor-sum formula, the classical
root-count sequences A000188--A000190, and Fried's earlier proof of the
A000188 square-indicator identity are credited in the note.
