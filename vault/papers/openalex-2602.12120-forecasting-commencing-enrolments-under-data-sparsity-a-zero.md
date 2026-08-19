---
# CSL-compatible fields
title: "Forecasting commencing enrolments under data sparsity: a zero-shot time series foundation models framework for higher education planning"
author:
  - literal: "Jittarin Jetwiriyanon"
  - literal: "Teo Sušnjak"
  - literal: "Surangika Ranathunga"
  - literal: "Guilherme Weigert Cassales"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2602.12120"

# Custom fields
paper_id: "2602.12120"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "leakage-safe-covariate-protocol"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-19T05:19:25Z"
created_at: "2026-08-19T05:19:25Z"
---

# Forecasting commencing enrolments under data sparsity: a zero-shot time series foundation models framework for higher education planning

**Authors**: Jittarin Jetwiriyanon, Teo Sušnjak, Surangika Ranathunga, Guilherme Weigert Cassales
**Date**: 2026-08-17
**Paper ID**: [openalex:2602.12120](https://arxiv.org/abs/2602.12120)

## Summary

This paper investigates the application of zero-shot Time Series Foundation Models (TSFMs) to annual higher education enrolment forecasting under severe data sparsity and structural shifts. The authors benchmark multiple TSFMs using an expanding-window backtest and introduce a leakage-safe covariate protocol that integrates Google Trends and the Institutional Operating Conditions Index (IOCI) without look-ahead bias. Results show that covariate-conditioned TSFMs provide competitive, auditable decision support for institutional planning without requiring bespoke training.

## Key Contributions

- Evaluated zero-shot Time Series Foundation Models (TSFMs) against classical operational baselines for annual higher education enrolment forecasting under data sparsity.
- Introduced a leakage-safe covariate protocol combining feature-engineered Google Trends with the Institutional Operating Conditions Index (IOCI) to capture environmental shifts without look-ahead bias.
- Demonstrated through expanding-window backtesting that covariate-conditioned TSFMs are competitive with classical methods and improve accuracy without requiring bespoke institutional training.

## Limitations

Operational benefits depend heavily on cohort characteristics and specific covariate design.

## Open Questions & Future Work

- [[broader-institutional-validation-transferability]]

## Key Concepts

- [[leakage-safe-covariate-protocol]]: A protocol for integrating external covariates like Google Trends and institutional regime measures into zero-shot forecasting without look-ahead bias.

## Archivist Review

Approved the leakage-safe covariate protocol as a distinct, reusable methodology for integrating external indicators into zero-shot forecasting without look-ahead bias, and retained the corresponding open question on institutional transferability. All candidates adhere to high selectivity and novelty standards.

### Approved Concepts
- Leakage-Safe Covariate Protocol: It introduces a rigorous, auditable mechanism for conditioning time series models on external macro and narrative indicators without look-ahead bias.

### Approved Open Questions
- Broader Institutional Validation and Transferability: Crucial for establishing external validity and generalizability of zero-shot time series foundation models and covariate-conditioning protocols in higher education planning.

## Links

- [Abstract](https://arxiv.org/abs/2602.12120)
- [PDF](https://arxiv.org/pdf/2602.12120)

