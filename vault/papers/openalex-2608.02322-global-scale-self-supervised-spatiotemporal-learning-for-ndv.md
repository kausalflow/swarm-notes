---
# CSL-compatible fields
title: "Global-Scale Self-Supervised Spatiotemporal Learning for NDVI Time-Series Reconstruction"
author:
  - literal: "Ang Li"
  - literal: "Menghui Jiang"
  - literal: "Xiaobin Guan"
  - literal: "Dong Chu"
  - literal: "Huanfeng Shen"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.02322"

# Custom fields
paper_id: "2608.02322"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "self-supervised-learning"
  - "time-series"
  - "forecasting"
  - "spatiotemporal"
  - "remote-sensing"
  - "attention-mechanism"
  - "convlstm"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:31:37Z"
created_at: "2026-08-06T07:31:37Z"
---

# Global-Scale Self-Supervised Spatiotemporal Learning for NDVI Time-Series Reconstruction

**Authors**: Ang Li, Menghui Jiang, Xiaobin Guan, Dong Chu, Huanfeng Shen
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.02322](https://arxiv.org/abs/2608.02322)

## Summary

The paper introduces GloSSR, a global-scale self-supervised spatiotemporal learning framework for reconstructing cloud-contaminated and noise-corrupted Normalized Difference Vegetation Index (NDVI) time series. GloSSR overcomes the lack of paired clean and degraded observations by generating realistic self-supervised training signals via simulated cloud contamination. The architecture combines a bidirectional Transformer and a ConvLSTM to capture multi-scale spatiotemporal correlations, supported by a specialized prior constraint that preserves phenological trends and fine spatial structures. Extensive evaluations on MODIS and AVHRR data prove its effectiveness, scalability, and robustness for large-scale environmental monitoring.

## Key Contributions

- Proposed GloSSR, a global-scale self-supervised spatiotemporal learning framework for cloud-contaminated NDVI time series reconstruction using realistic artificial cloud contamination degradation.
- Introduced an end-to-end network combining a bidirectional Transformer and ConvLSTM to jointly capture long-range temporal dependencies and short-term spatiotemporal correlations.
- Designed a spatiotemporal prior constraint to preserve fine-scale structures and long-term phenological trends during reconstruction.
- Demonstrated superior performance across artificial degradation and real-world MODIS NDVI observations, alongside strong transferability to AVHRR data.

## Archivist Review

The proposed concept GloSSR is specific to remote sensing NDVI time-series reconstruction using standard architectural backbones (Transformer + ConvLSTM), making it too paper-local for permanent standalone vault inclusion under strict selectivity guidelines.

### Rejected Candidates
- [concept] GloSSR (`glossr`) - paper_local: GloSSR is a paper-specific framework combining standard bidirectional transformers and ConvLSTM for NDVI reconstruction, lacking broad standalone reusability across diverse time-series tasks outside remote sensing.

## Links

- [Abstract](https://arxiv.org/abs/2608.02322)
- [PDF](https://arxiv.org/pdf/2608.02322)

