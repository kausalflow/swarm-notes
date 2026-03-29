---
created_at: '2026-03-29T06:08:10Z'
source_papers:
- '[[openalex-2603.25687-on-neural-scaling-laws-for-weather-emulation-through-continu]]'
title: Saturation bottleneck in extreme scaling
---

**Background:** Scaling laws derived from deep learning models in scientific domains, such as weather emulation, can exhibit saturation or breakdown when extrapolated to frontier scales due to factors like data limitations or overfitting.

**Question / Future Work:** Investigate whether the observed performance saturation of the 1.3B parameter model, which required training for over 13 epochs, is indeed due to overfitting or if other factors, such as fundamental limits imposed by the dataset size or spatiotemporal resolution, are the primary cause of the scaling law breakdown at extreme compute levels.

**Why It Matters:** Determining the true bottleneck for performance saturation (data limits vs. overfitting) is crucial for planning future resource allocation and architectural improvements in large-scale Scientific Machine Learning models.

**Evidence:** This large-scale experiment shows signs of saturation before reaching the projected loss. This suggests that scaling in this regime may become limited by data size and spatiotemporal resolution, highlighting the importance of neural scaling analyses for diagnosing when progress may require scaling data rather than model complexity. [...] The validation loss plateaus at around 0.053, pointing to significant overfitting.