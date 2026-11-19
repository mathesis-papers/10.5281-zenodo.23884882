# 参与形式化

原始的分子—取整乘积恒等式已有[公开 Lean 证明](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.lean)。参与者可以复用其中的结构，完善以下两个精确范围不同的任务：

- [完整积分的初始值与最简分母](https://github.com/the-omega-institute/trureturing-requests/issues/234)：对应[完整积分公式](statements.md#prop-integrals)。已有证明使用了正指标的有理行和求值。任务是在此基础上给出可复用的完整陈述，补齐初始值、最简分母投影，以及所选接口需要的积分与系数和之间的联系。
- [任意指数与平移区间的精确计数](https://github.com/the-omega-institute/trureturing-requests/issues/235)：对应[根计数公式](statements.md#prop-roots)。将已有整除检测推广到任意正指数和整数区间，保留精确阈值与边界。计数本身不依赖积分；最后与积分分子相认时才使用其符号公式。

两项均已有[版本 1 的书面证明](https://doi.org/10.5281/zenodo.23884883)，不是尚未解决的数学猜想。系数表的两处订正也在精确章节中逐项推导；它们不属于原始乘积恒等式的自动验证范围。

请在对应共享问题中协调工作范围，在自己的贡献者分支或 fork 中实现，遵循[上游贡献规则](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)，将聚焦的 PR 直接提交到上游 `dev`。保留原始问题提出者、论文作者与形式化贡献者各自的署名。Mathesis fork 不是必须经过的合入步骤；PR 合入与平台独立验证记录也各有其职责。

<style>pre:has(> code[class*="typst"]) { display: none; }</style>

```{=typst}
#pagebreak()
```
