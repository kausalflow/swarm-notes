---
# CSL-compatible fields
title: "Ensemble Complexity in Photovoltaic Forecasting"
author:
  - literal: "Sun Ze"
  - literal: "Zhou Liguo"
  - literal: "Xu Yuqing"
  - literal: "Yu Lei"
  - literal: "Jiang Mingming"
  - literal: "Jiang Mingming"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15049"

# Custom fields
paper_id: "2609.15049"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "gefcom2014"
  - "pvdaq"
concept_slugs:
  []
dataset_slugs:
  - "gefcom2014"
  - "pvdaq"
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:42Z"
created_at: "2026-09-17T09:43:42Z"
---

# Ensemble Complexity in Photovoltaic Forecasting

**Authors**: Sun Ze, Zhou Liguo, Xu Yuqing, Yu Lei, Jiang Mingming, Jiang Mingming
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15049](https://arxiv.org/abs/2609.15049)

## Summary

This paper assesses ensemble complexity and component contributions in photovoltaic forecasting through matched comparisons and ablations of a fixed heterogeneous predictor bank across four public datasets. Using chronological partitions, multiple seeds, and retrospective ERA5 assistance, the authors find that static fusion yields modest improvements over boosting, whereas weather gating provides no consistent incremental benefit. Exploratory member removals and model substitutions further reveal trade-offs between error reduction and computational overhead.

## Key Contributions

- Evaluated ensemble complexity and component contributions in photovoltaic forecasting using matched comparisons and ablations of a fixed heterogeneous predictor bank.
- Demonstrated that static fusion under retrospective ERA5 assistance reduces scaled mean absolute error against matched boosting on PVDAQ, OPSD, and Ausgrid datasets.
- Found that weather gating provides no consistent incremental benefit while exploratory member removals reveal group-level dependence and individual redundancy.

## Limitations

Weather gating offers no consistent incremental benefit, and certain complexity trade-offs (e.g., tree vs. neural replacements) yield error reductions at the expense of slower inference.

## Archivist Review

All candidates were rejected as they pertain narrowly to specific photovoltaic forecasting evaluations and retrospective analyses rather than reusable foundational mechanisms or general open research problems in time series. Two standard datasets already present in the vault are noted via canonical naming if applicable.

### Rejected Candidates
- [open_question] Prospective Validation of Reduced Ensembles (`prospective-ensemble-validation`) - paper_local: Too specific to retrospective photovoltaic forecasting evaluation protocols.

## Datasets

- [[gefcom2014]]
- [[pvdaq]]

## Links

- [Abstract](https://arxiv.org/abs/2609.15049)
- [PDF](https://arxiv.org/pdf/2609.15049)

