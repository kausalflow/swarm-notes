---
# CSL-compatible fields
title: "GeoNIRS: Geometry-Aware Pretraining for Heterogeneous fNIRS Representation Learning"
author:
  - literal: "Zongsheng Li"
  - literal: "Shengyuan Zhu"
  - literal: "Zimo Zhang"
  - literal: "Hanyao Li"
  - literal: "Shengming Wang"
  - literal: "Quanying Liu"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17845"

# Custom fields
paper_id: "2610.17845"
paper_source: "openalex"
domain: "biology"
tags:
  - "pre-training"
  - "representation-learning"
  - "multimodal"
  - "time-series"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "geonirs"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:25:30Z"
created_at: "2026-10-16T09:25:30Z"
---

# GeoNIRS: Geometry-Aware Pretraining for Heterogeneous fNIRS Representation Learning

**Authors**: Zongsheng Li, Shengyuan Zhu, Zimo Zhang, Hanyao Li, Shengming Wang, Quanying Liu
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17845](https://arxiv.org/abs/2610.17845)

## Summary

GeoNIRS is a geometry-aware pretraining framework designed for functional near-infrared spectroscopy (fNIRS) that overcomes cross-dataset channel layout heterogeneity by utilizing source-detector physical locations as a shared spatial reference. By compressing variable-size channel configurations into a fixed latent representation via bidirectional chromophore cross-reconstruction and temporal masking, GeoNIRS scales across up to 22 datasets without downstream labels. Extensive evaluations across eight held-out tasks demonstrate superior downstream balanced accuracy compared to various conventional and deep-learning baselines.

## Key Contributions

- Introduces GeoNIRS, the first geometry-aware pretraining framework that uses source-detector locations as a shared spatial reference to handle heterogeneous fNIRS probe layouts.
- Scales pretraining up to 22 heterogeneous datasets with bidirectional HbO/HbR cross-reconstruction and contiguous temporal masking.
- Achieves the highest task-averaged balanced accuracy across eight held-out clinical, cognitive, and motor tasks compared to conventional machine-learning, fNIRS-specific, general time-series, and pretraining baselines.
- Improves average balanced accuracy over random initialization by 4.12 percentage points under linear probing and 3.30 points under full fine-tuning.

## Limitations

None explicitly highlighted in the abstract.

## Key Concepts

- [[geonirs]]: A geometry-aware representation learning framework for heterogeneous fNIRS pretraining using source-detector spatial locations.

## Archivist Review

Approved the core concept GeoNIRS as it establishes a distinctive geometry-aware pretraining framework for functional near-infrared spectroscopy. Kept open questions and datasets empty as no universal reusable open question or standalone dataset note met the strict retention bar.

### Approved Concepts
- GeoNIRS: It is the central novel framework of the paper, establishing geometry-aware pretraining across heterogeneous fNIRS probe layouts.

## Links

- [Abstract](https://arxiv.org/abs/2610.17845)
- [PDF](https://arxiv.org/pdf/2610.17845)

