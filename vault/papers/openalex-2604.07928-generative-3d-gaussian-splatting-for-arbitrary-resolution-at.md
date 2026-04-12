---
# CSL-compatible fields
title: "Generative 3D Gaussian Splatting for Arbitrary-Resolution Atmospheric Downscaling and Forecasting"
author:
  - literal: "Tao Hana"
  - literal: "Zhibin Wen"
  - literal: "Zhenghao Chen"
  - literal: "Fenghua Lin"
  - literal: "Junyu Gao"
  - literal: "Song Guo"
  - literal: "Lei Bai"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.07928"

# Custom fields
paper_id: "2604.07928"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "attention-mechanism"
  - "vision-transformer"
  - "multimodal"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "ERA5"
  - "CMIP6"
concept_slugs:
  - "generative-3d-gaussian-atmospheric-modeling"
dataset_slugs:
  - "era5"
  - "cmip6"
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:19:13Z"
created_at: "2026-04-12T06:19:13Z"
---

# Generative 3D Gaussian Splatting for Arbitrary-Resolution Atmospheric Downscaling and Forecasting

**Authors**: Tao Hana, Zhibin Wen, Zhenghao Chen, Fenghua Lin, Junyu Gao, Song Guo, Lei Bai
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.07928](https://arxiv.org/abs/2604.07928)

## Summary

The paper introduces GSSA-ViT, a novel framework for atmospheric forecasting and downscaling that treats grid points as 3D Gaussians. By predicting Gaussian parameters instead of raw grid values, the model achieves better generalization and supports arbitrary output resolutions. A specialized scale-aware attention mechanism is integrated to effectively manage cross-scale information, enabling unified multi-scale prediction across diverse meteorological scenarios.

## Key Contributions

- Proposes GSSA-ViT, a framework that uses generative 3D Gaussian splatting for arbitrary-resolution atmospheric forecasting.
- Introduces a scale-aware attention module that captures cross-scale dependencies for flexible downscaling ratios.
- Demonstrates superior performance across 87 atmospheric variables on ERA5 and CMIP6 datasets compared to traditional high-resolution NWP models.

## Open Questions & Future Work

- [[mitigating-autoregressive-weather-forecasting-error-accumulation]]

## Key Concepts

- [[generative-3d-gaussian-atmospheric-modeling]]: A representation of atmospheric fields as a set of generative 3D Gaussians, allowing for continuous-resolution spatial forecasting and multi-scale downscaling.

## Archivist Review

I approved the generative 3D Gaussian atmospheric modeling approach as it defines a novel, reusable paradigm for continuous-resolution scientific forecasting. The open question regarding autoregressive error accumulation was retained as a critical, high-impact bottleneck for the field. I rejected the framework name itself in favor of the more descriptive modeling concept, and excluded the generic call for 'efficient attention' as it is a common, non-specific bottleneck in modern transformer research.

### Approved Concepts
- Generative 3D Gaussian Atmospheric Modeling: Represents atmospheric fields as continuous, generative 3D Gaussians instead of discrete grid points, enabling resolution-agnostic forecasting and downscaling.

### Approved Open Questions
- Mitigating Autoregressive Forecasting Error Accumulation: Error accumulation is a fundamental bottleneck for autoregressive AI weather models; solving it is critical for extending the reliable lead time of data-driven forecasting systems.

### Rejected Candidates
- [concept] GSSA-ViT (`gssa-vit`) - subcomponent_of_broader_mechanism: The specific framework name is a subcomponent or instance of the broader concept of Generative 3D Gaussian atmospheric modeling.
- [open_question] Efficient Sparse Global Attention (`efficient-sparse-attention-global-forecasting`) - generic: Generic call for 'efficient attention' is a widely recognized problem and lacks specific technical novelty or focus in the context of this paper.

## Datasets

- [[era5]]
- [[cmip6]]

## Links

- [Abstract](https://arxiv.org/abs/2604.07928)
- [PDF](https://arxiv.org/pdf/2604.07928)

