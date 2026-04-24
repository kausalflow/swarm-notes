---
created_at: '2026-04-24T06:58:19Z'
source_papers:
- '[[openalex-2509.14868-dpanet-dual-pyramid-attention-network-for-multivariate-time]]'
title: Adaptive Hierarchical Time-Frequency Decomposition
---

**Background:** Time series forecasting often requires modeling hierarchical structures that encompass both temporal scales and frequency resolutions. While current architectures like dual-stream pyramids facilitate these analyses, the choice of decomposition methods and their interaction remains a subject of research.

**Question / Future Work:** The current approach uses rigid downsampling for the temporal pyramid and pre-defined, logarithmically-spaced band-pass filtering for the frequency pyramid. Future research could explore adaptive, data-driven decomposition mechanisms that dynamically learn the optimal scales and frequency bands tailored to the specific characteristics of the underlying data, rather than relying on fixed transformations.

**Why It Matters:** Fixed decomposition approaches may fail to capture irregular or evolving periodicities present in non-stationary time series, limiting the model's flexibility and potential performance on diverse datasets.

**Evidence:** The frequency pyramid P_f = {F^{(0)}, ..., F^{(S-1)}} is created by decomposing the input series into different frequency resolutions... This logarithmic partitioning is crucial: it allocates finer resolution to the low-frequency components...