---
# CSL-compatible fields
title: "Hierarchical forecasting: The role of information"
author:
  - literal: "Minh Khoa Nguyen"
  - literal: "Farshid Vahid"
  - literal: "Shanika L. Wickramasuriya"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29611"

# Custom fields
paper_id: "2605.29611"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "forecast-reconciliation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "information-combination-icomb"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:08:38Z"
created_at: "2026-05-31T08:08:38Z"
---

# Hierarchical forecasting: The role of information

**Authors**: Minh Khoa Nguyen, Farshid Vahid, Shanika L. Wickramasuriya
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29611](https://arxiv.org/abs/2605.29611)

## Summary

This paper addresses the long-standing ambiguity in hierarchical forecasting: whether performance gains arise from satisfying aggregation constraints or from combining disparate information sets. By demonstrating that coherent forecasts can still be improved by better information integration, the authors introduce the Information Combination (IComb) method. IComb utilizes penalized regression to effectively fuse the information content carried by base forecasts during the reconciliation process, achieving significant accuracy improvements over traditional methods.

## Key Contributions

- Formalizes the distinction between information aggregation and constraint satisfaction in hierarchical forecast reconciliation.
- Introduces IComb, a regression-based reconciliation method that optimizes the integration of diverse information sets across hierarchy levels.
- Demonstrates superior performance over traditional forecast reconciliation approaches on established literature benchmarks.

## Open Questions & Future Work

- [[hierarchical-forecasting-information-sets]]

## Key Concepts

- [[information-combination-icomb]]: A regression-based forecast reconciliation method that explicitly integrates information content from diverse base forecast sources to enhance coherent forecasting accuracy.

## Archivist Review

The paper provides a significant advancement in hierarchical forecasting by disentangling the effects of aggregation constraints from information integration. IComb is approved as a central, reusable methodology for this domain. The open question regarding diverse information sets in hierarchical reconciliation is approved as it addresses a fundamental, unresolved bottleneck in the field.

### Approved Concepts
- Information Combination (IComb): It disentangles the benefits of information aggregation from hierarchical constraint satisfaction, providing a new perspective on forecast reconciliation.

### Approved Open Questions
- Role of diverse information sets: The authors explicitly state that because current evidence is derived from base forecasts using univariate information, it is difficult to identify whether improvements in reconciled forecasts are due to the imposition of constraints or the combination of information. They propose IComb as a step toward addressing this, but leave the deeper exploration of multi-source information integration as a primary future research direction.

## Links

- [Abstract](https://arxiv.org/abs/2605.29611)
- [PDF](https://arxiv.org/pdf/2605.29611)

