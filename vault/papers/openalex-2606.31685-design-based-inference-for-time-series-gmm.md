---
# CSL-compatible fields
title: "Design-Based Inference for Time-Series GMM"
author:
  - literal: "Thomas Glinnan"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.31685"

# Custom fields
paper_id: "2606.31685"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
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
processed_at: "2026-07-03T07:54:41Z"
created_at: "2026-07-03T07:54:41Z"
---

# Design-Based Inference for Time-Series GMM

**Authors**: Thomas Glinnan
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.31685](https://arxiv.org/abs/2606.31685)

## Summary

This paper reformulates time-series GMM inference by conditioning on a realized historical episode rather than assuming data are i.i.d. draws from a population. The author shows that standard HAC-based inference is inherently conservative due to the inclusion of mean-moment path variance. By incorporating macro covariates for projection adjustment, the framework allows for more accurate finite-history estimands and provides a diagnostic for identifying predictable variation in moment paths.

## Key Contributions

- Establishes a design-based inference framework for time-series GMM that treats historical shock realizations as the primary source of uncertainty.
- Demonstrates that conventional HAC estimators are conservative in finite-history settings, converging to a sum of design variance and mean-moment path variance (ΩR+Ωμ).
- Introduces projection adjustment via predetermined covariates to tighten conservative covariance bounds and diagnose economically significant predictable variation in moment paths.

## Open Questions & Future Work

- [[unidentified-mean-moment-path-variance]]

## Archivist Review

The paper provides a formal, design-based rethinking of GMM inference which is distinct from standard population-based approaches. I have approved the open question regarding the identification of the mean-moment path variance as it addresses a fundamental technical limitation in time-series inference. I rejected the original candidate title to better reflect the mathematical terminology used in the paper.

### Approved Open Questions
- Unidentified Mean-Moment Path Variance: This component represents the fundamental difference between design-based and conventional time-series standard errors; without identification, the degree of conservativeness in GMM inference remains fundamentally opaque.

### Rejected Candidates
- [open_question] Identification of Mean-Path Variance (`unidentified-mean-path-variance-gmm`) - other: Renamed for better precision and clarity as 'Unidentified Mean-Moment Path Variance'.

## Links

- [Abstract](https://arxiv.org/abs/2606.31685)
- [PDF](https://arxiv.org/pdf/2606.31685)

