---
created_at: '2026-04-12T06:19:24Z'
source_papers:
- '[[openalex-2604.07764-bayesian-tensor-on-tensor-varying-coefficient-model-for-fore]]'
title: Non-linear GP Tensor Regression
---

**Background:** Tensor-on-tensor (TOT) regression models are often limited by the assumption of linear dependencies between input and output tensors, which may not capture complex non-linear relationships present in multimodal or longitudinal imaging data. While Gaussian process (GP) priors have been proposed to address non-linearity, their effective integration into high-dimensional TOT frameworks remains challenging due to computational scalability concerns.

**Question / Future Work:** There is a need to further investigate and extend the adoption of Gaussian process (GP) priors to tackle non-linearity in tensor-on-tensor regression models. Existing methods often rely on linear assumptions, and while the current work proposes a Bayesian framework incorporating GP priors for voxel-wise non-linear effects, the generalizability and further refinement of these semi-parametric approaches in more diverse imaging or tensor-based applications remains an open area for study.

**Why It Matters:** This is technically important because it addresses the core modeling limitation of linearity in high-dimensional tensor regression, which is critical for accurately capturing complex biological or physical processes in longitudinal studies.

**Evidence:** However, the adoption of GPs to tackle non-linearity in TOT regression models is limited, to our knowledge.