---
# CSL-compatible fields
title: "Multi-task Disentangling Fusion Mamba-CNN for MODIS Spectral-Temporal Unmixing with Endmember Variability Modeling"
author:
  - literal: "Motasem Alkayid"
  - literal: "Yimin Zhu"
  - literal: "Naser El‐Sheimy"
  - literal: "Lincoln Linlin Xu"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36750"

# Custom fields
paper_id: "2610.36750"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "state-space-model"
  - "ssm"
  - "mamba"
  - "multimodal"
  - "time-series"
  - "remote-sensing"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:05:37Z"
created_at: "2026-10-30T11:05:37Z"
---

# Multi-task Disentangling Fusion Mamba-CNN for MODIS Spectral-Temporal Unmixing with Endmember Variability Modeling

**Authors**: Motasem Alkayid, Yimin Zhu, Naser El‐Sheimy, Lincoln Linlin Xu
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36750](https://arxiv.org/abs/2610.36750)

## Summary

The paper introduces the Multi-task Disentangling Fusion Mamba (MDF-Mamba) for spectral-temporal unmixing of MODIS time series, addressing spectral-temporal coupling, intra-class endmember variability, and expert integration instability. MDF-Mamba employs per-channel spectral convolution experts paired with a bidirectional Mamba temporal branch, integrated via a manifold-constrained hyper-connection framework (mHCFusion) with soft reweighting. Additionally, it incorporates an extended linear mixing model with pixel-wise learnable spectral variability weights and a multi-task training objective combining supervised abundance estimation and self-supervised reconstruction. Experiments on MODIS datasets from Alberta and Saskatchewan demonstrate that the framework achieves superior performance across the majority of evaluation metrics.

## Key Contributions

- Proposes MDF-Mamba, a multi-task disentangling fusion architecture combining per-channel spectral convolution experts with a bidirectional Mamba temporal branch for spectral-temporal unmixing.
- Introduces mHCFusion, a manifold-constrained hyper-connection framework for stable and interpretable multi-branch expert representation integration.
- Extends the linear mixing model with pixel-wise learnable spectral variability weights to model intra-class endmember variability and inter-class signature ambiguity.
- Achieves top performance on 12 of 14 evaluation metrics across MODIS datasets covering the Alberta and Saskatchewan provinces.

## Archivist Review

I applied strict selectivity criteria to protect the vault. The paper's open question on multi-year and global scaling is too broad and standard as future work, so it was rejected. No standalone concepts met the threshold for permanent archival notes.

### Rejected Candidates
- [open_question] Multi-Year and Global Spectral Unmixing (`multi-year-global-spectral-unmixing`) - low_impact: Future work proposing scaling to multi-year datasets and broader geographic biomes is too broad and standard for vault inclusion.

## Links

- [Abstract](https://arxiv.org/abs/2610.36750)
- [PDF](https://arxiv.org/pdf/2610.36750)

