---
# CSL-compatible fields
title: "Hierarchical Spatio-Temporal Transformer for Coherent Emergency Department Forecasting"
author:
  - literal: "Filipa Lino"
  - literal: "Bárbara Tavares"
  - literal: "Carlos Santiago"
  - literal: "Cláudia Soares"
  - literal: "Manuel Marques"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.27106"

# Custom fields
paper_id: "2607.27106"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "multimodal"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "hierarchical-spatio-temporal-transformer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-01T07:22:57Z"
created_at: "2026-08-01T07:22:57Z"
---

# Hierarchical Spatio-Temporal Transformer for Coherent Emergency Department Forecasting

**Authors**: Filipa Lino, Bárbara Tavares, Carlos Santiago, Cláudia Soares, Manuel Marques
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.27106](https://arxiv.org/abs/2607.27106)

## Summary

The paper introduces HierSTT, a hierarchical spatio-temporal Transformer framework designed for coherent multi-level emergency department forecasting. By combining temporal fusion networks for macro dynamics with spatio-temporal encoder-decoder modules and a coherence-aware loss, the model jointly predicts hospital, regional, and national demand. Evaluated on a new nationwide Portuguese dataset of 81 hospitals, HierSTT outperforms classical hierarchical reconciliation and non-hierarchical deep learning baselines by 32% in WAPE.

## Key Contributions

- Proposes HierSTT, a hierarchical Transformer-based framework that jointly predicts hospital, regional, and national emergency department demand end-to-end.
- Introduces a coherence-aware loss function that penalizes cross-level inconsistencies during training to ensure mathematically coherent multi-resolution forecasts.
- Demonstrates a 32% reduction in average WAPE relative to the best non-hierarchical deep learning baseline on a nationwide Portuguese ED dataset covering 81 hospitals.

## Limitations

Evaluation is restricted to emergency department demand forecasting and relies on a newly introduced proprietary nationwide dataset without public cross-domain benchmarks.

## Open Questions & Future Work

- [[hierarchical-coherence-deep-learning]]

## Key Concepts

- [[hierarchical-spatio-temporal-transformer]]: A hierarchical Transformer-based framework for coherent multi-level emergency department demand forecasting.

## Archivist Review

Approved the core Hierarchical Spatio-Temporal Transformer mechanism and the open question regarding joint hierarchical coherence optimization in deep forecasting. Rejected unnamed paper-local datasets.

### Approved Concepts
- Hierarchical Spatio-Temporal Transformer: Introduces a novel end-to-end framework for joint multi-level hospital demand forecasting with a coherence-aware loss.

### Approved Open Questions
- Joint Hierarchical Coherence Optimization: Understanding how to jointly optimize forecasting accuracy and hierarchical coherence across heterogeneous networks is crucial for multi-level resource allocation and planning in healthcare and other distributed systems.

## Links

- [Abstract](https://arxiv.org/abs/2607.27106)
- [PDF](https://arxiv.org/pdf/2607.27106)

