---
# CSL-compatible fields
title: "Beyond Magnitude and Shape: A Direction-Aware Loss for Time Series Forecasting"
author:
  - literal: "Seunghan Lee"
  - literal: "Jaehoon Lee"
  - literal: "Jun Seo"
  - literal: "Junhyuk Kang"
  - literal: "Sangjun Han"
  - literal: "Sungdong Yoo"
  - literal: "Minjae Kim"
  - literal: "Tae Yoon Lim"
  - literal: "Dongwan Kang"
  - literal: "Hwanil Choi"
  - literal: "Soonyoung Lee"
  - literal: "Wonbin Ahn"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01857"

# Custom fields
paper_id: "2608.01857"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cosdir"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:31:16Z"
created_at: "2026-08-06T07:31:16Z"
---

# Beyond Magnitude and Shape: A Direction-Aware Loss for Time Series Forecasting

**Authors**: Seunghan Lee, Jaehoon Lee, Jun Seo, Junhyuk Kang, Sangjun Han, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01857](https://arxiv.org/abs/2608.01857)

## Summary

This paper introduces CosDir, a direction-aware loss function for time series forecasting that aligns prediction and target difference vectors using cosine similarity to address the shortcomings of MSE on small directional changes. Furthermore, the authors propose CosDir-UW, an adaptive weighting extension that removes the need for manual hyperparameter tuning of the loss mixing ratio. Extensive experiments demonstrate consistent improvements in directional accuracy while maintaining magnitude performance across over 100K runs.

## Key Contributions

- Identified that standard MSE-trained forecasters fail to capture the direction of small moves in time series forecasting.
- Proposed CosDir, a lightweight scale-invariant direction-aware loss function based on cosine similarity of difference vectors.
- Proposed CosDir-UW, an adaptive extension that automatically learns the mixing ratio between directional and magnitude terms without manual hyperparameter tuning.
- Demonstrated through extensive experiments (over 100K runs) that the proposed method consistently improves directional accuracy while preserving magnitude accuracy across diverse benchmarks.

## Open Questions & Future Work

- [[probabilistic-multistep-direction-aware-forecasting]]

## Key Concepts

- [[cosdir]]: A direction-aware loss function that aligns prediction and target difference vectors via cosine similarity to improve directional accuracy.

## Archivist Review

Approved the core loss concept 'CosDir' and the explicit future direction regarding probabilistic multi-step extension, as they are reusable and adhere to vault guidelines. No datasets were approved since none were specifically named in the paper's metadata.

### Approved Concepts
- CosDir: It is the core proposed direction-aware loss function designed to address the limitations of MSE on small directional changes in time series forecasting.

### Approved Open Questions
- Probabilistic and Multi-Step Direction-Aware Forecasting: Extending direction-aware losses to probabilistic and multi-step forecasting addresses a critical limitation in decision-driven applications where uncertainty estimation and multi-horizon trajectory alignment are essential.

## Links

- [Abstract](https://arxiv.org/abs/2608.01857)
- [PDF](https://arxiv.org/pdf/2608.01857)

