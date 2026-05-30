---
# CSL-compatible fields
title: "Skillful high-resolution weather forecasting independent of physical models"
author:
  - literal: "Pengcheng Zhao"
  - literal: "Siqi Xiang"
  - literal: "Weixin Jin"
  - literal: "Zekun Ni"
  - literal: "Jiang Bian"
  - literal: "Zuliang Fang"
  - literal: "Hongyu Sun"
  - literal: "Bin Zhang"
  - literal: "Richard E. Turner"
  - literal: "Jonathan Weyn"
  - literal: "Haiyu Dong"
  - literal: "Kit Thambiratnam"
  - literal: "Qi Zhang"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28153"

# Custom fields
paper_id: "2605.28153"
paper_source: "openalex"
domain: "nlp"
tags:
  - "forecasting"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "obscast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:35:38Z"
created_at: "2026-05-30T07:35:38Z"
---

# Skillful high-resolution weather forecasting independent of physical models

**Authors**: Pengcheng Zhao, Siqi Xiang, Weixin Jin, Zekun Ni, Jiang Bian, Zuliang Fang, Hongyu Sun, Bin Zhang, Richard E. Turner, Jonathan Weyn, Haiyu Dong, Kit Thambiratnam, Qi Zhang
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28153](https://arxiv.org/abs/2605.28153)

## Summary

ObsCast is a regional weather forecasting system that generates both analysis and predictions directly from local observations, bypassing the traditional reliance on NWP-generated reanalysis data. By eliminating this dependency, the model avoids inheriting NWP-specific biases and resolution constraints, offering a more flexible approach to regional forecasting. Empirical results over the contiguous United States and Europe show that ObsCast achieves state-of-the-art performance in short-term near-surface forecasting and provides skillful precipitation predictions.

## Key Contributions

- Introduces ObsCast, an end-to-end regional weather forecasting system that eliminates reliance on NWP-derived data for both training and inference.
- Outperforms traditional operational NWP for near-surface variables through 18 hours over the contiguous United States and Europe.
- Demonstrates a scalable and cost-effective approach for building regional forecasting services using raw local observations.

## Open Questions & Future Work

- [[explicit-3d-atmospheric-modeling]]

## Key Concepts

- [[obscast]]: A regional weather forecasting system that performs end-to-end analysis and prediction directly from observational data without relying on numerical weather prediction (NWP) reanalyses.

## Archivist Review

ObsCast is approved as a key methodological shift in moving weather forecasting away from reanalysis-dependent supervision. The open question regarding 3D atmospheric modeling is also approved as it captures a critical structural limitation for observation-native forecasting systems. Other candidates were not submitted.

### Approved Concepts
- ObsCast: It is the central contribution of the paper, representing a new paradigm for NWP-free weather forecasting.

### Approved Open Questions
- Explicit 3D Atmospheric Modeling: Explicitly modeling 3D atmospheric dynamics is essential for improving forecast skill beyond the immediate near-surface layer and for achieving performance that competes with full-physics 3D NWP models.

## Links

- [Abstract](https://arxiv.org/abs/2605.28153)
- [PDF](https://arxiv.org/pdf/2605.28153)

