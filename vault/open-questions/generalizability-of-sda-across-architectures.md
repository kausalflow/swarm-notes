---
created_at: '2026-06-17T09:25:58Z'
source_papers:
- '[[openalex-2606.15701-robust-transformer-based-one-step-stock-index-forecasting-vi]]'
title: Generalizability of SDA across Architectures
---

**Background:** Data augmentation techniques are essential for improving the robustness of deep learning models, but their application to financial time series remains less explored compared to domains like computer vision and natural language processing. Standard augmentation methods can inadvertently distort the complex, non-stationary temporal dependencies inherent in financial market data.

**Question / Future Work:** While Shifted Data Augmentation (SDA) has demonstrated empirical benefits in stabilizing and improving Transformer-based stock index forecasting, it is necessary to determine whether these benefits generalize to other architectures, such as RNNs, LSTMs, GRUs, or CNNs. Investigating whether the effectiveness of SDA is universal or specifically synergistic with attention-based mechanisms is required to understand its role in financial forecasting.

**Why It Matters:** Establishing the generalizability of SDA across architectures is critical for identifying whether this augmentation strategy addresses fundamental challenges in financial time series modeling or if it only resolves limitations specific to the Transformer architecture.