---
# CSL-compatible fields
title: "Lightweight Wrappers for Adapting Time Series Foundation Models to Regional Drought Forecasting"
author:
  - literal: "Wentao Gao"
  - literal: "Jiuyong Li"
  - literal: "Lin Liu"
  - literal: "Thuc Duy Le"
  - literal: "Jixue Liu"
  - literal: "Yanchang Zhao"
  - literal: "Yun Chen"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17511"

# Custom fields
paper_id: "2607.17511"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "long-context"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "stationarity-aware-multi-resolution-residual-wrapper"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:26:24Z"
created_at: "2026-07-23T07:26:24Z"
---

# Lightweight Wrappers for Adapting Time Series Foundation Models to Regional Drought Forecasting

**Authors**: Wentao Gao, Jiuyong Li, Lin Liu, Thuc Duy Le, Jixue Liu, Yanchang Zhao, Yun Chen
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17511](https://arxiv.org/abs/2607.17511)

## Summary

This paper presents a lightweight, black-box adaptation framework for enhancing frozen Time Series Foundation Models (TSFMs) during inference without modifying backbone weights. The framework introduces two plug-and-play wrappers: SMR^2 for stationarity-aware multi-resolution residual decomposition and ensembling, and MBB for moving block bootstrap-based temporal dependency preservation and stabilization. Evaluated on one-month-ahead SPEI drought forecasting across South Australia sites, the framework achieves up to 26% MSE reduction over frozen backbones while overcoming computational and data constraints.

## Key Contributions

- Introduces a lightweight, black-box adaptation framework requiring no backbone parameter access or fine-tuning for time series foundation models.
- Proposes SMR^2, a stationarity-aware multi-resolution residual wrapper that decomposes inputs and learns stride-specific residual corrections.
- Proposes MBB, a moving block bootstrap wrapper that preserves temporal dependencies and stabilizes point forecasts via ensembling over residual perturbations.
- Achieves up to 26% mean squared error (MSE) reduction over corresponding frozen backbones on one-month-ahead SPEI drought forecasting in South Australia.

## Limitations

Evaluated primarily on one-month-ahead SPEI prediction in South Australia, leaving multi-region and broader climate generalizability open for future work.

## Open Questions & Future Work

- [[temporal-granularity-climate-generalization]]

## Key Concepts

- [[stationarity-aware-multi-resolution-residual-wrapper]]: A stationarity-aware multi-resolution residual wrapper that adapts frozen time series foundation models at inference time via ensembling.

## Archivist Review

Approved the core stationarity-aware multi-resolution residual wrapper concept and one open question concerning generalization across temporal granularities and climate regimes. Rejected the duplicate or classical method-based concepts to preserve vault stringency.

### Approved Concepts
- Stationarity-Aware Multi-Resolution Residual Wrapper: Provides a black-box, inference-time adaptation mechanism for time series foundation models that requires no backbone parameter updates.

### Approved Open Questions
- Generalization to Diverse Temporal Granularities: Determines the scope, limits, and environmental generalizability of zero-shot black-box adaptation frameworks for time series foundation models.

### Rejected Candidates
- [concept] SMR2 Wrapper (`smr2-wrapper`) - duplicate_existing: Redundant with or superseded by the more descriptive canonical concept name 'stationarity-aware-multi-resolution-residual-wrapper'.
- [concept] Moving Block Bootstrap Wrapper (`moving-block-bootstrap-wrapper`) - not_novel: Moving block bootstrap is a classical statistical resampling technique rather than a novel machine learning mechanism unique to this paper.

## Links

- [Abstract](https://arxiv.org/abs/2607.17511)
- [PDF](https://arxiv.org/pdf/2607.17511)

