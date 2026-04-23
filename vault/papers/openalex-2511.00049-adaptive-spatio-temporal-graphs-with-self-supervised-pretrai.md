---
# CSL-compatible fields
title: "Adaptive spatio-temporal graphs with self-supervised pretraining for multi-horizon weather forecasting"
author:
  - literal: "Y. A. Liu"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2511.00049"

# Custom fields
paper_id: "2511.00049"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "gnn"
  - "self-supervised-learning"
  - "forecasting"
  - "time-series"
architectures:
  []
datasets:
  - "era5"
  - "merra-2"
concept_slugs:
  []
dataset_slugs:
  - "era5"
  - "merra-2"
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:55:55Z"
created_at: "2026-04-23T06:55:55Z"
---

# Adaptive spatio-temporal graphs with self-supervised pretraining for multi-horizon weather forecasting

**Authors**: Y. A. Liu
**Date**: 2026-04-20
**Paper ID**: [openalex:2511.00049](https://arxiv.org/abs/2511.00049)

## Summary

This paper presents a self-supervised learning framework for multi-variable weather forecasting that effectively models the complex spatio-temporal dynamics of atmospheric systems. By integrating a graph neural network (GNN) for spatial dependency capture and a spatio-temporal adaptation mechanism for multi-horizon robustness, the model achieves state-of-the-art performance. Evaluations on the ERA5 and MERRA-2 datasets demonstrate the method's superior precision compared to both classical numerical weather prediction and recent deep learning approaches. The work highlights the efficacy of combining self-supervised representation learning with structural modeling to create more scalable and label-efficient weather forecasting systems.

## Key Contributions

- Introduces a self-supervised learning framework that exploits spatio-temporal structures to improve multi-variable weather forecasting accuracy.
- Integrates a graph neural network with a novel spatio-temporal adaptation mechanism, improving generalization across different forecasting horizons.
- Outperforms traditional numerical weather prediction (NWP) models and existing deep learning baselines on the ERA5 and MERRA-2 reanalysis benchmarks.

## Open Questions & Future Work

- [[dynamic-graph-weather-forecasting]]
- [[improving-extreme-weather-prediction]]

## Archivist Review

The paper focuses on standard techniques (GNNs and self-supervised learning) applied to a domain already well-represented in the vault. Therefore, no new concepts were approved. However, the open questions regarding dynamic graph construction and extreme event robustness address significant, recurring challenges in the meteorological forecasting literature. The datasets ERA5 and MERRA-2 were approved as they are foundational benchmarks for the field.

### Approved Open Questions
- Dynamic Graph Weather Forecasting: Static graph structures fail to capture the transient nature of weather patterns, limiting the model's ability to maintain high precision during complex or rapidly changing atmospheric events.
- Extreme Weather Prediction Robustness: Extreme weather events have significant societal and economic impacts; improving model performance during these conditions is critical for emergency preparedness and public safety.

### Rejected Candidates
- [concept] Graph Neural Network (`graph-neural-network`) - generic: This is a broad, well-established architectural paradigm, not a specific novel concept from this paper.
- [concept] Self-Supervised Learning (`self-supervised-learning`) - generic: This is a standard machine learning paradigm rather than a specific contribution unique to this paper.

## Datasets

- [[era5]]
- [[merra-2]]

## Links

- [Abstract](https://arxiv.org/abs/2511.00049)
- [PDF](https://arxiv.org/pdf/2511.00049)

