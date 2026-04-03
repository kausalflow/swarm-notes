---
created_at: '2026-04-03T06:06:17Z'
source_papers:
- '[[openalex-2603.29612-central-limit-theorems-for-the-outputs-of-fully-convolutiona]]'
title: Theoretical foundations of time-series deep learning
---

**Background:** Deep learning models, specifically fully convolutional neural networks, are frequently applied to time series classification and forecasting tasks, yet their theoretical properties in these domains remain poorly characterized. Existing research has primarily focused on the distribution of network outputs for independent, identically distributed, or Gaussian inputs.

**Question / Future Work:** There is a need for a comprehensive theoretical framework that characterizes the asymptotic output distribution of various neural network architectures (e.g., Transformers or recurrent models) when applied to more complex, non-linear, or long-range dependent time series input. Expanding this analysis to include the impact of different training procedures and initialization strategies on the output distribution during inference remains a significant open problem.

**Why It Matters:** Developing a rigorous theory for deep learning in time series is crucial for understanding the inductive biases of these models and provides a foundation for more principled architecture design and interpretation beyond empirical benchmarks.

**Evidence:** A possible future direction is to study the asymptotic activation distribution of transformer architectures if the inputs are time series.