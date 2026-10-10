---
# CSL-compatible fields
title: "Timer-M1: A Multivariate Time Series Foundation Model via Learning Primitives"
author:
  - literal: "Haoran Zhang"
  - literal: "Haixuan Liu"
  - literal: "Xingjian Su"
  - literal: "Yong Liu"
  - literal: "Zhi Chen"
  - literal: "Yuxuan Wang"
  - literal: "Jianmin Wang"
  - literal: "Mingsheng Long"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11734"

# Custom fields
paper_id: "2610.11734"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "foundation-model"
  - "pre-training"
  - "zero-shot-learning"
  - "multivariate"
  - "transformer"
  - "attention-mechanism"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:52:27Z"
created_at: "2026-10-10T10:52:27Z"
---

# Timer-M1: A Multivariate Time Series Foundation Model via Learning Primitives

**Authors**: Haoran Zhang, Haixuan Liu, Xingjian Su, Yong Liu, Zhi Chen, Yuxuan Wang, Jianmin Wang, Mingsheng Long
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11734](https://arxiv.org/abs/2610.11734)

## Summary

Timer-M1 is a multivariate time series foundation model designed for zero-shot forecasting through the learning of elementary temporal and relational primitives. It incorporates a primitive-based data synthesis and pretraining pipeline paired with episodic channel role assignment and gated two-dimensional Transformer blocks. Evaluations across FEV, TIME, and GIFT-Eval demonstrate competitive or superior performance compared to existing time series foundation models.

## Key Contributions

- Introduced Timer-M1, a multivariate time series foundation model that learns via elementary temporal and relational primitives for zero-shot forecasting.
- Developed a primitive-based data synthesis and pretraining pipeline that combines domain-shared temporal primitives with relational assembly.
- Designed an episodic training strategy assigning distinct channel roles (target variates, past-only covariates, known-future covariates) to leverage exogenous information.
- Achieved first rank on FEV and TIME benchmarks and second on GIFT-Eval among recent time series foundation models.

## Archivist Review

Strictly evaluated candidates against the vault policy and skill context. No concepts or open questions were sufficiently novel, standalone, or distinct from existing vault entries to warrant permanent storage.

### Rejected Candidates
- [open_question] Expanding Real-Data Coverage and Primitives (`expanding-real-data-coverage-and-primitive-compositions`) - weak_evidence: Too generic and resembles standard future work on expanding data coverage and datasets.
- [open_question] Input-Dependent Cross-Variate Interaction and Long-Context Modeling (`input-dependent-cross-variate-interaction-and-long-context-modeling`) - low_impact: Too broad as an open question regarding architecture-level improvements and long-context scaling.

## Links

- [Abstract](https://arxiv.org/abs/2610.11734)
- [PDF](https://arxiv.org/pdf/2610.11734)

