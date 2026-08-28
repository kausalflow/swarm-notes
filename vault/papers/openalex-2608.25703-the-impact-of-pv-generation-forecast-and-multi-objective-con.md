---
# CSL-compatible fields
title: "The Impact of PV Generation Forecast and Multi-Objective Control Policy on Optimal Operation of Grid Connected PV-BESS Microgrid"
author:
  - literal: "Berhane Darsene Dimd"
  - literal: "Steve Völler"
  - literal: "Ole‐Morten Midtgård"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25703"

# Custom fields
paper_id: "2608.25703"
paper_source: "openalex"
domain: "time-series"
tags:
  - "lstm"
  - "time-series"
  - "forecasting"
  - "reinforcement-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T17:00:09Z"
created_at: "2026-08-28T17:00:09Z"
---

# The Impact of PV Generation Forecast and Multi-Objective Control Policy on Optimal Operation of Grid Connected PV-BESS Microgrid

**Authors**: Berhane Darsene Dimd, Steve Völler, Ole‐Morten Midtgård
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25703](https://arxiv.org/abs/2608.25703)

## Summary

This paper investigates the impact of photovoltaic (PV) generation forecasts and multi-objective control policies on the optimal operation of grid-connected PV-BESS microgrids. By integrating an LSTM-based PV forecasting model with a multi-objective scheduling framework, the authors demonstrate that improved forecast accuracy substantially increases PV self-consumption, decreases grid injection, and reduces operating costs while exposing trade-offs involving battery throughput and aging. Three forecasting scenarios—perfect forecast, persistence model, and LSTM forecast—are evaluated to quantify operational performance.

## Key Contributions

- Proposes an LSTM-based PV power forecasting model integrated with a multi-objective scheduling framework for grid-connected PV-BESS microgrids.
- Quantifies the impact of PV forecast accuracy on key operational metrics, showing that an LSTM-based forecast reduces RMSE by 6% over a persistence model, increases PV self-consumption from 78.1% to 84.5%, and reduces grid injections by 82%.
- Highlights operational trade-offs, demonstrating that improved performance and higher self-consumption increase battery throughput, which can contribute to accelerated battery aging.

## Limitations

Future work will focus on incorporating probabilistic forecasting to quantify uncertainties, integrating load prediction, and developing smart control strategies for PV-side grid-support functionalities.

## Archivist Review

Applied rigorous scarcity and novelty standards. The single candidate open question was rejected because it proposes standard future work directions (probabilistic forecasting and grid support) rather than a novel, specific methodological bottleneck.

### Rejected Candidates
- [open_question] Probabilistic Forecasting and Grid Support (`probabilistic-forecasting-and-grid-support-microgrids`) - low_impact: Future work proposal is too broad and standard for microgrid optimization and forecasting literature.

## Links

- [Abstract](https://arxiv.org/abs/2608.25703)
- [PDF](https://arxiv.org/pdf/2608.25703)

