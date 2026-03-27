---
created_at: '2026-03-27T14:08:24Z'
source_papers:
- '[[openalex-2603.19899-deep-autocorrelation-modeling-for-time-series-forecasting-pr]]'
title: Autocorrelation-guided Foundation Models
---

**Background:** The development of large-scale foundation models for time-series forecasting is hindered by a lack of a general-purpose, large-scale pretraining corpus that captures the diverse temporal patterns found across different domains. Furthermore, tokenization methods must be advanced to effectively encode the rich semantic information within time-series data.

**Question / Future Work:** A key future direction involves leveraging the concept of autocorrelation to address the challenges in developing large-scale time-series foundation models. This includes two sub-directions: 1) using autocorrelation to generate high-quality synthetic data or augment existing datasets to mitigate data scarcity and learn domain-invariant temporal dynamics, and 2) designing tokenizers that explicitly account for complex, multi-scale, and non-stationary autocorrelation patterns, moving beyond current patch-based methods to unlock the full potential of large models.