---
# CSL-compatible fields
title: "MATNet: multi-level fusion transformer-based model for day-ahead PV generation forecasting"
author:
  - literal: "Matteo Tortora"
  - literal: "Francesco Conte"
  - literal: "Gianluca Natrella"
  - literal: "Paolo Soda"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2306.10356"

# Custom fields
paper_id: "2306.10356"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
architectures:
  - "encoder-only"
datasets:
  - "ausgrid"
concept_slugs:
  - "multi-level-joint-fusion"
dataset_slugs:
  - "ausgrid"
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:08:57Z"
created_at: "2026-07-17T07:08:57Z"
---

# MATNet: multi-level fusion transformer-based model for day-ahead PV generation forecasting

**Authors**: Matteo Tortora, Francesco Conte, Gianluca Natrella, Paolo Soda
**Date**: 2026-07-14
**Paper ID**: [openalex:2306.10356](https://arxiv.org/abs/2306.10356)

## Summary

MATNet is a transformer-based architecture designed for multi-step, day-ahead photovoltaic (PV) power generation forecasting that effectively fuses historical PV data with physics-informed Numerical Weather Prediction (NWP) inputs. By employing a multi-level joint fusion approach with hierarchical soft-attention mechanisms, the model successfully captures complex interactions between diverse data modalities. Extensive evaluation on the Ausgrid benchmark demonstrates significant performance gains over existing AI-based baselines, while secondary experiments confirm the model's robustness to missing data and its efficacy in zero-shot cross-site transfer scenarios.

## Key Contributions

- Proposes MATNet, a transformer-based multimodal architecture designed for day-ahead PV generation forecasting.
- Implements a multi-level joint fusion strategy that integrates historical PV data with physics-derived weather covariates via soft-attention.
- Demonstrates a 65% RMSE improvement over state-of-the-art baselines on the Ausgrid benchmark dataset, alongside robust cross-site zero-shot transferability.

## Open Questions & Future Work

- [[adaptive-multimodal-fusion-resilience]]

## Key Concepts

- [[multi-level-joint-fusion]]: An architectural strategy that integrates multimodal time-series inputs by performing fusion at multiple hierarchical stages using soft-attention mechanisms.

## Archivist Review

The paper presents a specific architectural approach to multimodal time-series fusion that is potentially reusable across various forecasting applications. I have approved this concept and the related open question regarding resilience to changing conditions. The 'Ausgrid' dataset is also approved as a recognized benchmark in PV generation research. I rejected the 'Explainable PV Forecasting' question as it is currently too generic, applying broadly to all ML models rather than being a specific, trackable technical bottleneck unique to these architectures.

### Approved Concepts
- Multi-level Joint Fusion: This is the core architectural innovation of the model, enabling the integration of heterogeneous historical sensor data and exogenous weather covariates across multiple hierarchy levels.

### Approved Open Questions
- Adaptive Multimodal Fusion Resilience: This addresses a primary bottleneck in current multimodal forecasting architectures, where fixed fusion strategies fail to handle non-stationary or adverse environmental scenarios.

## Datasets

- [[ausgrid]]

## Links

- [Abstract](https://arxiv.org/abs/2306.10356)
- [PDF](https://arxiv.org/pdf/2306.10356)

