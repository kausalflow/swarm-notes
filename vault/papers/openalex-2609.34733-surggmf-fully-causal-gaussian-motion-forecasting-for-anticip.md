---
# CSL-compatible fields
title: "SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering"
author:
  - literal: "Jingqian Sun"
  - literal: "Yichao Tang"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34733"

# Custom fields
paper_id: "2609.34733"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "multimodal"
  - "computer-vision"
  - "robotics"
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
processed_at: "2026-09-30T10:50:50Z"
created_at: "2026-09-30T10:50:50Z"
---

# SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering

**Authors**: Jingqian Sun, Yichao Tang
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34733](https://arxiv.org/abs/2609.34733)

## Summary

SurgGMF is a fully causal Gaussian motion forecasting framework designed for anticipatory surgical scene rendering. Instead of predicting RGB images directly, it forecasts future Gaussian motion states (position, scale, and rotation residuals) from historical Gaussian motion fields. To eliminate target leakage, a full-causal-last rendering protocol renders future states without accessing target-frame Gaussian attributes while maintaining causal appearance propagation. Evaluations on EndoNeRF and StereoMIS video slices demonstrate that learned Gaussian motion forecasting outperforms classical dynamics baselines in render space.

## Key Contributions

- Introduces SurgGMF, a fully causal Gaussian motion forecasting framework that predicts future Gaussian motion states (position, scale, rotation residuals) from historical Gaussian motion fields for anticipatory surgical scene rendering.
- Proposes a full-causal-last rendering protocol to prevent target leakage by rendering future Gaussian states without accessing target-frame Gaussian attributes while preserving causal appearance propagation.
- Evaluates motion forecasting across 12 EndoNeRF and StereoMIS video slices using neural temporal learners and classical dynamics baselines, showing that learned Gaussian motion forecasting outperforms classical hand-crafted state extrapolation in render space.

## Limitations

Latency analysis reveals an accuracy-efficiency trade-off where TKAN achieves higher accuracy while GRU and LSTM provide more favorable latency profiles.

## Archivist Review

Strictly applied the review policy, rejecting paper-local frameworks and standard future-work extensions to maintain a high-quality, reusable knowledge vault.

### Rejected Candidates
- [concept] SurgGMF (`surggmf`) - paper_local: SurgGMF is a paper-specific framework name and application implementation rather than a broadly reusable modeling primitive or foundational time-series technique.
- [open_question] Long-Horizon and Joint Appearance Forecasting (`long-horizon-joint-appearance-forecasting`) - paper_local: The open question primarily outlines standard paper-local extensions regarding longer-horizon prediction and online surgical system deployment.

## Links

- [Abstract](https://arxiv.org/abs/2609.34733)
- [PDF](https://arxiv.org/pdf/2609.34733)

