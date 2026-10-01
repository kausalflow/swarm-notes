---
created_at: '2026-10-01T11:15:17Z'
source_papers:
- '[[openalex-2609.37078-zerodiff-zero-shot-time-series-reconstruction-via-informed-p]]'
title: Joint Optimization and Co-Adaptation in Diffusion
---

**Background:** Joint optimization of upstream prior generation models and downstream calibration models can cause co-adaptation artifacts that may degrade zero-shot generalization performance across unobserved locations.

**Question / Future Work:** Determine whether joint end-to-end training schemes between prior construction and diffusion calibration can retain their performance gains while effectively suppressing co-adaptation artifacts during cross-location zero-shot time series reconstruction.

**Why It Matters:** Understanding how to jointly optimize modularized prior-informed diffusion pipelines without hurting out-of-domain transferability is a core architectural problem for robust generative reconstruction.

**Evidence:** Two-stage training enforces gradient isolation between the prior and the denoiser, avoiding co-adaptation by construction—a robust default for zero-shot reconstruction. Joint optimization is a viable refinement when domain knowledge indicates a strong, well-identified X→Y coupling. Whether joint schemes can retain these gains while suppressing co-adaptation remains an open direction.