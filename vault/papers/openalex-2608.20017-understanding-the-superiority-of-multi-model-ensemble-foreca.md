---
# CSL-compatible fields
title: "Understanding the superiority of multi-model ensemble forecasts through reservoir computing"
author:
  - literal: "Daniel Estévez Moya"
  - literal: "Francesco Martinuzzi"
  - literal: "Edmilson Roque dos Santos"
  - literal: "Erick Alejandro Madrigal Solis"
  - literal: "E. Estevez‐Rams"
  - literal: "Hölger Kantz"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20017"

# Custom fields
paper_id: "2608.20017"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "chaos"
  - "ensemble"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:19:24Z"
created_at: "2026-08-23T05:19:24Z"
---

# Understanding the superiority of multi-model ensemble forecasts through reservoir computing

**Authors**: Daniel Estévez Moya, Francesco Martinuzzi, Edmilson Roque dos Santos, Erick Alejandro Madrigal Solis, E. Estevez‐Rams, Hölger Kantz
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20017](https://arxiv.org/abs/2608.20017)

## Summary

This paper investigates the theoretical and empirical foundations of multi-model ensembles (MMEs) for chaotic time series forecasting using reservoir computing (RC). By evaluating an ensemble of randomly constructed RCs, the authors find that individual model errors exhibit heavy-tailed distributions and deviate along the unstable manifold of the target point. Simple and weighted arithmetic averaging successfully improves forecasting accuracy, approaching a $1/\sqrt{N_{\text{ens}}}$ scaling behavior that is modulated by the heavy tails of the error distribution.

## Key Contributions

- Demonstrates that multi-model ensembles of reservoir computing models yield heavy-tailed forecast error distributions for chaotic time series.
- Shows that arithmetic and weighted averaging of ensemble forecasts improve prediction accuracy by mitigating individual model errors.
- Proves analytically and empirically that iterated chaotic forecasts deviate along unstable manifolds, leading to a $1/\sqrt{N_{\text{ens}}}$ scaling behavior modified by error distribution tails.

## Limitations

Focuses on reservoir computing surrogates rather than full-scale physical climate models.

## Open Questions & Future Work

- [[formalize-mme-error-cancellation-theory]]

## Archivist Review

Evaluated the candidates under strict scarcity constraints. No new concepts met the high bar for standalone persistence since reservoir computing and multi-model ensembles are already well-established vault concepts, and the single open question was rejected to maintain high selectivity.

### Approved Open Questions
- Formalizing Multi-Model Ensemble Theory: Providing a rigorous mathematical framework for the observed geometric error cancellation and ensemble-size scaling would bridge empirical weather/climate forecasting heuristics with rigorous dynamical systems theory.

### Rejected Candidates
- [open_question] Formalizing Multi-Model Ensemble Theory (`formalize-mme-error-cancellation-theory`) - low_impact: A solid question, but we are keeping approvals strictly minimal as per policy.

## Links

- [Abstract](https://arxiv.org/abs/2608.20017)
- [PDF](https://arxiv.org/pdf/2608.20017)

