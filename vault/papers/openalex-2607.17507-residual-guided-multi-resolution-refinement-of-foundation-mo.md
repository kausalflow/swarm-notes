---
# CSL-compatible fields
title: "Residual-Guided Multi-Resolution Refinement of Foundation Models: A Case Study in Drought Forecasting"
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
url: "https://arxiv.org/abs/2607.17507"

# Custom fields
paper_id: "2607.17507"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "residual-guided-multi-resolution-refinement"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:26:51Z"
created_at: "2026-07-23T07:26:51Z"
---

# Residual-Guided Multi-Resolution Refinement of Foundation Models: A Case Study in Drought Forecasting

**Authors**: Wentao Gao, Jiuyong Li, Lin Liu, Thuc Duy Le, Jixue Liu, Yanchang Zhao, Yun Chen
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17507](https://arxiv.org/abs/2607.17507)

## Summary

The paper introduces RGMR (Residual-Guided Multi-Resolution Refinement), an inference-time wrapper designed to adapt frozen time series foundation models for regional climate prediction. Mimicking expert climatologists' iterative error diagnosis, RGMR performs structured coarse-to-fine refinement without updating backbone parameters. Evaluated on drought forecasting using SPEI across multiple sites with TimesFM, TimeGPT, and TabPFN backbones, RGMR consistently lowers test-set MSE, including an up to 18.9\% reduction in one-month-ahead SPEI MSE.

## Key Contributions

- Introduces RGMR (Residual-Guided Multi-Resolution Refinement), an inference-time wrapper that adapts frozen time series foundation models for multi-scale regional climate forecasting without backbone retraining.
- Demonstrates architecture-agnostic compatibility across TimesFM, TimeGPT, and TabPFN backbones.
- Achieves up to an 18.9% reduction in one-month-ahead SPEI MSE (mean reduction approximately 18.7%) across South Australian evaluation sites.

## Limitations

Evaluated specifically on drought forecasting using SPEI across limited geographical sites.

## Open Questions & Future Work

- [[stacking-tta-and-output-refinement]]

## Key Concepts

- [[residual-guided-multi-resolution-refinement]]: An inference-time framework that adapts frozen time series foundation models via structured coarse-to-fine residual-guided refinement.

## Archivist Review

The concept of inference-time residual-guided multi-resolution refinement is approved as a reusable paradigm for adapting frozen foundation models. The open question regarding stacking test-time adaptation and output refinement is approved due to its technical clarity. No datasets meet the strict criteria for standalone archival notes.

### Approved Concepts
- Residual-Guided Multi-Resolution Refinement: Introduces a novel inference-time framework for multi-resolution refinement of frozen time series foundation models using residual guidance.

### Approved Open Questions
- Stacking Test-Time Adaptation and Output Refinement: Combining parameter-based test-time adaptation with output-space refinement frameworks represents an important architectural exploration for balancing model stability and plasticity under distribution shifts.

## Links

- [Abstract](https://arxiv.org/abs/2607.17507)
- [PDF](https://arxiv.org/pdf/2607.17507)

