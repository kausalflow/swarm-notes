---
created_at: '2026-03-29T06:08:30Z'
source_papers:
- '[[openalex-2603.25473-causal-insight-probing-temporal-models-to-extract-causal-str]]'
title: Extension to Multi-Horizon Predictors
---

**Background:** The methodology is designed to analyze the dependency structure learned by a temporal predictor, which is currently limited to models that predict the next single time step ($t$) based on history up to $t$.

**Question / Future Work:** Extend the Causal-INSIGHT probing framework to function with multi-horizon or sequence-to-sequence temporal predictors, where the model outputs a prediction spanning multiple future time steps, rather than just the immediate next step.

**Why It Matters:** Many advanced temporal models, especially in sequence forecasting, are multi-horizon, so extending interpretability to these architectures is necessary for broader utility.

**Evidence:** Future work includes extending the probing framework to multi-horizon predictors and developing adaptive clamping schemes to better capture distributed or multi-lag influence patterns.