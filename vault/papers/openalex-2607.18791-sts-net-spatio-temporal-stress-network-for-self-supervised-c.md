---
# CSL-compatible fields
title: "STS-NET: Spatio-Temporal Stress Network for Self-Supervised Crop Stress Detection using Satellite Image Time Series"
author:
  - literal: "Pradeep Dalal"
  - literal: "Rajiv Ranjan"
  - literal: "Sushil Ghildiyal"
  - literal: "Shashank Tamaskar"
  - literal: "Neeraj Goel"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.18791"

# Custom fields
paper_id: "2607.18791"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "self-supervised-learning"
  - "time-series"
  - "convolutional-neural-network"
  - "remote-sensing"
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
processed_at: "2026-07-24T07:25:01Z"
created_at: "2026-07-24T07:25:01Z"
---

# STS-NET: Spatio-Temporal Stress Network for Self-Supervised Crop Stress Detection using Satellite Image Time Series

**Authors**: Pradeep Dalal, Rajiv Ranjan, Sushil Ghildiyal, Shashank Tamaskar, Neeraj Goel
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.18791](https://arxiv.org/abs/2607.18791)

## Summary

This paper introduces STS-NET, a spatio-temporal stress network built on a self-supervised 3D-convolutional autoencoder for crop stress detection using satellite image time series (SITS). By leveraging four vegetation indices derived from high-resolution Planetscope imagery and trained on the BSPT dataset, the model effectively detects water, nitrogen, and combined stresses in sugarcane crops with high precision. The approach demonstrates strong performance with minimal reliance on labeled training data, highlighting its utility as a robust feature extractor.

## Key Contributions

- Introduces STS-NET, a self-supervised 3D-convolutional autoencoder utilizing satellite image time series (SITS) for crop stress detection.
- Leverages four vegetation indices (NDVI, GNDVI, RECI, and NDRE) from Planetscope imagery to capture spatiotemporal stress patterns.
- Evaluated on a real-world sugarcane dataset, achieving 97.98% precision for water stress, 85.08% for nitrogen stress, and 83.47% for combined stress.

## Archivist Review

Applied strict archiving standards, rejecting the paper-specific spatio-temporal network model and its localized cross-region transfer open question as application-bound and lacking broad ML vault reusability.

### Rejected Candidates
- [concept] Spatio-Temporal Stress Network (STS-NET) (`sts-net`) - paper_local: Paper-local remote-sensing model combining standard 3D-CNN autoencoders with vegetation indices, lacking broad cross-domain machine learning reusability.
- [open_question] Cross-Region Crop Stress Generalization (`cross-region-crop-stress-generalization`) - low_impact: Standard application-specific transfer challenge rather than a fundamental theoretical bottleneck in time series or machine learning.

## Links

- [Abstract](https://arxiv.org/abs/2607.18791)
- [PDF](https://arxiv.org/pdf/2607.18791)

