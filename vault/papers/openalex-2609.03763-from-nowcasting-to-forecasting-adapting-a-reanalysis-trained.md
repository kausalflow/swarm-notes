---
# CSL-compatible fields
title: "From Nowcasting to Forecasting: Adapting a Reanalysis-Trained"
author:
  - literal: "Mikko Partio"
  - literal: "Leila Hieta"
  - literal: "Ossi Laine"
issued:
  date-parts:
    - [2026, 9, 3]
url: "https://arxiv.org/abs/2609.03763"

# Custom fields
paper_id: "2609.03763"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-06T09:01:08Z"
created_at: "2026-09-06T09:01:08Z"
---

# From Nowcasting to Forecasting: Adapting a Reanalysis-Trained

**Authors**: Mikko Partio, Leila Hieta, Ossi Laine
**Date**: 2026-09-03
**Paper ID**: [openalex:2609.03763](https://arxiv.org/abs/2609.03763)

## Summary

This paper presents CloudCast v2, a machine-learning model for 12-hour cloud-cover forecasting that bridges short-range nowcasting and long-range numerical weather prediction. The model is pre-trained on reanalysis data to learn cloud evolution dynamics and adapted to satellite observations using conditional flow matching conditioned on initial cloud states and NWP inputs. Results demonstrate that CloudCast v2 achieves a 10% reduction in mean absolute error over CloudCast v1 across 1-12 hour horizons while improving spatial skill scores at longer lead times.

## Key Contributions

- CloudCast v2 is developed as a 12-hour cloud-cover forecasting model combining reanalysis pre-training with satellite-derived adaptation via conditional flow matching.
- CloudCast v2 reduces mean absolute error by 10% compared to CloudCast v1 across the 1-12 h range.
- The model outperforms CloudCast v1 in fractions skill score after 3-6 hours depending on the cloudiness category, extending satellite-initialized forecasts beyond the standard nowcasting range.

## Open Questions & Future Work

- [[probabilistic-cloud-forecasting-and-transferability]]

## Archivist Review

Approved the open question on probabilistic cloud forecasting and transferability as it addresses core challenges in generative weather emulators and uncertainty quantification. Rejected concepts as they were specific to model versions and paper-local implementations.

### Approved Open Questions
- Probabilistic Cloud Forecasting and Transferability: Crucial for advancing generative and observation-guided weather prediction models toward robust operational uncertainty quantification and multi-region generalization.

### Rejected Candidates
- [concept] CloudCast v2 (`cloudcast-v2`) - paper_local: CloudCast v2 is a specific model architecture and application instance rather than a reusable standalone forecasting concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.03763)
- [PDF](https://arxiv.org/pdf/2609.03763)

