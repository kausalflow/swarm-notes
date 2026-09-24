---
# CSL-compatible fields
title: "MGRD: Compact morphology-gated residual diffusion for variance-aware cross-domain neurite forecasting"
author:
  - literal: "Tsung Yeh Hsieh"
  - literal: "Cosmin Anitescu"
  - literal: "Chunghwan Kim"
  - literal: "Victoria A. Webster‐Wood"
  - literal: "Yongjie Jessica Zhang"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.23990"

# Custom fields
paper_id: "2609.23990"
paper_source: "openalex"
domain: "biology"
tags:
  - "diffusion-model"
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "morphology-gated-residual-diffusion"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:39:02Z"
created_at: "2026-09-24T09:39:02Z"
---

# MGRD: Compact morphology-gated residual diffusion for variance-aware cross-domain neurite forecasting

**Authors**: Tsung Yeh Hsieh, Cosmin Anitescu, Chunghwan Kim, Victoria A. Webster‐Wood, Yongjie Jessica Zhang
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.23990](https://arxiv.org/abs/2609.23990)

## Summary

The paper introduces Morphology-Gated Residual Diffusion (MGRD), a compact stochastic surrogate designed for variance-aware cross-domain neurite-morphology forecasting. By conditioning on morphology features derived from latest observations, MGRD efficiently predicts future morphology frames while modeling uncertainty. Experiments on phase-field simulations, human iPSC-derived neuron microscopy, and cross-domain mouse cortical-neurosphere data demonstrate superior accuracy, parameter efficiency, and zero-shot generalization compared to existing deterministic baselines like gSTA. Additionally, repeated sampling provides a natural variance score for case prioritization, substantially reducing forecasting error on reliable instances.

## Key Contributions

- Introduces Morphology-Gated Residual Diffusion (MGRD), a compact stochastic surrogate for neurite-morphology forecasting that jointly predicts twenty future frames from ten observed frames.
- Achieves a 9.7% reduction in trajectory-wise mean MAE on controlled phase-field trajectories while using 4.46x fewer parameters than matched controls.
- Improves all four reported metrics over gSTA on human iPSC-derived neuron microscopy, including a 39.6% reduction in MAE and a 45.3% increase in skeleton F1.
- Demonstrates zero-shot cross-domain generalization to mouse cortical-neurosphere microscopy across varying sampling intervals and forecast horizons beyond 13 hours.
- Enables case-level variance scoring via repeated sampling to prioritize low-variance forecasting cases, reducing mean MAE by 17.6% on iPSC microscopy.

## Limitations

Future work could explore extending MGRD to broader biological morphology forecasting tasks and further optimizing DDIM sampling speed.

## Open Questions & Future Work

- [[variance-score-calibration]]

## Key Concepts

- [[morphology-gated-residual-diffusion]]: A compact stochastic surrogate for variance-aware cross-domain neurite forecasting that combines morphology gating with residual diffusion.

## Archivist Review

Approved the central methodological concept of Morphology-Gated Residual Diffusion and its corresponding open question regarding forecast variance score calibration. No standalone named datasets were appropriate for vault entry as the datasets mentioned are general domains.

### Approved Concepts
- Morphology-Gated Residual Diffusion: Central methodological novelty of the paper, introducing a compact stochastic surrogate for variance-aware cross-domain neurite forecasting.

### Approved Open Questions
- Calibrating Forecast Variance Scores: Crucial for establishing confidence intervals and reliability metrics in high-stakes biological forecasting tasks.

## Links

- [Abstract](https://arxiv.org/abs/2609.23990)
- [PDF](https://arxiv.org/pdf/2609.23990)

