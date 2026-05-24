---
created_at: '2026-05-24T07:46:12Z'
source_papers:
- '[[openalex-2605.22672-is-capability-a-liability-more-capable-language-models-make]]'
title: LLM knowledge-calibration gap mechanisms
---

**Background:** Large language models often exhibit inverse scaling in distributional forecasting tasks on time series characterized by superlinear growth and potential regime change. This failure manifests as the over-extrapolation of growth trends, leading to miscalibrated upper-tail predictions when regime changes occur.

**Question / Future Work:** The discrepancy between a model's latent knowledge of regime-prone trends and its inability to translate that knowledge into calibrated predictive distributions remains a significant barrier to reliable forecasting. Investigation into why this internal knowledge fails to manifest in the tails of predictive distributions, even when prompted, is essential.

**Why It Matters:** Understanding this gap is critical for developing more robust AI forecasting systems, particularly for tail-sensitive domains where inaccurate forecasts lead to severe real-world consequences.

**Evidence:** Prompt-level interventions cannot tell us why a recoverable prior fails to translate into calibrated tails.