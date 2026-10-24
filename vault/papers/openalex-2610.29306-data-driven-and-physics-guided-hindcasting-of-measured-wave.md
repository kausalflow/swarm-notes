---
# CSL-compatible fields
title: "Data-driven and physics-guided hindcasting of measured wave spectra"
author:
  - literal: "Sander Rikka"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29306"

# Custom fields
paper_id: "2610.29306"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:12:54Z"
created_at: "2026-10-24T09:12:54Z"
---

# Data-driven and physics-guided hindcasting of measured wave spectra

**Authors**: Sander Rikka
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29306](https://arxiv.org/abs/2610.29306)

## Summary

This paper evaluates short-range hindcasts of measured wave spectra in the Baltic Sea using a recurrent model initialized with hourly buoy spectra and local physical forcing. The study compares various data-driven supervision targets (variance, peak frequency, and peak amplitude) alongside physics-guided constraints such as local relaxation and wind-sea bounds. Results indicate that targeted supervision combined with selective physical relaxation yields modest improvements in spectral and wave-height accuracy.

## Key Contributions

- Evaluates short-range hindcasts of measured wave spectra using a recurrent model initialized by buoy spectra and driven by local wind, fetch, and depth across Baltic Sea stations.
- Compares data-driven supervision strategies, finding variance and peak-frequency supervision yields the lowest spectral error while peak-amplitude supervision minimizes wave-height error.
- Demonstrates that local physical guidance via a relaxation constraint reduces height RMSE by 5.01% and extends accuracy through hours 13-24 to reduce primary spectral RMSE by 2.31%.

## Limitations

Wave-height scores concern the retained frequency band, and operational forecasting and transfer to independent stations remain to be evaluated.

## Open Questions & Future Work

- [[operational-forecasting-and-station-transfer]]

## Archivist Review

Applied strict selectivity criteria. No concepts met the threshold for standalone vault value since the paper's methods (local physical relaxation and spectral supervision targets) are domain-specific or paper-local implementations rather than broadly reusable ML concepts. One open question regarding operational forecasting and transferability was approved as it captures a genuine translational bottleneck in physical time-series forecasting.

### Approved Open Questions
- Operational Forecasting and Station Transfer: Determines whether local data-driven and physics-guided wave spectrum models can successfully transition from retrospective hindcasting to operational forecasting environments.

### Rejected Candidates
- [open_question] Operational Forecasting and Station Transfer (`operational-forecasting-and-station-transfer`) - other: The question was approved.

## Links

- [Abstract](https://arxiv.org/abs/2610.29306)
- [PDF](https://arxiv.org/pdf/2610.29306)

