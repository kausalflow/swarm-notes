---
# CSL-compatible fields
title: "Distributed JEPA: A Self-Supervised Framework for Energy Forecasting"
author:
  - literal: "Liana Toderean"
  - literal: "Tudor Cioara"
  - literal: "Vasilis Michalakopoulos"
  - literal: "Efstathios Sarantinopoulos"
  - literal: "Ionut Anghel"
  - literal: "Elissaios Sarmas"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.17029"

# Custom fields
paper_id: "2609.17029"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "self-supervised-learning"
  - "transformer"
  - "robustness"
  - "representation-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "distributed-jepa"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:28Z"
created_at: "2026-09-17T09:43:28Z"
---

# Distributed JEPA: A Self-Supervised Framework for Energy Forecasting

**Authors**: Liana Toderean, Tudor Cioara, Vasilis Michalakopoulos, Efstathios Sarantinopoulos, Ionut Anghel, Elissaios Sarmas
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.17029](https://arxiv.org/abs/2609.17029)

## Summary

The paper introduces a distributed Joint Embedding Predictive Architecture (JEPA) for self-supervised learning from heterogeneous energy time-series, predicting latent representations of masked temporal segments while integrating contextual information. To prevent representation collapse, the training combines latent-space prediction with covariance and temporal variance regularization. Evaluations on energy consumption and generation datasets demonstrate high representation stability, competitive performance against Transformers on building data, higher R2 on consumer clusters, and superior robustness to missing data on unseen photovoltaics.

## Key Contributions

- Proposes a distributed Joint Embedding Predictive Architecture (JEPA) for self-supervised learning from heterogeneous energy time-series.
- Combines a latent-space predictive objective with covariance and temporal variance regularization to prevent representation collapse.
- Achieves competitive performance with Transformer baselines on building data, higher R2 in 3/5 consumer clusters, and superior performance on unseen PVs under missing data degradation.

## Limitations

Evaluated primarily on energy consumption and generation datasets; scalability to broader industrial time-series remains to be explored.

## Key Concepts

- [[distributed-jepa]]: A distributed Joint Embedding Predictive Architecture (JEPA) for self-supervised learning from heterogeneous energy time-series.

## Archivist Review

Approved the core framework concept 'Distributed JEPA' as it represents a distinct self-supervised architectural application for heterogeneous energy time-series. No datasets or open questions met the strict standalone thresholds.

### Approved Concepts
- Distributed JEPA: Central novelty of the paper, introducing a distributed Joint Embedding Predictive Architecture tailored for self-supervised learning on heterogeneous energy time-series.

## Links

- [Abstract](https://arxiv.org/abs/2609.17029)
- [PDF](https://arxiv.org/pdf/2609.17029)

