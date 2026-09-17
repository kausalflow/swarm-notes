---
# CSL-compatible fields
title: "Short-term forecasting of wildfire spread: A network epidemiology approach"
author:
  - literal: "Indrila Ganguly"
  - literal: "Muhammad Ali"
  - literal: "Swarnali Sanyal"
  - literal: "Viney Aneja"
  - literal: "Srijan Sengupta"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.14951"

# Custom fields
paper_id: "2609.14951"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:44:09Z"
created_at: "2026-09-17T09:44:09Z"
---

# Short-term forecasting of wildfire spread: A network epidemiology approach

**Authors**: Indrila Ganguly, Muhammad Ali, Swarnali Sanyal, Viney Aneja, Srijan Sengupta
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.14951](https://arxiv.org/abs/2609.14951)

## Summary

This paper proposes a statistical framework integrating cellular automata and network epidemiology for short-term wildfire spread forecasting across spatial lattices. The model classifies grid cells as available, burning, or consumed, using covariate-linked transition rates for spread, ignition, and cessation. Evaluated on simulated data, the 2018 California wildfires, the 2019-2020 Australian wildfires, and the 2017 Haypress fire, the approach achieves strong short-term discrimination while highlighting challenges at longer horizons and during rapid expansion.

## Key Contributions

- Developed a statistical framework combining cellular automata with network epidemiology to model wildfire evolution across spatial lattices with state transitions driven by meteorological and environmental covariates.
- Implemented a likelihood-based estimation procedure yielding transition-specific covariate effects and probabilistic cell-state forecasts.
- Demonstrated strong short-term discrimination in simulation studies, the 2018 California wildfires, the 2019-2020 Australian wildfires, and comparative analysis on the 2017 Haypress fire.

## Limitations

Reduced forecasting accuracy observed at longer forecast horizons and during abrupt fire expansion events.

## Archivist Review

Applied strict selectivity principles, rejecting the domain-specific open question as paper-local wildfire modeling rather than a general ML or time-series methodology question. No concepts or datasets met the threshold for standalone inclusion.

### Rejected Candidates
- [open_question] SIRS Extensions for Wildfire Reignition (`sirs-wildfire-reignition-models-fuel-availability`) - paper_local: This open question is domain-specific to wildfire modeling rather than representing a general methodological bottleneck in machine learning or time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2609.14951)
- [PDF](https://arxiv.org/pdf/2609.14951)

