---
created_at: '2026-08-01T07:23:22Z'
source_papers:
- '[[openalex-2607.26820-forecasting-trajectory-level-safety-risks-in-black-box-multi]]'
title: Category-Aware Risk Forecasting Calibration
---

**Background:** Safety guardrails for multi-turn large language model interactions typically operate reactively by detecting explicit violations rather than predicting latent risk accumulation across dialogue trajectories.

**Question / Future Work:** Investigating how to design effective category-aware calibration mechanisms and specialized temporal encoders to improve multi-turn safety risk forecasting and early warning performance across diverse harm categories (such as cybersecurity and chemical/biological risks) where predictive uncertainty remains high.

**Why It Matters:** Important for bridging performance gaps across highly technical or sensitive harm domains where standard temporal forecasting models struggle with high false alarm rates and calibration issues.

**Evidence:** Cybersecurity remains the most challenging category for temporal forecasting, achieving an NLL of 0.56 and an Expected-MAE of 0.41. These results indicate that Recast learns transferable trajectory-level risk patterns across diverse harm domains, while highlighting the need for category-aware calibration in practical deployments.