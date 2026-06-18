---
# CSL-compatible fields
title: "Can Optimal Dispatch Models Recreate Reality? A Retrospective Analysis of Europe's 2022 Energy Crisis Using PyPSA-Eur"
author:
  - literal: "Lukas Karkossa"
  - literal: "Marco Saretta"
  - literal: "Frederik Erhard Gullach"
  - literal: "Marta Victoria"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16486"

# Custom fields
paper_id: "2606.16486"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-18T09:08:11Z"
created_at: "2026-06-18T09:08:11Z"
---

# Can Optimal Dispatch Models Recreate Reality? A Retrospective Analysis of Europe's 2022 Energy Crisis Using PyPSA-Eur

**Authors**: Lukas Karkossa, Marco Saretta, Frederik Erhard Gullach, Marta Victoria
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16486](https://arxiv.org/abs/2606.16486)

## Summary

This paper evaluates the efficacy of optimal dispatch modeling in replicating historical electricity market prices during the volatile 2020-2024 period in Europe. By hindcasting nodal marginal prices using PyPSA-Eur, the authors demonstrate that integrating high-resolution fuel and CO2 price data with a limited two-week rolling-horizon significantly improves accuracy over static or perfect-foresight baselines. The results highlight substantial modeling challenges during the 2022 energy crisis, particularly regarding discrepancies in natural gas and coal usage, attributable to unmodeled real-world policy constraints and generator outages.

## Key Contributions

- Conducts a retrospective analysis of European electricity market outcomes from 2020 to 2024 using the PyPSA-Eur optimal dispatch model.
- Evaluates the impact of dynamic fuel/CO2 price modeling and limited foresight (rolling-horizon) versus perfect foresight on electricity price hindcasting accuracy.
- Achieves an average SMAPE of 20.76% for daily load-weighted European electricity prices by integrating high-resolution fuel price series with two-week rolling-horizon optimization.

## Open Questions & Future Work

- [[optimizing-storage-under-rolling-horizons]]

## Archivist Review

The paper provides a detailed empirical validation of optimal dispatch modeling under different foresight and price assumptions, revealing significant gaps during crises. I approved the open question regarding storage management because it identifies a structural limitation inherent to rolling-horizon optimization that is common across energy system models. I rejected the concept of 'rolling-horizon optimization' as it is a well-established standard optimization technique rather than a novel contribution.

### Approved Open Questions
- Optimizing storage under rolling horizons: The cyclic constraint is a fundamental limitation in rolling-horizon dispatch models used to simulate real-world system behavior under uncertainty, making it a key bottleneck for long-term dispatch modeling accuracy.

## Links

- [Abstract](https://arxiv.org/abs/2606.16486)
- [PDF](https://arxiv.org/pdf/2606.16486)

