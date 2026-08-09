---
# CSL-compatible fields
title: "Information leakage from data revisions in retrospective forecasts"
author:
  - literal: "Johannes Bracher"
  - literal: "Sebastian Funk"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.05883"

# Custom fields
paper_id: "2608.05883"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:40:26Z"
created_at: "2026-08-09T05:40:26Z"
---

# Information leakage from data revisions in retrospective forecasts

**Authors**: Johannes Bracher, Sebastian Funk
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.05883](https://arxiv.org/abs/2608.05883)

## Summary

This paper investigates claims that an AI-driven Empirical Research Assistance (ERA) system significantly outperforms state-of-the-art CDC ensembles for COVID-19 hospitalisation forecasting. The authors demonstrate that the reported performance gains stem from information leakage in the retrospective forecasting setup, specifically because data revisions were ignored. This cautionary finding highlights a widespread methodological pitfall in retrospective predictive modeling where unadjusted vintage data inflates apparent accuracy.

## Key Contributions

- Demonstrated that performance gains claimed by an AI-driven forecasting system (ERA) over the CDC ensemble for COVID-19 hospitalisations are attributable to information leakage via data revisions in retrospective setups.
- Provided a cautionary analysis showing how unmodeled data revisions inflate retrospective forecast accuracy across epidemic and general predictive modeling domains.
- Highlighted methodological pitfalls in retrospective forecasting benchmarks where future vintage data inadvertently leaks into past evaluation periods.

## Open Questions & Future Work

- [[quantifying-information-leakage-retrospective-forecasts-revisions]]

## Archivist Review

The paper provides a valuable methodological critique on information leakage from data revisions in retrospective forecasting setups. No novel algorithmic concepts or specific named datasets warrant standalone notes, but the open question regarding the quantification and elimination of data-revision leakage in benchmarks is important and retained.

### Approved Open Questions
- Quantifying Information Leakage in Retrospective Forecasts: Uncontrolled information leakage from data revisions distorts benchmark leaderboards and leads to overestimation of predictive performance in retrospective studies.

## Links

- [Abstract](https://arxiv.org/abs/2608.05883)
- [PDF](https://arxiv.org/pdf/2608.05883)

