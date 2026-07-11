---
# CSL-compatible fields
title: "Temporal-Spatial Tubelet Embedding for Cloud-Robust MSI Reconstruction using MSI-SAR Fusion: A Multi-Head Self-Attention Video Vision Transformer Approach"
author:
  - literal: "Yiqun Wang"
  - literal: "Lujun Li"
  - literal: "Meiru Yue"
  - literal: "Radu State"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2512.09471"

# Custom fields
paper_id: "2512.09471"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "transformer"
  - "multi-head-attention"
  - "vision-transformer"
  - "multimodal"
  - "vision-language-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "temporal-spatial-tubelet-embedding"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:06:12Z"
created_at: "2026-07-11T07:06:12Z"
---

# Temporal-Spatial Tubelet Embedding for Cloud-Robust MSI Reconstruction using MSI-SAR Fusion: A Multi-Head Self-Attention Video Vision Transformer Approach

**Authors**: Yiqun Wang, Lujun Li, Meiru Yue, Radu State
**Date**: 2026-07-08
**Paper ID**: [openalex:2512.09471](https://arxiv.org/abs/2512.09471)

## Summary

This paper introduces MTS-ViViT, a reconstruction framework designed to address cloud-induced spectral degradation in multispectral imagery (MSI) for agricultural monitoring. By replacing coarse temporal sequence aggregation with a localized temporal-spatial tubelet embedding mechanism using constrained 3D convolutions, the model preserves local spatio-temporal coherence. The framework is evaluated in both MSI-only and SAR-MSI fusion scenarios, consistently outperforming baseline ViT-based architectures in reconstruction accuracy on real-world agricultural data.

## Key Contributions

- Proposes a Video Vision Transformer (ViViT)-based framework using localized temporal-spatial tubelet embedding to improve MSI reconstruction under cloud cover.
- Introduces a 3D convolution-based tokenization with a constrained temporal span (t=2) to preserve local spectral-temporal coherence.
- Demonstrates that the MTS-ViViT framework achieves a 2.23% MSE reduction over the MTS-ViT baseline and a 10.33% improvement when integrating SAR data.

## Open Questions & Future Work

- [[flexible-spatiotemporal-embedding-for-irregular-sampling]]

## Key Concepts

- [[temporal-spatial-tubelet-embedding]]: A localized tokenization mechanism using 3D convolutions with a constrained temporal span to represent spatio-temporal video data in transformers.

## Archivist Review

I approved the temporal-spatial tubelet embedding as it provides a reusable architectural mechanism for improving transformers in spatio-temporal tasks. I also approved the open question regarding flexible embedding for irregular sampling, as it addresses a significant bottleneck in remote sensing reconstruction. The paper's contribution is well-defined, and the rejected datasets are not sufficiently critical or novel for separate vault notes.

### Approved Concepts
- Temporal-Spatial Tubelet Embedding: This is the core architectural contribution, replacing coarse temporal sequence aggregation with localized 3D tubelets to preserve local spatio-temporal coherence.

### Approved Open Questions
- Flexible Spatiotemporal Embedding Strategy: Current aggregation methods limit the model's adaptability to real-world scenarios where remote sensing data are often sparse, irregularly sampled, or inconsistent across space and time.

## Links

- [Abstract](https://arxiv.org/abs/2512.09471)
- [PDF](https://arxiv.org/pdf/2512.09471)

