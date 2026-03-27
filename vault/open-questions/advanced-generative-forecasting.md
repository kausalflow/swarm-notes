---
created_at: '2026-03-27T14:08:24Z'
source_papers:
- '[[openalex-2603.19899-deep-autocorrelation-modeling-for-time-series-forecasting-pr]]'
title: Explore Advanced Generative Paradigms
---

**Background:** Conditional generative models, such as diffusion and autoregressive models, show promise for capturing the complex dependencies within target time-series sequences, thereby modeling label autocorrelation effectively. However, they suffer from limitations like training instability (diffusion models) or error accumulation over long horizons (autoregression models).

**Question / Future Work:** Future work in learning objectives should explore two complementary paths for advanced generative methods: 1) mitigating the inherent limitations of existing paradigms (e.g., refining diffusion models for better stability or reducing error accumulation in autoregression for long horizons) which are exacerbated in time-series forecasting, and 2) exploring cutting-edge generative paradigms like bridge models, continuous normalizing flows, and neural optimal transport models to potentially introduce beneficial inductive biases and enhance label autocorrelation modeling.