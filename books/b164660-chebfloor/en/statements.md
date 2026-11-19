# Precise statements and complete proofs

This chapter gives the content of Theorem 1, Proposition 2 and Proposition 3 of [Haobo Ma and Wenlin Zhang, version 1](https://doi.org/10.5281/zenodo.23884883). The preceding examples are instances of these statements. Original result numbers refer to the manuscript, not this explanation's chapter numbers.

## Objects and main conclusion

Let $T_0(x)=1$, $T_1(x)=x$, and $T_{m+1}(x)=2xT_m(x)-T_{m-1}(x)$ for $m\ge1$. Write $[x^j]T_m$ for the coefficient of $x^j$. Set

$$
\begin{aligned}
I_m&=\int_0^1T_m(x)\,dx\\
&=\sum_{j=1}^{m+1}\frac{[x^{j-1}]T_m(x)}{j}.
\end{aligned}
$$

Let $a(m)$ and $d(m)$ be the signed numerator and positive denominator of $I_m$ in lowest terms. The radical $\operatorname{rad}(n)$ is the product of its distinct prime factors, with $\operatorname{rad}(1)=1$. For positive integers $n,r$ and an integer $s$, write

$$
\delta_n(t)=\left\lfloor\frac tn\right\rfloor-
\left\lfloor\frac{t-1}{n}\right\rfloor\quad(t\in\mathbb Z),
$$

$$
P_r(n;s)=\prod_{k=s+1}^{s+n}\bigl(1-2\delta_n(k^r)\bigr).
$$

All division inside floors is rational division; subtract $1$ before the second division.

::: {.theorem #thm-browne title="Browne's numerator and product identity" mathesis="collected:b164660-chebfloor:1:s1" lean="D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.result"}
For every positive integer $n$,

$$
\begin{aligned}
a(n+1)&=P_n(n;0),\\
P_n(n;0)&=(-1)^{n/\operatorname{rad}(n)}.
\end{aligned}
$$
:::

::: proof
[@prop-integrals] gives $a(n+1)=1$ exactly when $4\mid n$. For $n\ge2$, take $r=n,s=0$ in [@prop-roots]. If $p^e\mid n$, then $e\le2^e\le p^e\le n$, so $\lceil e/n\rceil=1$. The count is therefore $n/\operatorname{rad}(n)$, even precisely when $4\mid n$, and the two signs agree. At $n=1$, $P_1(1;0)=1-2(1-0)=-1$, $a(2)=-1$, and $1/\operatorname{rad}(1)=1$. This includes the endpoint.
:::

**Exact sign description.** The equal quantities are $+1$ when $4\mid n$ and $-1$ otherwise. Directly, for odd $n$, $n/\operatorname{rad}(n)$ is odd. For $n=2^tu$ with $u$ odd and $t\ge1$, the quotient has $2$-exponent $t-1$, so it is even exactly when $t\ge2$. This sign argument also occurs among the auxiliary arguments consumed by the existing formal proof. The theorem box above states exactly the two equalities of its public main conclusion.

## Integral and denominator formulas

::: {.proposition #prop-integrals title="Complete integral, numerator and denominator formulas" mathesis="collected:b164660-chebfloor:1:s2" status="written-proof" proof="pf-integrals" doi="10.5281/zenodo.23884883" source="Proposition 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/234"}
We have $I_0=1$ and $I_1=1/2$. For $m\ge2$,

$$
I_m=\begin{cases}
-1/(m^2-1),&m\ge2\text{ even},\\
1/(m+1),&m\equiv1\pmod4,\\
-1/(m-1),&m\equiv3\pmod4.
\end{cases}
$$
Consequently $a(0)=1$; for $m\ge1$, $a(m)=1$ exactly when $m\equiv1\pmod4$, and $a(m)=-1$ otherwise. Also $d(0)=1$, and for $m\ge1$,

$$
d(m)=\begin{cases}
m^2-1,&m\ge2\text{ even},\\
m+1,&m\equiv1\pmod4,\\
m-1,&m\equiv3\pmod4.
\end{cases}
$$
The second branch includes $m=1$.
:::

<a id="integral-proof"></a>

::: {.proof #pf-integrals}
Following the manuscript's Proposition 2: the cosine addition formula and recurrence imply $T_m(\cos\theta)=\cos(m\theta)$ for every $m\ge0$. In the substitution $x=\cos\theta$, $dx=-\sin\theta\,d\theta$; endpoints $x=0,1$ correspond to $\theta=\pi/2,0$. Hence

$$
I_m=\int_0^{\pi/2}\cos(m\theta)\sin\theta\,d\theta.
$$

For $m\ge2$, the identity $2\sin\theta\cos(m\theta)=\sin((m+1)\theta)-\sin((m-1)\theta)$ yields

$$
\begin{aligned}
I_m={}&\frac{1-\cos((m+1)\pi/2)}{2(m+1)}\\
&-\frac{1-\cos((m-1)\pi/2)}{2(m-1)}.
\end{aligned}
$$

For even $m$, both cosines vanish and the difference is $-1/(m^2-1)$. For $m\equiv1\pmod4$, they are respectively $-1,1$, giving $1/(m+1)$; for $m\equiv3\pmod4$, they are $1,-1$, giving $-1/(m-1)$. The polynomials $T_0=1$ and $T_1=x$ give $I_0,I_1$ directly, avoiding the zero denominator that would occur in the intermediate expression at $m=1$. Every displayed denominator is positive and coprime to $\pm1$, so the fractions are reduced. This proves both numerator and denominator assertions.
:::

The two odd branches, including $m=1$, combine into

$$
I_m=\frac{(-1)^{(m-1)/2}}
{2\bigl(2\lfloor(m-1)/4\rfloor+1\bigr)}.
$$

Substituting $m=4q+1$ or $4q+3$ recovers the two expressions. This proves the preceding rational-integral conjecture in A164660; the denominator formula gives A164661.

## Arbitrary exponents and translated intervals

::: {.proposition #prop-roots title="Exact root count and product invariance" mathesis="collected:b164660-chebfloor:1:s3" status="written-proof" proof="pf-roots" doi="10.5281/zenodo.23884883" source="Proposition 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/235"}
Let $n,r\ge1$ be integers, write $n=\prod_{p\mid n}p^{e_p}$, and define

$$
\begin{aligned}
D_r(n)&=\prod_{p\mid n}p^{\lceil e_p/r\rceil},\\
C_r(n)&=n/D_r(n).
\end{aligned}
$$
Empty products are $1$. For every integer $s$,

$$
\begin{aligned}
\sum_{k=s+1}^{s+n}\delta_n(k^r)&=C_r(n),\\
P_r(n;s)&=(-1)^{C_r(n)}.
\end{aligned}
$$
For $n>1$, $C_r(n)=n/\operatorname{rad}(n)$ exactly when $r\ge\max_{p\mid n}e_p$; for $n=1$, equality holds for every $r\ge1$. For every $r\ge2$, $P_r(n;s)=a(n+1)$, independently of $s$.
:::

::: {.proof #pf-roots}
Following the manuscript's Proposition 3, prove the detector, count, threshold and sign in that order. For any integer $t$, Euclidean division gives $t=qn+u$, $0\le u<n$. At $u=0$ the floors are $q,q-1$; at $u>0$ both are $q$. Thus $\delta_n(t)$ detects $n\mid t$, including negative integers and zero.

For nonzero integer $k$, let $v_p(k)$ denote the exponent of $p$ in $|k|$. Then

$$
\begin{aligned}
n\mid k^r
&\Longleftrightarrow r v_p(k)\ge e_p\quad(p\mid n)\\
&\Longleftrightarrow D_r(n)\mid k.
\end{aligned}
$$

Both divisibility conditions also hold at $k=0$. Since $D_r(n)\mid n$, the number of multiples in $s+1,\ldots,s+n$ is

$$
\left\lfloor\frac{s+n}{D_r(n)}\right\rfloor-
\left\lfloor\frac{s}{D_r(n)}\right\rfloor=\frac n{D_r(n)}.
$$

Summing the indicators gives this count; each success contributes one negative factor, giving $(-1)^{C_r(n)}$.

For $n>1$, equality $C_r(n)=n/\operatorname{rad}(n)$ holds exactly when every $\lceil e_p/r\rceil=1$, equivalently every $e_p\le r$. This proves the sharp threshold. At $n=1$, the empty product and count are both $1$.

Finally let $r\ge2$. For odd $n$, $C_r(n)$ is odd. If $t=v_2(n)\ge1$, then

$$
v_2(C_r(n))=t-\lceil t/r\rceil.
$$

At $t=1$ this is zero. For $t\ge2$, $\lceil t/r\rceil\le\lceil t/2\rceil\le t-1$, so it is positive. Thus the count is even precisely when $4\mid n$. [@prop-integrals] identifies its product with $a(n+1)$. At $r=1$, $D_1(n)=n$ and $C_1(n)=1$, so the product is always $-1$, explaining the boundary difference.
:::

The specialization $r=n,s=0$ recovers Browne's 11 May 2016 floor sum in A003557. Bottomley's sufficient condition $n<2^{r+1}$ ensures saturation because $e_p\le\log_2n<r+1$ and $e_p$ is an integer. The largest-prime-exponent condition above is the exact threshold.

## Coefficient corrections and scope

Let $c_{m,j}=[x^j]T_m(x)$, and let $b_{m,j}$ be the coefficient of $x^j$ in its primitive with zero constant term. Termwise integration gives

$$
b_{m,j}=c_{m,j-1}/j\quad(1\le j\le m+1).
$$

Multiplying this column by $j/2^{j-1}$ therefore produces $c_{m,j-1}/2^{j-1}$. The multiplier $j/2^{j-2}$ printed in the COMMENT of A164658 is twice the required value: at $(m,j)=(0,1)$ it gives $2$ instead of $1$.

The recurrence gives $T_7=64x^7-112x^5+56x^3-7x$, hence $b_{7,6}=-112/6=-56/3$. In Lang's table linked from A164660, rational row $n=7$, displayed column $m=5$, the printed $56/3$ needs a minus sign. The table's numerator $-56$ and row sum $-1/6$ agree with the correction. Here $b_{7,6}$ denotes the coefficient of $x^6$ after integration; the displayed table column is a different indexing convention.

These are written corrections from manuscript Section 4. No new closed formulas are supplied for A164662 or A164663: those sum separate reduced coefficient numerators or denominators, unlike the rational row sum here. The manuscript describes finite prefix checks; this explanation does not treat those as all-index proofs and has not executed that program.

## Sources and further reading

- Haobo Ma and Wenlin Zhang, this paper, version 1, Theorem 1, Propositions 2–3 and Sections 4–5. [Version DOI](https://doi.org/10.5281/zenodo.23884883). CC BY 4.0. Haobo Ma: ChronoAI Pte Ltd, Singapore; Wenlin Zhang: National University of Singapore and ChronoAI Pte Ltd, Singapore.
- W. Lang and formula contributor A. Browne: [A164660](https://oeis.org/A164660), revision 19 used by the manuscript; related [A164661](https://oeis.org/A164661), [A164658](https://oeis.org/A164658), [A164659](https://oeis.org/A164659), and coefficient recurrence [A053120](https://oeis.org/A053120).
- [A003557](https://oeis.org/A003557) and [A007947](https://oeis.org/A007947): radical quotient and earlier floor sums; [A000188](https://oeis.org/A000188), [A000189](https://oeis.org/A000189), [A000190](https://oeis.org/A000190): prior power-root counts.
- S. Finch, *Idempotents and Nilpotents Modulo n*, [arXiv:math/0605019v2](https://arxiv.org/abs/math/0605019v2), Section 2.
- NIST DLMF, [18.5.1](https://dlmf.nist.gov/18.5.E1): Chebyshev trigonometric representation.
- S. Fried, *Proofs of some conjectures of Yanev*, 2025, Theorem 1, [public paper](https://oeis.org/A000188/a000188.pdf). Its related square-indicator identity is already proved.
- [Earlier Lean source cited by the manuscript](https://github.com/the-omega-institute/trureturing/blob/122c987d276498783de7d873378a28b27ced8761/D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.lean). The main result's generated source link uses this explanation's full pin; the mathematical statement agrees.
