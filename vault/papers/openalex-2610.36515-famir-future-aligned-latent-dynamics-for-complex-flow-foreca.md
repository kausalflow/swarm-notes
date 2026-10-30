---
# CSL-compatible fields
title: "FAMIR: Future-aligned latent dynamics for complex-flow forecasting"
author:
  - literal: "Yuxuan Chen"
  - literal: "Yan Wang"
  - literal: "Haotian Cheng"
  - literal: "Hongna Zhang"
  - literal: "Wenhua Zhang"
  - literal: "Yuke Li"
  - literal: "Xiaobin Li"
  - literal: "Fengchen Li"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36515"

# Custom fields
paper_id: "2610.36515"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:05:09Z"
created_at: "2026-10-30T11:05:09Z"
---

# FAMIR: Future-aligned latent dynamics for complex-flow forecasting

**Authors**: Yuxuan Chen, Yan Wang, Haotian Cheng, Hongna Zhang, Wenhua Zhang, Yuke Li, Xiaobin Li, Fengchen Li
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36515](https://arxiv.org/abs/2610.36515)

## Summary

FAMIR is a recursive physical forecasting method that uses a future-conditioned teacher to align posterior and prior motion tensors via Posterior-Prior Motion Alignment (PPMA), mitigating error accumulation in complex-flow predictions. Trained with prediction-fed multistep objectives, the student model outperforms direct latent predictors across viscoelastic channel flow, Rayleigh-Bénard convection, and planetary shallow-water flow.

## Key Contributions

- Proposes Future-Aligned Motion Inference for Recursive Physical Forecasting (FAMIR), which uses realized future states to shape motion tensors guiding recursive updates in complex-flow forecasting.
- Introduces Posterior-Prior Motion Alignment (PPMA) to jointly align a future-conditioned teacher posterior and a history-only student prior.
- Achieves lower complete-prefix normalized root-mean-square error than direct latent predictors on viscoelastic channel flow, Rayleigh-Bénard convection, and planetary shallow-water flow over 10-step and 20-step forecasts.
- Demonstrates superior maintenance of fluctuation profiles and probability densities over 40-step forecasts compared to direct predictors.

## Open Questions & Future Work

- [[generalization-to-unseen-parameters-and-geometries-flow-forecasting]]

## Archivist Review

Applied strict selectivity guidelines. No standalone core forecasting concepts or benchmark datasets met the threshold for vault addition. One open question was evaluated and rejected due to domain specificity and low reuse impact.

### Approved Open Questions
- Unseen Parameters and Geometries Flow Forecasting: Evaluating generalization to unseen physical parameters and geometries is crucial for validating whether recursive latent dynamics surrogates can operate robustly outside training domains.

### Rejected Candidates
- [open_question] Unseen Parameters and Geometries in Flow Forecasting (`generalization-to-unseen-parameters-and-geometries-flow-forecasting`) - low_impact: The open question was too narrow and paper-local to physical fluid flow surrogates to warrant permanent standalone archival.

## Links

- [Abstract](https://arxiv.org/abs/2610.36515)
- [PDF](https://arxiv.org/pdf/2610.36515)

