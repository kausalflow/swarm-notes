---
created_at: '2026-03-27T14:08:24Z'
source_papers:
- '[[openalex-2603.19899-deep-autocorrelation-modeling-for-time-series-forecasting-pr]]'
title: Modernizing Statistical Methods
---

**Background:** Canonical statistical methods for time-series analysis, such as those involving generalized least squares (GLS) or structured covariance kernels in Gaussian processes, provide theoretical insights into handling autocorrelation but are difficult to integrate into modern deep learning pipelines due to constraints with mini-batch training.

**Question / Future Work:** A critical research direction involves modernizing canonical statistical methods by developing new learning objectives that explicitly incorporate complex label autocorrelation structures, making concepts from classical statistics like GLS or structured covariance modeling compatible with the end-to-end training paradigm of deep neural networks.