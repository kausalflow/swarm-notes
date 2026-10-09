---
# CSL-compatible fields
title: "ERP Event Logs: A Canonical Form for KPI Time-Series Extraction and Characterization"
author:
  - literal: "Sherri Hadian"
  - literal: "Adrian Rebmann"
  - literal: "Atacan Korkmaz"
  - literal: "Gregor Berg"
  - literal: "Ulf Brackmann"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.09903"

# Custom fields
paper_id: "2610.09903"
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
processed_at: "2026-10-09T11:34:03Z"
created_at: "2026-10-09T11:34:03Z"
---

# ERP Event Logs: A Canonical Form for KPI Time-Series Extraction and Characterization

**Authors**: Sherri Hadian, Adrian Rebmann, Atacan Korkmaz, Gregor Berg, Ulf Brackmann
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.09903](https://arxiv.org/abs/2610.09903)

## Summary

The paper proposes using a canonical event log representation (case, activity, timestamp) extracted from enterprise resource planning (ERP) systems to unify the extraction of key performance indicator (KPI) time series across heterogeneous relational schemas. By defining three process-derived KPI families (volumes, durations, and rates) under a shared activity ontology across hundreds of SAP S/4HANA customers, the authors enable uniform cross-tenant and cross-industry analysis. Evaluating these KPI series using both classical statistical baselines (ARIMA, ETS) and time-series foundation models (Chronos), they uncover a consistent predictability hierarchy ranging from volumes to durations and rates.

## Key Contributions

- Demonstrated that an event log canonical form (case, activity, timestamp) collapses enterprise resource planning (ERP) relational heterogeneity into a single flat structure for uniform KPI extraction.
- Defined three families of process-derived KPIs (volumes, durations, and rates) and extracted them uniformly across hundreds of SAP S/4HANA customers for order-to-cash and procure-to-pay processes.
- Characterized KPI time-series forecastability across a highly heterogeneous customer base, showing a recurring ordering of predictability from volumes through durations to rates.
- Evaluated time-series foundation models (Chronos) against classical baselines (ARIMA, ETS), finding that pretrained foundation models are competitive on rate and duration series while classical models excel on volumes.

## Archivist Review

Reviewed the paper proposing canonical event log representations for ERP KPI extraction. No concepts met the high reusability threshold for standalone vault notes, and the single open question was a paper-local future work suggestion regarding supply chain joins.

### Rejected Candidates
- [open_question] Item-Level Supply Chain Dynamics (`item-level-supply-chain-dynamics`) - low_impact: Future work suggestion addressing micro-level supply chain joins rather than an overarching methodological or theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.09903)
- [PDF](https://arxiv.org/pdf/2610.09903)

