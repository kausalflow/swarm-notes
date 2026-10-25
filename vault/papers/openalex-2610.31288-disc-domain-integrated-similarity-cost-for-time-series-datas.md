---
# CSL-compatible fields
title: "DISC: Domain-Integrated Similarity Cost for Time-Series Dataset"
author:
  - literal: "Yen-Ku Liu"
  - literal: "Hongjie Chen"
  - literal: "Franck Dernoncourt"
  - literal: "Ryan A. Rossi"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.31288"

# Custom fields
paper_id: "2610.31288"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transfer-learning"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "domain-integrated-similarity-cost-disc"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:29:11Z"
created_at: "2026-10-25T09:29:11Z"
---

# DISC: Domain-Integrated Similarity Cost for Time-Series Dataset

**Authors**: Yen-Ku Liu, Hongjie Chen, Franck Dernoncourt, Ryan A. Rossi
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.31288](https://arxiv.org/abs/2610.31288)

## Summary

The paper investigates how dataset similarity metrics align with downstream transfer learning utility in time-series forecasting. The authors find that existing single-metric similarity references vary heavily in their ability to capture transfer relationships, proving that time-series dataset similarity is inherently task-dependent. To bridge this gap, they introduce Domain-Integrated Similarity Cost (DISC), a learnable aggregation framework that combines complementary metrics using calibration transfer observations. Experimental results show that DISC yields significantly stronger alignment with downstream transfer behavior than manual single-metric selection.

## Key Contributions

- Evaluated the alignment gap between existing time-series dataset similarity metrics and downstream forecasting errors in transfer-learning settings.
- Proposed Domain-Integrated Similarity Cost (DISC), a learnable aggregation framework that selects, weights, and combines similarity metrics using calibration transfer observations.
- Demonstrated that DISC achieves higher alignment with downstream transfer behavior compared to single-metric references on evaluation splits.

## Open Questions & Future Work

- [[generalization-of-learned-time-series-similarity]]

## Key Concepts

- [[domain-integrated-similarity-cost-disc]]: A learnable aggregation framework that combines multiple time-series dataset similarity metrics using calibration transfer observations to better predict downstream transfer utility.

## Archivist Review

Approved the core concept DISC for dataset similarity aggregation and the open question regarding its generalization across partitions and domains. Adhered strictly to the scarcity limits and review policy.

### Approved Concepts
- Domain-Integrated Similarity Cost (DISC): DISC is the core methodological contribution of the paper, offering a learnable framework to aggregate similarity metrics for predicting downstream transfer performance.

### Approved Open Questions
- Generalization of Learned Time-Series Similarity: Understanding whether learned dataset similarity costs overfit to specific dataset splits is crucial for ensuring reliable transferability estimation in general time-series foundation model pipelines.

## Links

- [Abstract](https://arxiv.org/abs/2610.31288)
- [PDF](https://arxiv.org/pdf/2610.31288)

