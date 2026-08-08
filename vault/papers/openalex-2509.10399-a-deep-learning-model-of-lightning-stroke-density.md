---
# CSL-compatible fields
title: "A Deep Learning Model of Lightning Stroke Density"
author:
  - literal: "Randall E. Jones"
  - literal: "Joel A. Thornton"
  - literal: "Chris J. Wright"
  - literal: "R. H. Holzworth"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2509.10399"

# Custom fields
paper_id: "2509.10399"
paper_source: "openalex"
domain: "time-series"
tags:
  - "convolutional-neural-network"
  - "cnn"
  - "forecasting"
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
processed_at: "2026-08-08T05:35:23Z"
created_at: "2026-08-08T05:35:23Z"
---

# A Deep Learning Model of Lightning Stroke Density

**Authors**: Randall E. Jones, Joel A. Thornton, Chris J. Wright, R. H. Holzworth
**Date**: 2026-08-05
**Paper ID**: [openalex:2509.10399](https://arxiv.org/abs/2509.10399)

## Summary

This study develops deep learning-based parameterizations of lightning stroke density using meteorological variables from ERA and IMERG datasets via convolutional neural networks with U-Net architectures. Trained on World Wide Lightning Location Network (WWLLN) data from 2010 to 2021 and evaluated on 2022-2023 observations, the models significantly outperform traditional multiplicative products of CAPE and precipitation by reducing domain mean bias by an order of magnitude and yielding higher Fractions Skill Score values across various lightning regimes. Furthermore, the CNN-produced climatology achieves $r^2$ values up to 0.92 over oceans and accurately captures 12-hourly spatial patterns on an event-by-event basis.

## Key Contributions

- Develops deep learning-based parameterizations of lightning stroke density using meteorological variables from ERA and IMERG datasets.
- Employs convolutional neural networks with U-Net architectures trained on WWLLN lightning data from 2010 to 2021 and evaluated on 2022-2023 observations.
- Reduces average domain mean bias by an order of magnitude and achieves significantly higher Fractions Skill Score values compared to traditional CAPE and precipitation multiplicative products.
- Achieves $r^2$ values as high as 0.92 for lightning stroke density climatology over oceans.

## Archivist Review

No concepts, open questions, or datasets met the strict novelty and reusability standards of the vault. The paper applies standard convolutional neural network (U-Net) architectures to meteorological datasets for lightning parameterization, which represents an application of existing machine learning methods rather than a novel, standalone algorithmic framework or foundational research concept.

## Links

- [Abstract](https://arxiv.org/abs/2509.10399)
- [PDF](https://arxiv.org/pdf/2509.10399)

