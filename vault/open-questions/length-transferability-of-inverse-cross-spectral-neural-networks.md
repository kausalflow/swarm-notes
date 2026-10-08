---
created_at: '2026-10-08T11:40:42Z'
source_papers:
- '[[openalex-2610.06630-inverse-cross-spectral-neural-networks-for-multivariate-time]]'
title: Length-Transferability of Inverse Cross-Spectral Neural Networks
---

**Background:** Inverse cross-spectral neural networks (iCSNNs) leverage spectral representation to process stationary multivariate time series using bandwise inverse cross-spectral density (iCSD) operators.

**Question / Future Work:** Investigate whether inverse cross-spectral neural networks trained on time series of length T can generalize to sequences of different lengths (length-transferability), taking advantage of the fact that spectral filtering operators capture general second-order properties of the underlying stationary process rather than a specific observation horizon.

**Why It Matters:** Evaluating length-transferability is crucial for understanding whether graph neural networks operating in the spectral domain can maintain robust predictive performance across varying temporal observation windows without retraining.

**Evidence:** A promising research direction is to investigate whether iCSNNs trained on time series of length T can generalize to sequences of different lengths (length-transferability).