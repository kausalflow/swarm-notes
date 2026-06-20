---
created_at: '2026-06-20T08:17:13Z'
source_papers:
- '[[openalex-2606.19255-scan-enhance-time-series-anomaly-detection-via-multi-scale-n]]'
title: Adaptive Cluster Number Determination
---

**Background:** Clustering-based anomaly detection models often rely on a predefined number of clusters to partition normal data patterns, which limits the flexibility of these methods when the true number of underlying clusters is unknown.

**Question / Future Work:** Adaptive clustering algorithms are required to automatically determine the optimal number of clusters for diverse and complex time series datasets, eliminating the need for manual hyperparameter tuning of the cluster count.

**Why It Matters:** The reliance on a fixed cluster count is a significant bottleneck for generalization and practical application in unsupervised settings where the number of underlying patterns is not known a priori.

**Evidence:** However, like most clustering methods, SCAN requires a predefined number of clusters, which limits its flexibility. In future work, we plan to evaluate more real-world scenarios and explore adaptive clustering algorithms.