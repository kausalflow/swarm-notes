---
# CSL-compatible fields
title: "TypiCore: A Hybrid Active Query Strategy for Class-Incremental Learning on Time Series"
author:
  - literal: "Gábor Szűcs"
  - literal: "Sámuel Jacsev"
  - literal: "Marcell Németh"
  - literal: "Davide Dalle Pezze"
  - literal: "Gian Antonio Susto"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17632"

# Custom fields
paper_id: "2607.17632"
paper_source: "openalex"
domain: "time-series"
tags:
  - "continual-learning"
  - "active-learning"
  - "time-series"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "typicore"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:26:39Z"
created_at: "2026-07-23T07:26:39Z"
---

# TypiCore: A Hybrid Active Query Strategy for Class-Incremental Learning on Time Series

**Authors**: Gábor Szűcs, Sámuel Jacsev, Marcell Németh, Davide Dalle Pezze, Gian Antonio Susto
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17632](https://arxiv.org/abs/2607.17632)

## Summary

This paper investigates Active Class-Incremental Learning (ACIL) for multivariate time series under constrained annotation budgets. The authors systematically evaluate various query strategies and identify limitations in traditional uncertainty-based and distribution-aware methods. To resolve this, they introduce TypiCore, a hybrid query strategy alternating between typicality-based and diversity-based sample selection. Evaluated on the TSCIL benchmark, TypiCore outperforms existing baselines and matches fully supervised performance using a fraction of the labels.

## Key Contributions

- Investigates Active Class-Incremental Learning (ACIL) for multivariate time series under fixed annotation budgets.
- Proposes TypiCore, a novel hybrid query strategy alternating between typicality-based and diversity-based sample selection to build representative and diverse memory buffers.
- Demonstrates that TypiCore achieves statistically significant improvements over baselines on the TSCIL benchmark while matching or surpassing fully supervised continual learning performance using only a fraction of the labels.

## Open Questions & Future Work

- [[dynamic-budget-allocation-acil]]

## Key Concepts

- [[typicore]]: A hybrid active query strategy combining typicality and diversity for class-incremental learning on time series under annotation budgets.

## Archivist Review

Approved the core hybrid query strategy (TypiCore) as a distinct algorithmic contribution to active class-incremental learning and retained the open question on dynamic budget allocation. Rejected generic problem descriptions and loose future work extensions.

### Approved Concepts
- TypiCore: Introduces a novel hybrid query strategy combining typicality and diversity for active class-incremental learning on time series.

### Approved Open Questions
- Dynamic Budget Allocation in ACIL: Dynamic budget allocation can optimize label efficiency and model adaptation in non-stationary environments where task complexity and distribution shifts vary unpredictably.

### Rejected Candidates
- [concept] Active Class-Incremental Learning (`active-class-incremental-learning`) - not_novel: Standard problem setting rather than a novel reusable technical mechanism or algorithm.
- [open_question] Combined Domain and Class Incremental Learning (`combined-domain-class-incremental-learning`) - weak_evidence: Generic future work direction suggesting extension to combined domain and class incremental learning without a concrete structural bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.17632)
- [PDF](https://arxiv.org/pdf/2607.17632)

