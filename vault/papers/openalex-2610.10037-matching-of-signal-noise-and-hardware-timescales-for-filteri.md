---
# CSL-compatible fields
title: "Matching of signal, noise and hardware timescales for filtering and forecasting of correlated noise signals"
author:
  - literal: "Joshua Donald"
  - literal: "A. Gabbitas"
  - literal: "Arthur G. T. Coveney"
  - literal: "Sergey Savel’ev"
  - literal: "Pavel Borisov"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.10037"

# Custom fields
paper_id: "2610.10037"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reservoir"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "reservoir-memory-horizon-and-forecasting-regime-index"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:34:46Z"
created_at: "2026-10-09T11:34:46Z"
---

# Matching of signal, noise and hardware timescales for filtering and forecasting of correlated noise signals

**Authors**: Joshua Donald, A. Gabbitas, Arthur G. T. Coveney, Sergey Savel’ev, Pavel Borisov
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.10037](https://arxiv.org/abs/2610.10037)

## Summary

This paper investigates how matching signal, noise, and hardware timescales determines the filtering versus forecasting behavior of physical reservoir computing systems. Using a nanoporous niobium oxide reservoir alongside synthetic and cryptocurrency volatility data, the authors demonstrate that noise faster than the reservoir memory is averaged out, while slower noise can be forecasted. They introduce the reservoir memory horizon and forecasting regime index to formally distinguish these operating regimes.

## Key Contributions

- Demonstrated that the relationship among noise correlation time, reservoir memory, and forecast horizon governs whether correlated noise is filtered or predicted using a nanoporous niobium oxide reservoir.
- Showed that noise varying faster than the reservoir memory is averaged out, whereas slower-varying noise structures enable algorithmic forecasting.
- Introduced the reservoir memory horizon and forecasting regime index to distinguish between noise filtering and forecasting operating regimes.

## Key Concepts

- [[reservoir-memory-horizon-and-forecasting-regime-index]]: A framework of metrics distinguishing whether physical reservoirs filter or predict correlated noise based on timescale matching.

## Archivist Review

Approved the core methodological concept 'Reservoir Memory Horizon and Forecasting Regime Index' as a reusable framework for characterizing timescale-dependent physical reservoir computing and noise handling. Rejected the dataset as it is an unformatted descriptive label rather than a canonical benchmark dataset.

### Approved Concepts
- Reservoir Memory Horizon and Forecasting Regime Index: Provides a novel mathematical and empirical framework for characterizing whether physical reservoirs filter or predict correlated noise based on timescale matching.

### Rejected Candidates
- [dataset] cryptocurrency-price volatility (`cryptocurrency-price volatility`) - not_reusable: Not a specific benchmark dataset name but a description of data used.

## Links

- [Abstract](https://arxiv.org/abs/2610.10037)
- [PDF](https://arxiv.org/pdf/2610.10037)

