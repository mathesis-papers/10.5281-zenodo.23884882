# 精确陈述与完整证明

本章按原论文的定理 1、命题 2、命题 3 给出精确内容。前一章的例子是这些陈述的实例；所有原文编号均指 [Haobo Ma 与 Wenlin Zhang，版本 1](https://doi.org/10.5281/zenodo.23884883)，而非本说明的章节编号。

## 对象与主结论

$T_0(x)=1$、$T_1(x)=x$，且对 $m\ge1$ 有 $T_{m+1}(x)=2xT_m(x)-T_{m-1}(x)$。令 $[x^j]T_m$ 表示 $x^j$ 的系数。定义

$$
\begin{aligned}
I_m&=\int_0^1T_m(x)\,dx\\
&=\sum_{j=1}^{m+1}\frac{[x^{j-1}]T_m(x)}{j}.
\end{aligned}
$$

令 $a(m)$ 和 $d(m)$ 分别是 $I_m$ 的最简带符号分子与正分母。$\operatorname{rad}(n)$ 是 $n$ 不同质因子的乘积，并约定 $\operatorname{rad}(1)=1$。对正整数 $n,r$、整数 $s$，记

$$
\delta_n(t)=\left\lfloor\frac tn\right\rfloor-
\left\lfloor\frac{t-1}{n}\right\rfloor\quad(t\in\mathbb Z),
$$

$$
P_r(n;s)=\prod_{k=s+1}^{s+n}\bigl(1-2\delta_n(k^r)\bigr).
$$

所有取整中的除法都是有理数除法；第二个分子先减 $1$。

::: {.theorem #thm-browne title="Browne 的分子与乘积恒等式" mathesis="collected:b164660-chebfloor:1:s1" lean="D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.result"}
对每个正整数 $n$，

$$
\begin{aligned}
a(n+1)&=P_n(n;0),\\
P_n(n;0)&=(-1)^{n/\operatorname{rad}(n)}.
\end{aligned}
$$
:::

::: proof
[@prop-integrals] 给出 $a(n+1)=1$ 当且仅当 $4\mid n$。[@prop-roots] 在 $r=n,s=0,n\ge2$ 时给出计数 $n/\operatorname{rad}(n)$：若 $p^e\mid n$，则 $e\le2^e\le p^e\le n$，因而 $\lceil e/n\rceil=1$。该计数为偶数当且仅当 $4\mid n$，故两边相等。$n=1$ 时，$P_1(1;0)=1-2(1-0)=-1$，$a(2)=-1$，且 $1/\operatorname{rad}(1)=1$。这也说明边界值被包含。
:::

**符号的精确描述。** 上述两个相等的量在 $4\mid n$ 时为 $+1$，否则为 $-1$。直接论证为：奇数 $n$ 的 $n/\operatorname{rad}(n)$ 为奇数；若 $n=2^tu$，其中 $u$ 为奇数、$t\ge1$，则商中 $2$ 的指数为 $t-1$，它为偶数恰好当 $t\ge2$。这一符号描述也在现有形式证明所使用的辅助论证中出现；上面的定理框严格陈述其公开主结论的两个等式。

## 积分与分母

::: {.proposition #prop-integrals title="完整积分、分子和分母公式" mathesis="collected:b164660-chebfloor:1:s2" status="written-proof" proof="pf-integrals" doi="10.5281/zenodo.23884883" source="Proposition 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/234"}
$I_0=1$，$I_1=1/2$。对 $m\ge2$，

$$
I_m=\begin{cases}
-1/(m^2-1),&m\ge2\text{ 为偶数},\\
1/(m+1),&m\equiv1\pmod4,\\
-1/(m-1),&m\equiv3\pmod4.
\end{cases}
$$
因此 $a(0)=1$，且对 $m\ge1$，$a(m)=1$ 当且仅当 $m\equiv1\pmod4$，其余情形 $a(m)=-1$。此外 $d(0)=1$，对 $m\ge1$，

$$
d(m)=\begin{cases}
m^2-1,&m\ge2\text{ 为偶数},\\
m+1,&m\equiv1\pmod4,\\
m-1,&m\equiv3\pmod4.
\end{cases}
$$
第二个分支包括 $m=1$。
:::

<a id="integral-proof"></a>

::: {.proof #pf-integrals}
依据原文命题 2。由余弦加法公式与递推，对所有 $m\ge0$，$T_m(\cos\theta)=\cos(m\theta)$。代入 $x=\cos\theta$ 时，$dx=-\sin\theta\,d\theta$，$x=0,1$ 分别对应 $\theta=\pi/2,0$，故

$$
I_m=\int_0^{\pi/2}\cos(m\theta)\sin\theta\,d\theta.
$$

对 $m\ge2$，由 $2\sin\theta\cos(m\theta)=\sin((m+1)\theta)-\sin((m-1)\theta)$，得到

$$
\begin{aligned}
I_m={}&\frac{1-\cos((m+1)\pi/2)}{2(m+1)}\\
&-\frac{1-\cos((m-1)\pi/2)}{2(m-1)}.
\end{aligned}
$$

若 $m$ 为偶数，两个余弦均为零，所得差为 $-1/(m^2-1)$。若 $m\equiv1\pmod4$，两个余弦依次为 $-1,1$，给出 $1/(m+1)$；若 $m\equiv3\pmod4$，则依次为 $1,-1$，给出 $-1/(m-1)$。$T_0=1$ 与 $T_1=x$ 直接给出 $I_0,I_1$，避免在 $m=1$ 处使用含零分母的公式。每一分母均为正，且与 $\pm1$ 互素，故已经约分。于是分子与分母断言都成立。
:::

奇数 $m\ge1$ 的两个分支还可合成

$$
I_m=\frac{(-1)^{(m-1)/2}}
{2\bigl(2\lfloor(m-1)/4\rfloor+1\bigr)}.
$$

写 $m=4q+1$ 或 $4q+3$ 即可分别还原两式。这给出 A164660 中前一条有理积分猜想，分母公式给出 A164661。

## 任意指数与平移区间

::: {.proposition #prop-roots title="精确根计数与乘积的不变性" mathesis="collected:b164660-chebfloor:1:s3" status="written-proof" proof="pf-roots" doi="10.5281/zenodo.23884883" source="Proposition 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/235"}
设整数 $n,r\ge1$，$n=\prod_{p\mid n}p^{e_p}$，定义

$$
\begin{aligned}
D_r(n)&=\prod_{p\mid n}p^{\lceil e_p/r\rceil},\\
C_r(n)&=n/D_r(n).
\end{aligned}
$$
空乘积为 $1$。对每个整数 $s$，

$$
\begin{aligned}
\sum_{k=s+1}^{s+n}\delta_n(k^r)&=C_r(n),\\
P_r(n;s)&=(-1)^{C_r(n)}.
\end{aligned}
$$
若 $n>1$，则 $C_r(n)=n/\operatorname{rad}(n)$ 当且仅当 $r\ge\max_{p\mid n}e_p$；若 $n=1$，则对所有 $r\ge1$ 都相等。对所有 $r\ge2$，$P_r(n;s)=a(n+1)$，与 $s$ 无关。
:::

::: {.proof #pf-roots}
依据原文命题 3，依次证明检测、计数、阈值与符号。对任意整数 $t$ 作欧几里得除法 $t=qn+u$，$0\le u<n$。$u=0$ 时两个取整为 $q,q-1$，$u>0$ 时均为 $q$，故 $\delta_n(t)$ 恰为 $n\mid t$ 的指标。这也覆盖负数和零。

对非零整数 $k$，令 $v_p(k)$ 表示 $|k|$ 分解中 $p$ 的指数，则

$$
\begin{aligned}
n\mid k^r
&\Longleftrightarrow r v_p(k)\ge e_p\quad(p\mid n)\\
&\Longleftrightarrow D_r(n)\mid k.
\end{aligned}
$$

$k=0$ 时两个整除条件也都成立。由于 $D_r(n)\mid n$，区间 $s+1,\ldots,s+n$ 中倍数的个数为

$$
\left\lfloor\frac{s+n}{D_r(n)}\right\rfloor-
\left\lfloor\frac{s}{D_r(n)}\right\rfloor=\frac n{D_r(n)}.
$$

指标求和就是这个数量；每个成功者贡献一个 $-1$，故乘积为 $(-1)^{C_r(n)}$。

$n>1$ 时，$C_r(n)=n/\operatorname{rad}(n)$ 等价于每个 $\lceil e_p/r\rceil=1$，即每个 $e_p\le r$，给出充要阈值。$n=1$ 时空乘积与计数均为 $1$。

最后设 $r\ge2$。奇数 $n$ 的 $C_r(n)$ 为奇数。若 $t=v_2(n)\ge1$，则

$$
v_2(C_r(n))=t-\lceil t/r\rceil.
$$

$t=1$ 时该值为零；$t\ge2$ 时，$\lceil t/r\rceil\le\lceil t/2\rceil\le t-1$，所以该值为正。因此计数为偶数恰好当 $4\mid n$。由[@prop-integrals]，其乘积等于 $a(n+1)$。当 $r=1$ 时，$D_1(n)=n$、$C_1(n)=1$，乘积总为 $-1$，解释了边界差异。
:::

计数公式在 $r=n,s=0$ 时还原 Browne 在 A003557 中 2016 年 5 月 11 日的取整和。Bottomley 在该数列中的条件 $n<2^{r+1}$ 足以保证计数饱和，因为 $e_p\le\log_2n<r+1$ 且 $e_p$ 为整数；这里的最大质数指数条件是精确阈值。

## 系数表订正与范围

令 $c_{m,j}=[x^j]T_m(x)$，$b_{m,j}$ 是常数项为零的原函数中 $x^j$ 的系数。逐项积分直接给出

$$
b_{m,j}=c_{m,j-1}/j\quad(1\le j\le m+1).
$$

所以将该列乘 $j/2^{j-1}$ 后，得到的是 $c_{m,j-1}/2^{j-1}$。A164658 的 COMMENT 所印 $j/2^{j-2}$ 多了一倍；在 $(m,j)=(0,1)$ 就会给出 $2$ 而不是 $1$。

由递推 $T_7=64x^7-112x^5+56x^3-7x$，故 $b_{7,6}=-112/6=-56/3$。Lang 在 A164660 下链接的表中，行 $n=7$、显示列 $m=5$ 的 $56/3$ 应为负号；该表的分子 $-56$ 与行和 $-1/6$ 均与订正一致。这里的 $b_{7,6}$ 标的是积分后 $x^6$ 的系数，避免把表的显示列号当成幂次。

这些是原文第 4 节的书面订正。本文未给 A164662、A164663 的新闭式；它们分别相加各个约分后系数的分子或分母，与这里的有理行和不同。原文描述的程序检查仅涉及有限前缀，本说明不将其当作全指标证明，也未执行该程序。

## 来源与阅读线索

- Haobo Ma、Wenlin Zhang，本文版本 1，定理 1、命题 2、命题 3 及第 4–5 节。[版本 DOI](https://doi.org/10.5281/zenodo.23884883)。CC BY 4.0。Haobo Ma：ChronoAI Pte Ltd, Singapore；Wenlin Zhang：National University of Singapore 与 ChronoAI Pte Ltd, Singapore。
- W. Lang 与公式贡献者 A. Browne：[A164660](https://oeis.org/A164660)，原文采用修订 19；相关 [A164661](https://oeis.org/A164661)、[A164658](https://oeis.org/A164658)、[A164659](https://oeis.org/A164659) 与系数递推 [A053120](https://oeis.org/A053120)。
- [A003557](https://oeis.org/A003557) 与 [A007947](https://oeis.org/A007947)：根基商与此前的取整和；[A000188](https://oeis.org/A000188)、[A000189](https://oeis.org/A000189)、[A000190](https://oeis.org/A000190)：此前的幂根计数。
- S. Finch，*Idempotents and Nilpotents Modulo n*，[arXiv:math/0605019v2](https://arxiv.org/abs/math/0605019v2)，第 2 节。
- NIST DLMF，[18.5.1](https://dlmf.nist.gov/18.5.E1)：Chebyshev 三角表示。
- S. Fried，*Proofs of some conjectures of Yanev*，2025，定理 1，[公开论文](https://oeis.org/A000188/a000188.pdf)。其相关平方指标结论是已有证明。
- [原论文所引用的较早 Lean 源码](https://github.com/the-omega-institute/trureturing/blob/122c987d276498783de7d873378a28b27ced8761/D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.lean)。当前说明所用的完整修订见主结论的自动来源链接；数学陈述相同。
