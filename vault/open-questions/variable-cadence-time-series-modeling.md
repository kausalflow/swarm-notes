---
created_at: '2026-07-03T07:56:14Z'
source_papers:
- '[[openalex-2606.31627-multi-scale-contrastive-attention-for-light-curve-representa]]'
title: Native variable-cadence representation learning
---

**Background:** Astronomical surveys often produce time-series data with highly heterogeneous observational cadences across different photometric filters. Current Transformer-based models for time-series representation learning often rely on lossy pre-processing like padding or fixed-length truncation.

**Question / Future Work:** Developing architectures capable of natively processing the full, irregular temporal structure of astronomical light curves without relying on fixed-length input constraints or heuristic fusion techniques remains a significant challenge for time-series representation learning.

**Why It Matters:** This is a central bottleneck in time-domain astronomy, as it limits the ability to process raw data efficiently without loss of information.