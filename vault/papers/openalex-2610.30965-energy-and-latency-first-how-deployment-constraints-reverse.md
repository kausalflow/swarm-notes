---
# CSL-compatible fields
title: "Energy and Latency First: How Deployment Constraints Reverse Time-Series Model Selection"
author:
  - literal: "Shruti Bothe"
  - literal: "Illyyne Saffar"
  - literal: "Ayush K. Varshney"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.30965"

# Custom fields
paper_id: "2610.30965"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
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
processed_at: "2026-10-25T09:29:27Z"
created_at: "2026-10-25T09:29:27Z"
---

# Energy and Latency First: How Deployment Constraints Reverse Time-Series Model Selection

**Authors**: Shruti Bothe, Illyyne Saffar, Ayush K. Varshney
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.30965](https://arxiv.org/abs/2610.30965)

## Summary

This paper investigates how real-world deployment constraints—specifically hard timing deadlines and cumulative energy budgets on user equipment—reverse standard time-series model rankings that rely solely on accuracy. Using handover prediction in cellular networks as a case study, the authors evaluate eight architectures and find that gradient-boosted trees outperform neural models like 1D-CNNs, which consume over three times more energy and may fail strict tail deadlines. They outline three general conditions governing when deployment constraints alter model selection outcomes.

## Key Contributions

- Demonstrates that accuracy-only time-series benchmarking can select models that fail strict deployment constraints (such as hard timing deadlines and device energy budgets).
- Evaluates eight time-series architectures under a handover prediction protocol in cellular networks incorporating tail deadline feasibility and cumulative inference energy.
- Finds that gradient-boosted trees on handcrafted temporal features outperform neural network alternatives like 1D-CNNs in both accuracy and energy efficiency under duty-cycled deployment.
- Provides three generalizable conditions where deployment constraints reverse standard model selection rankings.

## Open Questions & Future Work

- [[deployment-constrained-time-series-benchmarking-frameworks]]

## Archivist Review

Approved the open question on deployment-constrained time-series benchmarking as it captures a fundamental methodological critique of accuracy-only model selection in edge environments. No concepts or datasets met the strict novelty and reusability standards.

### Approved Open Questions
- Deployment-Constrained Time-Series Benchmarking: Crucial for bridging the gap between theoretical machine learning research and resource-constrained edge/IoT deployments, where accuracy-only benchmarks frequently select models that fail to meet runtime or energy requirements.

## Links

- [Abstract](https://arxiv.org/abs/2610.30965)
- [PDF](https://arxiv.org/pdf/2610.30965)

