---
# CSL-compatible fields
title: "$t_0$: A Time-Series Foundation Model for Forecasting with Context"
author:
  - literal: "Lucas Meyer"
  - literal: "Claudio Sole"
  - literal: "Huikan Xiang"
  - literal: "Nicolas Li"
  - literal: "Lucas Franceschino"
  - literal: "Arnau Quera-Bofarull"
  - literal: "Maarten P. Scholl"
  - literal: "Joachim Fainberg"
  - literal: "Geoffrey Négiar"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24559"

# Custom fields
paper_id: "2609.24559"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "transformer"
  - "attention-mechanism"
  - "pre-training"
  - "zero-shot-learning"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  - "gift-eval"
concept_slugs:
  []
dataset_slugs:
  - "gift-eval"
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:37:30Z"
created_at: "2026-09-24T09:37:30Z"
---

# $t_0$: A Time-Series Foundation Model for Forecasting with Context

**Authors**: Lucas Meyer, Claudio Sole, Huikan Xiang, Nicolas Li, Lucas Franceschino, Arnau Quera-Bofarull, Maarten P. Scholl, Joachim Fainberg, Geoffrey Négiar
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24559](https://arxiv.org/abs/2609.24559)

## Summary

The paper presents t_0, a family of open-weights time-series foundation models (t0-alpha at 102M and t0-beta at 256M parameters) that generate zero-shot multivariate probabilistic forecasts conditioned on target history, past covariates, and known-future covariates. Utilizing transformer layers with alternating temporal and cross-variate attention, the models are pretrained on a mix of public data and synthetic covariate-to-target generator families. Evaluations on GIFT-Eval and fev-bench demonstrate competitive zero-shot accuracy, while detailed analyses reveal substantial performance gains from known-future covariates, robust long-horizon rollouts, and strong handling of extended context windows up to a year.

## Key Contributions

- Introduces t_0, a family of open-weights time-series foundation models (t0-alpha at 102M and t0-beta at 256M parameters) that condition multivariate forecasts on target history, past covariates, and known-future covariates without task-specific retraining.
- Achieves competitive zero-shot forecasting performance, reaching an aggregate CRPS of 0.4941 (t0-alpha) and 0.4738 with a MASE of 0.6865 (t0-beta) on GIFT-Eval, placing within 4.0% of the leading zero-shot TSFM.
- Demonstrates that incorporating known-future covariates raises model skill by 6.3 percentage points across 30 tasks, while effectively handling long rolling horizons, missing data robustness, and extended context windows of nearly a year on electricity-demand benchmarks.

## Archivist Review

Rigorously applied scarcity and redundancy checks. No new concepts or open questions met the strict novelty and reusability standards, and the dataset GIFT-Eval is already present in the vault.

### Rejected Candidates
- [dataset] GIFT-Eval (`gift-eval`) - duplicate_existing: Already exists in vault.

## Datasets

- [[gift-eval]]

## Links

- [Abstract](https://arxiv.org/abs/2609.24559)
- [PDF](https://arxiv.org/pdf/2609.24559)

