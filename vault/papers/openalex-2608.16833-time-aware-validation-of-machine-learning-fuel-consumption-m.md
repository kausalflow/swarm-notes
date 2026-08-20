---
# CSL-compatible fields
title: "Time-Aware Validation of Machine Learning Fuel Consumption Models: Evidence from 1\,Hz Operational Data, CCGS \textit{Sir Wilfrid Laurier}"
author:
  - literal: "Samarasimha Reddy Chittamuru"
  - literal: "Ayhan Akintürk"
  - literal: "Allison Kennedy"
  - literal: "Joshua Barnes"
  - literal: "Matthew Hamilton"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2608.16833"

# Custom fields
paper_id: "2608.16833"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-20T05:21:16Z"
created_at: "2026-08-20T05:21:16Z"
---

# Time-Aware Validation of Machine Learning Fuel Consumption Models: Evidence from 1\,Hz Operational Data, CCGS \textit{Sir Wilfrid Laurier}

**Authors**: Samarasimha Reddy Chittamuru, Ayhan Akintürk, Allison Kennedy, Joshua Barnes, Matthew Hamilton
**Date**: 2026-08-17
**Paper ID**: [openalex:2608.16833](https://arxiv.org/abs/2608.16833)

## Summary

This paper investigates the impact of validation practices on data-driven ship fuel consumption (SFC) models, demonstrating that random train-test splits cause temporal leakage and overly optimistic performance on high-frequency operational data. Using 3.88 million 1 Hz records from the CCGS Sir Wilfrid Laurier, the study evaluates six regression models and a physics baseline across time-aware schemes including Time Series Cross-Validation (TSCV) and Blocked TSCV (BTSCV). Results emphasize the necessity of chronological hold-out evaluations to accurately reflect real-world deployment conditions in maritime decision support systems.

## Key Contributions

- Demonstrates that random train-test splits in high-frequency ship fuel consumption modeling introduce severe temporal leakage and optimistic evaluation bias.
- Compares six regression models and a physics baseline using Time Series Cross-Validation (TSCV) and Blocked TSCV (BTSCV) on 1 Hz operational data from CCGS Sir Wilfrid Laurier.
- Evaluates models across three time-aware validation schemes and three feature configurations on a common chronological hold-out set of approximately 3.88 million records.

## Limitations

Evaluated on a single vessel (CCGS Sir Wilfrid Laurier) and operational dataset; generalizability to other vessel classes or adverse weather regimes requires further study.

## Archivist Review

Reviewed candidates strictly against vault standards. The paper highlights temporal leakage when using random splits on high-frequency operational data, which is an important empirical finding but doesn't introduce a new standalone algorithmic concept or open vault question that is sufficiently broad.

### Rejected Candidates
- [open_question] Time-Aware Neural and Physics-Informed Fuel Models (`time-aware-neural-physics-fuel-models`) - low_impact: The question primarily proposes applying standard sequence and physics-informed models to a specific application domain (ship fuel consumption) rather than posing a generalizable foundational ML challenge.

## Links

- [Abstract](https://arxiv.org/abs/2608.16833)
- [PDF](https://arxiv.org/pdf/2608.16833)

