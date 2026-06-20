---
# CSL-compatible fields
title: "SCAN: Enhance Time Series Anomaly Detection via Multi-Scale Neighborhood-Centered Clustering"
author:
  - literal: "Xingze Zheng"
  - literal: "Hanyin Cheng"
  - literal: "Siyuan Wang"
  - literal: "Yiting Hao"
  - literal: "Peng Chen"
  - literal: "Yuan Jun"
  - literal: "Yang Shu"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.19255"

# Custom fields
paper_id: "2606.19255"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "clustering"
  - "representation-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-scale-neighborhood-centered-clustering-scan"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:13Z"
created_at: "2026-06-20T08:17:13Z"
---

# SCAN: Enhance Time Series Anomaly Detection via Multi-Scale Neighborhood-Centered Clustering

**Authors**: Xingze Zheng, Hanyin Cheng, Siyuan Wang, Yiting Hao, Peng Chen, Yuan Jun, Yang Shu
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.19255](https://arxiv.org/abs/2606.19255)

## Summary

SCAN addresses the over-generalization and under-generalization limitations inherent in reconstruction-based time series anomaly detection. By integrating multi-scale clustering, the method constrains model reconstruction toward representative normal patterns using cluster centers. Additionally, it improves detection robustness by deriving an anomaly confidence score from cluster membership, which is used alongside traditional reconstruction error to establish dual criteria for anomaly identification.

## Key Contributions

- Introduces the SCAN framework, which improves reconstruction-based anomaly detection by integrating cluster-center representations to constrain normal pattern learning.
- Proposes a dual-criterion anomaly detection mechanism combining cluster membership probability and reconstruction error to address generalization imbalances.
- Demonstrates state-of-the-art performance in time series anomaly detection by leveraging neighborhood-centered multi-view clustering for refined representation learning.

## Open Questions & Future Work

- [[adaptive-cluster-number-determination-for-time-series-anomaly-detection]]

## Key Concepts

- [[multi-scale-neighborhood-centered-clustering-scan]]: A framework that enhances reconstruction-based time series anomaly detection by integrating cluster-center constraints and neighborhood-centered clustering.

## Archivist Review

The SCAN framework introduces a robust approach to mitigating over-generalization in reconstruction-based time series anomaly detection by enforcing cluster-center constraints. The selected open question addresses the structural limitation of fixed cluster counts, which is a common bottleneck in this class of models. I have excluded any datasets as they were not specified beyond generic descriptors.

### Approved Concepts
- Multi-Scale Neighborhood-Centered Clustering (SCAN): It provides a novel mechanism to balance reconstruction-based anomaly detection by using cluster-center constraints and dual-criterion detection, mitigating common over-generalization issues.

### Approved Open Questions
- Adaptive Cluster Number Determination: The reliance on a fixed cluster count is a significant bottleneck for generalization and practical application in unsupervised settings where the number of underlying patterns is not known a priori.

## Links

- [Abstract](https://arxiv.org/abs/2606.19255)
- [PDF](https://arxiv.org/pdf/2606.19255)

