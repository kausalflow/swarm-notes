---
# CSL-compatible fields
title: "Fine-grained hierarchical crop type classification from integrated hyperspectral EnMAP data and multispectral sentinel-2 time series: A large-scale dataset and dual-stream transformer method"
author:
  - literal: "Wenyuan Li"
  - literal: "Shunlin Liang"
  - literal: "Yuxiang Zhang"
  - literal: "Liqin Liu"
  - literal: "Keyan Chen"
  - literal: "Yongzhe Chen"
  - literal: "Han Ma"
  - literal: "Jianglei Xu"
  - literal: "Yichuan Ma"
  - literal: "Shikang Guan"
  - literal: "Zhenwei Shi"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2506.06155"

# Custom fields
paper_id: "2506.06155"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "multimodal"
  - "transformer"
  - "vision-transformer"
  - "dataset"
  - "benchmark"
  - "image-classification"
architectures:
  - "encoder-decoder"
datasets:
  - "H2 Crop"
concept_slugs:
  - "h2-crop-dataset"
dataset_slugs:
  - "h2-crop"
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:06:39Z"
created_at: "2026-06-11T09:06:39Z"
---

# Fine-grained hierarchical crop type classification from integrated hyperspectral EnMAP data and multispectral sentinel-2 time series: A large-scale dataset and dual-stream transformer method

**Authors**: Wenyuan Li, Shunlin Liang, Yuxiang Zhang, Liqin Liu, Keyan Chen, Yongzhe Chen, Han Ma, Jianglei Xu, Yichuan Ma, Shikang Guan, Zhenwei Shi
**Date**: 2026-06-08
**Paper ID**: [openalex:2506.06155](https://arxiv.org/abs/2506.06155)

## Summary

This paper addresses the challenge of fine-grained crop type classification by constructing H2 Crop, a large-scale hierarchical dataset that integrates EnMAP hyperspectral data with Sentinel-2 multi-temporal imagery. The authors introduce a dual-stream Transformer architecture that employs a spectral-spatial pathway for hyperspectral features and a temporal Swin Transformer for growth pattern analysis. The integrated approach demonstrates significant accuracy improvements over existing methods, providing a robust benchmark for hierarchical agricultural mapping.

## Key Contributions

- Introduces H2 Crop, a large-scale hierarchical dataset with over one million annotated parcels integrating EnMAP hyperspectral and Sentinel-2 multispectral data.
- Proposes a dual-stream Transformer architecture with a spectral-spatial pathway and a temporal Swin Transformer pathway to leverage multimodal agricultural features.
- Demonstrates that integrating hyperspectral data with Sentinel-2 time series improves F1-scores by an average of 4.2%.

## Open Questions & Future Work

- [[addressing-extreme-class-imbalance-in-crop-classification]]
- [[advanced-multi-modal-interaction-strategies]]

## Key Concepts

- [[h2-crop-dataset]]: A large-scale hierarchical crop classification dataset integrating EnMAP hyperspectral imagery and Sentinel-2 time series with over one million annotated field parcels.

## Archivist Review

The paper introduces a significant new hierarchical multimodal dataset for remote sensing and proposes a dual-stream architecture. I have approved the H2 Crop dataset and concept as they represent a substantial contribution to the field. I also approved two high-level open questions regarding class imbalance and multimodal interaction in agricultural remote sensing, which address known bottlenecks in the field.

### Approved Concepts
- H2 Crop Dataset: Provides a large-scale, hierarchical multimodal benchmark integrating hyperspectral and multi-temporal remote sensing data.

### Approved Open Questions
- Addressing Extreme Class Imbalance: Class imbalance is a persistent bottleneck in real-world large-scale remote sensing, hindering the deployment of automated systems for monitoring rare or specialty crops.
- Advanced Multi-Modal Interaction: As remote sensing moves toward foundation models, the ability to effectively fuse diverse data modalities is critical for maximizing the diagnostic utility of integrated satellite systems.

### Rejected Candidates
- [dataset] EnMAP (`enmap`) - other: This is an existing satellite platform/sensor data stream, not a specific research dataset for the vault.
- [dataset] Sentinel-2 (`sentinel-2`) - other: This is a standard satellite data source, not a specific research dataset.

## Datasets

- [[h2-crop]]

## Links

- [Abstract](https://arxiv.org/abs/2506.06155)
- [PDF](https://arxiv.org/pdf/2506.06155)

