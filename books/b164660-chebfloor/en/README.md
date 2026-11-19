# Why should an integral's numerator obey divisibility?

Choose a positive integer $n$. On one side, integrate a recursively generated polynomial from $0$ to $1$, reduce the answer to a fraction with positive denominator, and keep its signed numerator. On the other, inspect $1,2,\ldots,n$ and flip a sign whenever $k^n$ is divisible by $n$. Anthony Browne conjectured in 2016 that the answers always agree. They have a particularly simple value: **$+1$ when $4$ divides $n$, and $-1$ otherwise.** A question that appears to concern areas under curves turns into a question about how many factors of $2$ an integer contains.

Haobo Ma and Wenlin Zhang give a complete written derivation and study what happens when the exponent changes or the integer interval moves. The [precise statements and proofs](statements.md) retain all the conditions. We begin with examples you can calculate by hand.

## Two small meetings

Start with $T_0(x)=1$ and $T_1(x)=x$. At each step multiply the preceding polynomial by $2x$ and subtract the one before it:

$$
T_{m+1}(x)=2xT_m(x)-T_{m-1}(x)\quad(m\ge1).
$$

Thus $T_2=2x^2-1$ and $T_3=4x^3-3x$. These are the Chebyshev polynomials of the first kind. We can use them before learning the reason for the name. Integrating each term gives

$$
I_3=\int_0^1(4x^3-3x)\,dx=1-\frac32=-\frac12.
$$

Here $n=2$, since the degree is $n+1=3$. The reduced numerator is $-1$. Of $k=1,2$, only $2^2$ is divisible by $2$, so there is one sign flip: the product is also $-1$.

For $n=4$, the recurrence gives $T_5=16x^5-20x^3+5x$, hence

$$
I_5=\frac{16}{6}-\frac{20}{4}+\frac52=\frac16.
$$

The numerator is $+1$. Among $1,2,3,4$, precisely $2^4$ and $4^4$ are divisible by $4$. Two flips return the sign to $+1$. Examples suggest the question; the mechanism below answers it for every $n$.

## How two floors become a switch

The floor $\lfloor y\rfloor$ is the greatest integer at most $y$: for example $\lfloor7/3\rfloor=2$, whereas $\lfloor-1/3\rfloor=-1$. For an integer $t$ and positive integer $n$, compare $t/n$ with $(t-1)/n$. They differ by $1/n$; their floors differ precisely when this short step crosses an integer:

$$
\delta_n(t)=\left\lfloor\frac tn\right\rfloor-
\left\lfloor\frac{t-1}{n}\right\rfloor
=\begin{cases}1,&n\mid t,\\0,&n\nmid t.\end{cases}
$$

For $n=4$, $t=8$ gives $2-1=1$, while $t=9$ gives $2-2=0$. Subtracting $1$ must happen before the second division. At $t=0$, the two floors are $0$ and $-1$, so the switch still works.

Place this switch inside $1-2\delta_n(t)$. A successful detection contributes $-1$; a failure contributes $+1$. A long product therefore needs no multiplication of enormous powers. Count the successes: if there are $C$, the answer is $(-1)^C$.

## Count without evaluating huge powers

Factor $n$ into prime powers. For example, $12=2^2\cdot3$. The product of its distinct prime factors is its radical: $\operatorname{rad}(12)=2\cdot3=6$, with $\operatorname{rad}(1)=1$ by convention.

For the original exponent $n$, the condition $n\mid k^n$ means precisely that every prime factor of $n$ occurs in $k$, or $\operatorname{rad}(n)\mid k$. Why is one copy enough? If $p^e$ occurs in $n$, then $e\le n$. One copy of $p$ in $k$ supplies at least $n$ copies in $k^n$; no copy supplies none.

The successful integers from $1$ to $n$ are thus exactly the multiples of the radical. There are $n/\operatorname{rad}(n)$, turning the floor product into

$$
(-1)^{n/\operatorname{rad}(n)}.
$$

At $n=12$, the successes are $6,12$, giving $+1$. At $n=6$, only $6$ succeeds, giving $-1$. Dividing by the radical removes one copy of each prime. Odd primes cannot affect parity. If $n$ has exactly one factor of $2$, it disappears; if it has at least two, a factor of $2$ remains. The success count is therefore even exactly when $4\mid n$.

## Why the polynomial side also has a four-step pattern

