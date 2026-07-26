---
created_at: '2026-07-26T07:29:54Z'
source_papers:
- '[[openalex-2607.21080-nipping-the-butterfly-effect-in-the-bud-self-output-fine-tun]]'
title: Global-Scale Autoregressive Weather Prediction
---

**Background:** Autoregressive deep learning weather prediction models suffer from rapid error accumulation over long forecasting horizons due to distribution shifts between training data and recursively generated inputs.

**Question / Future Work:** Investigate how self-output fine-tuning and similar distribution-matching calibration strategies scale and perform when extended from regional settings to global-scale autoregressive weather forecasting models.

**Why It Matters:** Scaling regional distribution correction methods to global domains is essential for validating their operational robustness and generalization in large-scale atmospheric systems.

**Evidence:** While validated on standard ERA5 benchmarks, our experiments are currently limited to a regional East Asia subset. Global-scale deployment remains future work.