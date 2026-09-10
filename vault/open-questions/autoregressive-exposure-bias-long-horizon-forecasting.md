---
created_at: '2026-09-10T09:16:17Z'
source_papers:
- '[[openalex-2609.09140-noah-learning-the-full-patient-journey-a-longitudinal-multim]]'
title: Mitigating Autoregressive Exposure Bias
---

**Background:** Autoregressive generative models trained on longitudinal multimodal patient data face limitations from autoregressive exposure bias and error accumulation over long prediction horizons.

**Question / Future Work:** Investigate and mitigate autoregressive exposure bias and error propagation during long-horizon rollouts in multimodal generative patient journey models, potentially through advanced post-training techniques or larger reliable training corpora.

**Why It Matters:** Exposure bias and error propagation limit the reliability of multi-step autoregressive rollouts for long-term clinical forecasting and simulation.

**Evidence:** However, Noah comes with the exposure bias of autoregressive models: it trains predicting one token ahead under teacher forcing with ground truth predecessors, while at rollout it iteratively consumes re-encoded predictions.