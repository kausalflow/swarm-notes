---
created_at: '2026-08-13T06:08:50Z'
source_papers:
- '[[openalex-2608.09692-evaluating-generative-time-series-models-on-data-with-point]]'
title: Native Point-Mass Generative Modeling
---

**Background:** Many time-series datasets contain point masses (such as exact zeros), which standard continuous-state generative models cannot natively represent.

**Question / Future Work:** Develop generative time-series architectures and training objectives that can natively model mixed data distributions combining point masses (atoms) and continuous values, without relying on heuristics or post-hoc thresholding.

**Why It Matters:** Current continuous-state models like flows and diffusion struggle fundamentally with data containing probability masses on single values, leading to evaluation anomalies and poor modeling of intermittent phenomena.

**Evidence:** A model is therefore being asked to reproduce, on more than half of the observations in some of these datasets, a feature it cannot represent.