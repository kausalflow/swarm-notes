---
# CSL-compatible fields
title: "Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions"
author:
  - literal: "David Moriña"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2608.16537"

# Custom fields
paper_id: "2608.16537"
paper_source: "openalex"
domain: "biology"
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
processed_at: "2026-08-20T05:21:30Z"
created_at: "2026-08-20T05:21:30Z"
---

# Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions

**Authors**: David Moriña
**Date**: 2026-08-17
**Paper ID**: [openalex:2608.16537](https://arxiv.org/abs/2608.16537)

## Summary

Seasonal infectious-disease interventions are often evaluated using designs that align epidemics by calendar week, which can confound shifts in epidemic phase with changes in disease burden. To address this, the paper proposes a Bayesian causal count model that uses season-specific affine transformations to map calendar time to a latent epidemic clock, estimating intervention effects on that clock. By treating alignment as an integrated model component rather than a preprocessing step, uncertainty about epidemic timing is properly propagated into all causal contrasts, which is demonstrated on Catalan surveillance and respiratory syncytial virus data.

## Key Contributions

- Proposes a Bayesian causal count model with season-specific affine transformations mapping calendar time to a latent epidemic clock to evaluate seasonal infectious-disease interventions.
- Propagates epidemic timing uncertainty directly within the model rather than treating alignment as a preprocessing step.
- Evaluates the framework using open Catalan primary-care surveillance and respiratory syncytial virus immunisation data.

## Open Questions & Future Work

- [[asymmetric-epidemic-clock-warps]]

## Archivist Review

Applied strict scarcity and novelty filters. Approved the open question regarding asymmetric epidemic clock warps because it addresses a fundamental limitation in functional curve registration and causal alignment under uncertainty. No standalone concepts met the threshold for permanent vault storage.

### Approved Open Questions
- Asymmetric Epidemic Clock Warps: Handling asymmetric epidemic deformation is critical for capturing realistic non-linear seasonal shifts in infectious disease outbreaks without discarding uncertainty in functional curve registration.

## Links

- [Abstract](https://arxiv.org/abs/2608.16537)
- [PDF](https://arxiv.org/pdf/2608.16537)

