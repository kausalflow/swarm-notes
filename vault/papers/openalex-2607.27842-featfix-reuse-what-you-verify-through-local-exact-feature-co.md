---
# CSL-compatible fields
title: "FeatFix: Reuse What You Verify through Local Exact-Feature Correction for Faster Cached Diffusion Inference"
author:
  - literal: "Hanshuai Cui"
  - literal: "Zhiqing Tang"
  - literal: "Zhi Yao"
  - literal: "Qianli Ma"
  - literal: "Fanshuai Meng"
  - literal: "Weijia Jia"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.27842"

# Custom fields
paper_id: "2607.27842"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "model-compression"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:27:40Z"
created_at: "2026-08-02T07:27:40Z"
---

# FeatFix: Reuse What You Verify through Local Exact-Feature Correction for Faster Cached Diffusion Inference

**Authors**: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Qianli Ma, Fanshuai Meng, Weijia Jia
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.27842](https://arxiv.org/abs/2607.27842)

## Summary

FeatFix is a training-free acceleration method for cached diffusion inference that reuses exact intermediate features computed during verification to correct local draft residuals and reduce downstream feature error. By replacing draft block outputs at a sparse set of layer-timestep sites rather than discarding them or performing full-timestep recomputation, FeatFix achieves up to a 6.70x speedup across image and video backbones while preserving generation quality.

## Key Contributions

- Introduces FeatFix, a training-free local exact-feature correction method that reuses verification exact features to reset local draft residuals in cached diffusion inference.
- Replaces complete draft block outputs at a sparse set of layer-timestep sites with exact outputs computed from the same incoming state without full-timestep recomputation.
- Achieves up to a 6.70x acceleration over vanilla diffusion models across four image and video backbones while maintaining competitive output quality.

## Archivist Review

All candidates were rejected because the paper's focus on computer vision diffusion generation acceleration falls outside the specialized time-series forecasting, temporal dynamics, and distribution-shift scope of this knowledge vault.

### Rejected Candidates
- [concept] FeatFix (`featfix`) - low_impact: Paper focuses on computer vision diffusion model acceleration rather than core time-series forecasting, temporal modeling, or structural distribution-shift mechanisms stored in this vault.
- [open_question] Prompt-Adaptive Budget-Aware Correction Policies (`prompt-adaptive-budget-aware-correction-policies`) - low_impact: Open question targets image/video diffusion generation schedules rather than core time-series forecasting, distribution shift, or temporal emulation bottlenecks.

## Links

- [Abstract](https://arxiv.org/abs/2607.27842)
- [PDF](https://arxiv.org/pdf/2607.27842)

