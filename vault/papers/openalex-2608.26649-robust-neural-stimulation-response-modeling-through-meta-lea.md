---
# CSL-compatible fields
title: "Robust Neural Stimulation Response Modeling Through Meta-Learning and Pretraining"
author:
  - literal: "Matthew J. Bryan"
  - literal: "Daniel C Muir"
  - literal: "Felix Schwock"
  - literal: "Azadeh Yazdan-Shahmorad"
  - literal: "Rajesh P N Rao"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26649"

# Custom fields
paper_id: "2608.26649"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "meta-learning"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:11:07Z"
created_at: "2026-08-30T10:11:07Z"
---

# Robust Neural Stimulation Response Modeling Through Meta-Learning and Pretraining

**Authors**: Matthew J. Bryan, Daniel C Muir, Felix Schwock, Azadeh Yazdan-Shahmorad, Rajesh P N Rao
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26649](https://arxiv.org/abs/2608.26649)

## Summary

This paper addresses the challenges of forecasting failures and heavy per-session calibration requirements in model-based closed-loop neural stimulation by introducing a cross-session pretraining and meta-learning approach based on model-agnostic meta-learning (MAML). Evaluated on 40 sessions of optogenetic stimulation in non-human primates, the MAML-pretrained Temporal Basis Function Models (TBFMs) drastically reduce catastrophic forecast failures and cut calibration requirements by 50-90%. These findings demonstrate that cross-session structure in neural stimulation responses is sufficiently consistent to support robust pretraining and sample-efficient deployment.

## Key Contributions

- Demonstrated for the first time that cross-session pretraining and model-agnostic meta-learning (MAML) can be applied to neural stimulation response modeling.
- Reduced catastrophic forecasting failures (test R-squared < 0.05) from 16 out of 40 sessions down to 1 session using MAML-pretrained Temporal Basis Function Models (TBFMs) on optogenetic stimulation data.
- Decreased per-session calibration data requirements by 50-90% at matched accuracy, easing clinical constraints for closed-loop neural stimulation.

## Limitations

Evaluated on optogenetic stimulation in the primary sensorimotor cortex of two non-human primates; broader cross-subject and cross-modality scaling remain to be explored.

## Open Questions & Future Work

- [[neural-stimulation-foundation-model-consistency]]

## Archivist Review

Approved the foundational cross-session neural stimulation open question as it highlights a novel and important long-term challenge in closed-loop neuromodulation. No concepts met the high bar for permanent methodological reusability across general time-series forecasting, as temporal basis function models and MAML application to neural data are domain-specific instantiations rather than broadly reusable forecasting primitives.

### Approved Open Questions
- Foundation Model Latent Structure Consistency: Determines the feasibility of scaling meta-learning and pretraining approaches into universal cross-subject and cross-modality foundation models for neural stimulation.

## Links

- [Abstract](https://arxiv.org/abs/2608.26649)
- [PDF](https://arxiv.org/pdf/2608.26649)

