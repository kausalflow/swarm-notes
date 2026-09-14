---
# CSL-compatible fields
title: "Potential Periodic Signals in Blazars: Significance, Forecasting, and Deep Learning"
author:
  - literal: "M. A. Hashad"
  - literal: "A. Hammad"
  - literal: "Amr A. EL-Zant"
issued:
  date-parts:
    - [2026, 9, 11]
url: "https://arxiv.org/abs/2602.19214"

# Custom fields
paper_id: "2602.19214"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "seasonality"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-14T10:11:14Z"
created_at: "2026-09-14T10:11:14Z"
---

# Potential Periodic Signals in Blazars: Significance, Forecasting, and Deep Learning

**Authors**: M. A. Hashad, A. Hammad, Amr A. EL-Zant
**Date**: 2026-09-11
**Paper ID**: [openalex:2602.19214](https://arxiv.org/abs/2602.19214)

## Summary

This paper investigates quasiperiodic oscillations (QPOs) in blazars using Fermi-LAT gamma-ray light curves, employing STL decomposition for detrending to reveal underlying transient periodic signals. The authors find that most blazars exhibit transient QPO behavior rather than strict long-term periodicity, except for PG 1553+113. Finally, they apply transformer-based deep learning and statistical methods to forecast future light curve behavior and anticipate QPO evolution over a four-year horizon.

## Key Contributions

- Analyzed five blazars with previously reported high-significance year-long quasiperiodic oscillations (QPOs) and an additional nascent QPO source using Fermi-LAT data up to 2025.
- Demonstrated that detrending via Seasonal and Trend decomposition using Loess (STL) generally increases the strength of detected QPO signals while revealing transience on timescales under 4000 days in most sources.
- Applied transformer-based deep learning models alongside traditional statistical methods to forecast blazar light curves four years into the future, successfully predicting unexpected behaviors and future QPO signal strengths.

## Limitations

Limited to a small sample of five established blazars and one nascent source, with transience making long-term periodicity difficult to maintain except in PG 1553+113.

## Open Questions & Future Work

- [[blazar-qpo-transience-persistence]]

## Archivist Review

Applied strict selectivity criteria, approving only the open question regarding blazar QPO persistence and transience, while rejecting domain-specific astrophysical datasets and routine methods.

### Approved Open Questions
- Persistence and Transience of Blazar QPOs: Resolving the transience versus persistence of blazar QPOs is critical for validating supermassive binary black hole candidates and understanding relativistic jet emission physics.

### Rejected Candidates
- [open_question] Persistence and Transience of Blazar QPOs (`blazar-qpo-transience-persistence`) - paper_local: Already in vault or domain-specific astrophysics rather than general machine learning time series methodology.

## Links

- [Abstract](https://arxiv.org/abs/2602.19214)
- [PDF](https://arxiv.org/pdf/2602.19214)

