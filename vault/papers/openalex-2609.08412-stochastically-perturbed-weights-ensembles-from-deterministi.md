---
# CSL-compatible fields
title: "Stochastically Perturbed Weights: Ensembles from Deterministic Machine-Learning Weather Models"
author:
  - literal: "Simon Adamov"
  - literal: "Oliver Fuhrer"
  - literal: "Reto Knutti"
  - literal: "Sebastian Schemm"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.08412"

# Custom fields
paper_id: "2609.08412"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "forecasting"
  - "robustness"
  - "uncertainty-estimation"
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
processed_at: "2026-09-10T09:18:00Z"
created_at: "2026-09-10T09:18:00Z"
---

# Stochastically Perturbed Weights: Ensembles from Deterministic Machine-Learning Weather Models

**Authors**: Simon Adamov, Oliver Fuhrer, Reto Knutti, Sebastian Schemm
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.08412](https://arxiv.org/abs/2609.08412)

## Summary

This paper introduces stochastically perturbed weights (SPW), a post-hoc inference-time method that injects noise into raw weight tensors of deterministic machine-learning weather models to generate forecast ensembles without retraining. Evaluated across four backbones (Aurora, GraphCast, SFNO, and AIFS), SPW achieves competitive continuous ranked probability skill scores compared to trained-probabilistic models at zero marginal training cost. However, the optimal noise injection sites are strictly architecture-specific, and the primary failure mode involves domain-mean overdispersion caused by whole-field offsets.

## Key Contributions

- Introduced stochastically perturbed weights (SPW) as a post-hoc method to extract ensemble uncertainty from deterministic machine-learning weather models without retraining.
- Demonstrated SPW across four deterministic backbones (Aurora, GraphCast, SFNO, AIFS), achieving CRPSS within 0.04 to 0.13 of trained-probabilistic baselines at zero marginal training cost.
- Identified that the productive tensor injection site is architecture-specific and diagnosed domain-mean overdispersion as the primary failure mode, showing that scale restriction or initial condition perturbation mitigates it.

## Limitations

The optimal injection site for weight noise is architecture-specific, requiring tuning rather than acting as a plug-and-play recipe.

## Open Questions & Future Work

- [[principled-injection-site-selection-ml-weather-ensembles]]

## Archivist Review

Applied rigorous filtration to keep the knowledge vault highly selective. The open question regarding principled injection site selection was approved because it targets a fundamental limitation in post-hoc model perturbation methods for weather forecasting. No concepts met the stringent bar for standalone notes.

### Approved Open Questions
- Principled Injection Site Selection: Eliminating the costly trial-and-error search phase across architectures is crucial for making post-hoc weight perturbation a truly portable, plug-and-play recipe for any arbitrary deterministic weather model.

### Rejected Candidates
- [concept] Stochastically Perturbed Weights (SPW) (`stochastically-perturbed-weights`) - not_novel: Perturbing weights at inference time is a variation of weight perturbation / stochastic weight averaging noise techniques rather than a sufficiently distinct architectural or algorithmic novelty for a permanent note.

## Links

- [Abstract](https://arxiv.org/abs/2609.08412)
- [PDF](https://arxiv.org/pdf/2609.08412)