An integral measures signed area: contributions above the horizontal axis are positive and those below it negative. For these polynomials, a direct exact calculation replaces each term $c x^j$ by $c/(j+1)$ and adds the results.

The polynomials also satisfy a structural identity:

$$
T_m(\cos\theta)=\cos(m\theta).
$$

The cosine addition formula gives the same recurrence, proving the identity. Substituting $x=\cos\theta$ into the integral produces $\cos(m\theta)\sin\theta$. A product-to-sum formula splits this into two sine terms. Integration then requires only endpoint cosine values. As the integer $j$ increases, $\cos(j\pi/2)$ cycles through $1,0,-1,0$: this is the source of the four-step pattern.

The [full integral calculation](statements.md#integral-proof) gives $I_m=-1/(m^2-1)$ for even $m\ge2$, $I_m=1/(m+1)$ for $m\equiv1\pmod4$, and $I_m=-1/(m-1)$ for $m\equiv3\pmod4$. The initial values are $I_0=1$ and $I_1=1/2$.

Every denominator is positive and every numerator is $\pm1$, so these fractions are already reduced. At degree $n+1$, the numerator is positive precisely when $4\mid n$. The two constructions now meet through the same condition. Evaluating the full integral also gives the entire denominator sequence, beyond the sign alone.

## The count can change while the sign stays fixed

Replace $k^n$ by $k^r$. If $n$ contains $p^e$, then $k$ needs at least $\lceil e/r\rceil$ copies of $p$. Rounding upward ensures that multiplication by $r$ reaches $e$. Multiply these required prime powers to obtain $D_r(n)$. The successful integers are its multiples, so their count is $C_r(n)=n/D_r(n)$.

Take $n=16=2^4$. With $r=2$, $k$ needs two factors of $2$: the successes are $4,8,12,16$. With $r=4$, any even $k$ works, giving eight successes. **Four and eight are different counts, but both are even**, so both products are $+1$. Invariance of the product must not be mistaken for invariance of the count.

For every $r\ge2$, parity still depends only on whether $4\mid n$. To make the count itself equal $n/\operatorname{rad}(n)$ requires the stronger condition that $r$ reach the largest prime exponent in $n$. For $16$, that threshold is $4$.

We can also replace $1,\ldots,n$ by any block of $n$ consecutive integers, including negative integers and zero. Since $D_r(n)$ divides $n$, each such block contains the same number of its multiples. For $n=16,r=2$, the successes in $-7,\ldots,8$ are $-4,0,4,8$: still four.

When $r=1$, exactly one integer in the block succeeds, so the product is always $-1$. The case $n=4$ shows why the uniform exponent condition cannot be weakened to $r\ge1$. At $n=1$, the single factor also gives $-1$, agreeing with the numerator of $I_2=-1/3$.

This film draws the same route from a divisibility switch to a count and then its parity.

::: {.film src="001-divisibility-sign"}
How two floors detect divisibility, and why changing the count need not change the product; English narration with aligned Chinese and English subtitles.
:::

The seminar presentation follows these examples into the precise formulas and arguments.

::: {.slides src="seminar"}
An academic presentation with aligned Chinese and English frames and speaker notes.
:::

## Where this result comes from, and what it covers

Wolfdieter Lang introduced the sequences in 2009; Anthony Browne contributed A164660's final formula on 29 May 2016. The paper explicitly credits an earlier complete Lean proof. Its contributions include a self-contained written explanation, arbitrary-exponent and interval extensions, and two coefficient-table corrections. Prior square-, cube-, and fourth-power counts appear in OEIS A000188, A000189 and A000190. S. Fried proved Yanev's related square-indicator identity in 2025.

The [existing formal proof](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.lean) represents the integral by its finite rational coefficient sum and states the two original equalities for every positive $n$. The complete initial-value and denominator formulas and the arbitrary-exponent, translated-interval formulas have written proofs here. Coverage of the original identity does not by itself establish formal coverage of those extensions.

Finally, summing rational coefficients and then taking the numerator differs from summing the separate numerators: $1/2+1/3=5/6$ has numerator $5$, whereas $1+1=2$. The paper supplies no new closed formulas for the separate-sum sequences A164662 and A164663. Finite prefix checks do not replace all-index proofs. The [precise chapter](statements.md) contains the proofs, corrections and original sources; the [contribution guide](contribute.md) links the shared tasks for the remaining mathematical interfaces and extensions.
