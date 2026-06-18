---
# CSL-compatible fields
title: "Minimising magnetic activity effects in PLATO observations: insights from the Sun-as-a-star"
author:
  - literal: "J. Bétrisey"
  - literal: "Anne-Marie Broomhall"
  - literal: "Sylvain N. Breton"
  - literal: "E. Panetier"
  - literal: "R Garcia"
  - literal: "Henry Davenport"
  - literal: "Oleg Kochukhov"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16450"

# Custom fields
paper_id: "2606.16450"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "benchmark"
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
processed_at: "2026-06-18T09:08:06Z"
created_at: "2026-06-18T09:08:06Z"
---

# Minimising magnetic activity effects in PLATO observations: insights from the Sun-as-a-star

**Authors**: J. Bétrisey, Anne-Marie Broomhall, Sylvain N. Breton, E. Panetier, R Garcia, Henry Davenport, Oleg Kochukhov
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16450](https://arxiv.org/abs/2606.16450)

## Summary

This study investigates the impact of magnetic activity on seismic age estimates of solar-type stars by analyzing long-baseline time series from BiSON and GOLF. The researchers demonstrate that magnetic activity suppression is non-monotonic, with four-year observing windows proving significantly more effective than shorter intervals due to improved temporal averaging and frequency determination. These findings provide critical guidance for the PLATO mission, suggesting that a continuous four-year observation strategy is preferable to split-field deployments for minimizing systematic biases in solar-analogue seismic modeling.

## Key Contributions

- Quantified magnetic activity-induced systematic bias in seismic inferences for solar-type stars using long-baseline Sun-as-a-star observations.
- Demonstrated that the suppression of magnetic activity effects is non-monotonic with respect to the observing window duration, with 1460-day windows providing superior bias reduction over shorter intervals.
- Established that continuous four-year PLATO observations are significantly more effective at mitigating magnetic activity biases than split 2+2-year strategies for solar analogues.

## Open Questions & Future Work

- [[mitigating-magnetic-activity-non-solar-regimes]]

## Archivist Review

The paper provides empirical analysis of magnetic activity bias in solar seismic time series, which is domain-specific to asteroseismology. I approved the open question regarding non-solar regimes as it represents a broader scientific research bottleneck relevant to the mission-critical objectives of PLATO. I rejected the concept of non-monotonic window suppression because it is a specific empirical observation within this domain rather than a general-purpose ML mechanism or inductive bias.

### Approved Open Questions
- Mitigating magnetic activity in non-solar regimes: Understanding and mitigating magnetic activity is critical for achieving the high-precision stellar parameters required by the PLATO mission and other future high-precision asteroseismology surveys.

### Rejected Candidates
- [concept] Non-monotonic observing window suppression (`non-monotonic-observing-window-suppression`) - paper_local: The observed effect is a specific empirical finding for solar time series rather than a broadly reusable forecasting mechanism or inductive bias.
- [dataset] BiSON network dataset (`bison-network-data`) - not_reusable: This is a domain-specific scientific observation dataset rather than a reusable machine learning benchmark dataset.
- [dataset] GOLF instrument dataset (`golf-instrument-data`) - not_reusable: This is a domain-specific scientific observation dataset rather than a reusable machine learning benchmark dataset.

## Links

- [Abstract](https://arxiv.org/abs/2606.16450)
- [PDF](https://arxiv.org/pdf/2606.16450)

