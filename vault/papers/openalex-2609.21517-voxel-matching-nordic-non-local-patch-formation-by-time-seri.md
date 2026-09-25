---
# CSL-compatible fields
title: "Voxel-Matching NORDIC: Non-local patch formation by time-series similarity increases tSNR in high-resolution BOLD fMRI"
author:
  - literal: "Alessandro Nigi"
  - literal: "Natalia Petridou"
  - literal: "Jeroen C.W. Siero"
issued:
  date-parts:
    - [2026, 9, 24]
url: "https://arxiv.org/abs/2609.21517"

# Custom fields
paper_id: "2609.21517"
paper_source: "openalex"
domain: "medicine"
tags:
  - "anomaly-detection"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:54:35Z"
created_at: "2026-09-25T09:54:35Z"
---

# Voxel-Matching NORDIC: Non-local patch formation by time-series similarity increases tSNR in high-resolution BOLD fMRI

**Authors**: Alessandro Nigi, Natalia Petridou, Jeroen C.W. Siero
**Date**: 2026-09-24
**Paper ID**: [openalex:2609.21517](https://arxiv.org/abs/2609.21517)

## Summary

Submillimeter BOLD fMRI suffers from low signal-to-noise ratio (SNR), which traditional local-patch NORDIC denoising struggles with due to mixed tissue signals within local spatial patches. To overcome this, the authors propose voxel-matching (VM) NORDIC, which constructs non-local patches by grouping voxels with similar time-series. Results demonstrate that VM-NORDIC significantly enhances temporal SNR and signal redundancy while preserving spatial sharpness compared to standard local NORDIC.

## Key Contributions

- Proposes voxel-matching (VM) NORDIC, an alternative non-local patch formation strategy for BOLD fMRI denoising based on time-series similarity.
- Achieves a temporal SNR (tSNR) improvement of ~9-90% over standard local-patch NORDIC and ~23-250% over original data on submillimeter-resolution BOLD fMRI.
- Preserves spatial smoothness effectively, producing only ~20% of the spatial smoothness induced by standard local-patch NORDIC.

## Archivist Review

Applied strict selectivity standards, rejecting the paper-specific neuroimaging denoising concept as domain-local and non-reusable across broader machine learning or time-series forecasting tasks.

### Rejected Candidates
- [concept] Voxel-Matching NORDIC (`voxel-matching-nordic`) - paper_local: The method is a paper-specific application of non-local patching to BOLD fMRI denoising (NORDIC), which is highly specialized for neuroimaging rather than a broad, reusable time-series or machine learning forecasting concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.21517)
- [PDF](https://arxiv.org/pdf/2609.21517)

