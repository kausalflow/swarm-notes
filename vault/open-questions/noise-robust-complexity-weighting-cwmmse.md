---
created_at: '2026-07-19T07:24:49Z'
source_papers:
- '[[openalex-2607.14738-quantifying-the-complexity-of-trajectory-ensembles-with-clus]]'
title: Noise-Robust Complexity Weighting CWMMSE
---

**Background:** Sample entropy measures used within CWMMSE are sensitive to unstructured stochastic noise, which can be incorrectly interpreted as high dynamical complexity.

**Question / Future Work:** Investigating or developing an alternative within-trajectory complexity metric that effectively discriminates between underlying nonlinear dynamical structure and stochastic noise is essential to improve the reliability of CWMMSE in noisy real-world applications.

**Why It Matters:** Reducing sensitivity to unstructured noise would significantly enhance the measure's specificity and prevent misinterpretation of simple noisy systems as dynamically complex.

**Evidence:** A per-trajectory weight that explicitly discounts unstructured noise, in place of the sample entropy used here, would sharpen this separation.