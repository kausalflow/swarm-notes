---
# CSL-compatible fields
title: "Cropland PAtteRNS: Parallel Dimensional Attention Networks and Attention to Dataset Disparity for Crop Segmentation in Satellite Imagery Time Series Data"
author:
  - literal: "Joseph Metcalfe"
  - literal: "Sara Sharifzadeh"
  - literal: "Fabio Caraffini"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.38165"

# Custom fields
paper_id: "2609.38165"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
  - "multimodal"
  - "time-series"
  - "image-segmentation"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "pastis"
concept_slugs:
  []
dataset_slugs:
  - "pastis"
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:47:10Z"
created_at: "2026-10-02T10:47:10Z"
---

# Cropland PAtteRNS: Parallel Dimensional Attention Networks and Attention to Dataset Disparity for Crop Segmentation in Satellite Imagery Time Series Data

**Authors**: Joseph Metcalfe, Sara Sharifzadeh, Fabio Caraffini
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.38165](https://arxiv.org/abs/2609.38165)

## Summary

This paper presents Cropland Parallel Attention and Refinement Network for Segmentation (PAtteRNS), a hybrid transformer-convolutional model that applies fully-factorised self-attention separately across temporal, spectral, and spatial dimensions for satellite imagery time series (SITS) crop segmentation. By introducing a novel parallel transformer architecture, the model reduces the computational complexity of triple-factorised attention while outperforming existing state-of-the-art models on the PASTIS and MTLCC datasets, notably in parcel delineation quality (Boundary IoU). Additionally, the authors uncover critical dataset pitfalls, demonstrating that inconsistent tile-size variants and flawed class groupings invalidate fair model comparisons.

## Key Contributions

- Introduces PAtteRNS, the first model applying self-attention separately across temporal, spectral, and spatial dimensions for Sentinel-2 satellite imagery time series (SITS) crop segmentation.
- Proposes a novel parallel transformer architecture achieving fully-factorised attention while significantly reducing the computational complexity of triple-factorised self-attention.
- Demonstrates state-of-the-art performance across multiple tile-size variants of the PASTIS and MTLCC datasets, particularly improving parcel delineation quality measured by Boundary IoU.
- Identifies and analyzes dataset vulnerabilities, showing that flawed class groupings and differing tile-size variants invalidate fair comparisons across models.

## Limitations

Alternative tile-size variants produce incomparable results, indicating that dataset standardisation and dynamic-tile-sizing practices require further research.

## Archivist Review

Strictly enforced selectivity limits: approved only PASTIS as the primary named evaluation dataset while rejecting the paper-local architecture and narrow dataset standardization question.

### Rejected Candidates
- [concept] Cropland Parallel Attention and Refinement Network for Segmentation (`cropland-parallel-attention-and-refinement-network-for-segmentation`) - paper_local: Paper-local architecture name that is unlikely to recur as a general concept in future literature.
- [open_question] SITS Crop Dataset Standardization and Tile Sizing (`sits-crop-dataset-standardization-and-dynamic-tile-sizing`) - low_impact: Too narrow and dataset-specific to be a permanent theoretical open question for the vault.
- [dataset] MTLCC (`mtlcc`) - low_impact: Exceeds the dataset approval limit and is less central than PASTIS.

## Datasets

- [[pastis]]

## Links

- [Abstract](https://arxiv.org/abs/2609.38165)
- [PDF](https://arxiv.org/pdf/2609.38165)

