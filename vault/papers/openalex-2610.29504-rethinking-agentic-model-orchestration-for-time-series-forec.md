---
# CSL-compatible fields
title: "Rethinking Agentic Model Orchestration for Time Series Forecasting"
author:
  - literal: "Tong Guan"
  - literal: "Tianxiang Zhan"
  - literal: "Shirui Pan"
  - literal: "Ming Jin"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29504"

# Custom fields
paper_id: "2610.29504"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "agent"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fairamo"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:11:37Z"
created_at: "2026-10-24T09:11:37Z"
---

# Rethinking Agentic Model Orchestration for Time Series Forecasting

**Authors**: Tong Guan, Tianxiang Zhan, Shirui Pan, Ming Jin
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29504](https://arxiv.org/abs/2610.29504)

## Summary

This paper investigates agentic model orchestration (AMO) for time series forecasting, revealing that recent performance gains largely stem from candidate complementarity rather than sophisticated orchestration. The authors introduce FairAMO, a controlled evaluation protocol with frozen candidate forecasts, to isolate true orchestration value on GIFT-Eval. Results demonstrate that AMO gains are bounded within 6% MASE improvement over the best single model, suffer from diminishing returns, and are highly sensitive to redundant candidates and historical window saturation.

## Key Contributions

- Introduces FairAMO, a controlled evaluation protocol with frozen candidate forecasts to disentangle orchestration gains from individual time series foundation model (TSFM) performance.
- Demonstrates that agentic model orchestration (AMO) performance is tightly bounded, reducing MASE by less than 6% relative to the best single TSFM.
- Shows that orchestration gains rely heavily on model complementarity and suffer from diminishing returns or degradation when redundant members are introduced.
- Reveals that the value of historical evidence saturates quickly in AMO, where a few recent windows capture all achievable gains.

## Limitations

Limited to evaluating existing TSFMs via frozen candidate forecasts under specific orchestration protocols.

## Open Questions & Future Work

- [[finer-grained-contextual-agentic-orchestration]]

## Key Concepts

- [[fairamo]]: A controlled evaluation protocol with frozen candidate forecasts designed to disentangle orchestration gains from individual model performance in time series forecasting.

## Archivist Review

Approved the evaluation protocol FairAMO as it provides a valuable, reusable framework for disentangling orchestration gains from candidate performance in time series model selection. Approved the open question addressing finer-grained contextual agentic orchestration. GIFT-Eval was omitted from datasets since it is already present in the vault.

### Approved Concepts
- FairAMO: FairAMO provides a rigorous evaluation protocol to isolate system-level forecasting gains from orchestrator contribution by using frozen candidate forecasts.

### Approved Open Questions
- Finer-Grained Contextual Agentic Orchestration: Developing finer-grained commitment strategies and leveraging richer context is crucial to bridging the gap between current deployable orchestrators and optimal window-level oracles in time series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2610.29504)
- [PDF](https://arxiv.org/pdf/2610.29504)

