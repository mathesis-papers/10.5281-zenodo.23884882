# OEIS A164660, final FORMULA (29 May 2016): Chebyshev numerators and floor products

**Authors:** Haobo Ma, Wenlin Zhang

We prove Anthony Browne's conjecture in OEIS A164660, final FORMULA (29 May 2016): for every positive integer n, the reduced numerator of the integral from 0 to 1 of T_(n+1)(x) equals the stated floor product and (-1)^(n/rad(n)). Both sides are +1 exactly when 4 divides n. The same calculation proves the preceding rational-integral conjecture and gives its denominator sequence A164661. More generally, replacing the exponent n in the product by any integer r >= 2, and translating its interval by any integer, leaves the product unchanged. We give the exact root count for every r >= 1 and correct two coefficient-table discrepancies in the linked sources.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23884883](https://doi.org/10.5281/zenodo.23884883)
- Concept DOI: [https://doi.org/10.5281/zenodo.23884882](https://doi.org/10.5281/zenodo.23884882)
- License: CC-BY-4.0
- Version: 1
- Mathesis record: [b164660-chebfloor](https://mathesis-omega-research.apps.chrono-ai.fun/papers/b164660-chebfloor?version=1)

## How to cite

Haobo Ma, Wenlin Zhang (2026). OEIS A164660, final FORMULA (29 May 2016): Chebyshev numerators and floor products. Mathesis, version 1. https://doi.org/10.5281/zenodo.23884883

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/122c987d276498783de7d873378a28b27ced8761/D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.lean) | No public receipt |
| Proposition (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/122c987d276498783de7d873378a28b27ced8761/D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.lean) | No public receipt |
| Proposition (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/122c987d276498783de7d873378a28b27ced8761/D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23884882/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23884882/b164660-chebfloor/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23884882/b164660-chebfloor/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23884882/b164660-chebfloor/slides/) ([sources](books/b164660-chebfloor/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23884882/b164660-chebfloor/films/) ([sources](books/b164660-chebfloor/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23884882/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `thm-browne` | same | `D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.result` |
| `prop-integrals` | variant | `D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.result` |
| `prop-roots` | special case | `D5/S3/ArithSums/BrowneA164660ChebyshevFloorProduct.result` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/b164660-chebfloor/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
