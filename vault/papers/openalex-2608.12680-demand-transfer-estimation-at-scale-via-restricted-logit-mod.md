---
# CSL-compatible fields
title: "Demand Transfer Estimation at Scale via Restricted Logit Modeling"
author:
  - literal: "Lakshya Garg"
  - literal: "Deep Narayan Mishra"
  - literal: "Swapnil Yadav"
  - literal: "Haoan Wang"
  - literal: "Sujal Alugubelli"
  - literal: "Karthik Kumaran"
  - literal: "Anupriya Sharma"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.12680"

# Custom fields
paper_id: "2608.12680"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "time-series"
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
processed_at: "2026-08-16T05:18:25Z"
created_at: "2026-08-16T05:18:25Z"
---

# Demand Transfer Estimation at Scale via Restricted Logit Modeling

**Authors**: Lakshya Garg, Deep Narayan Mishra, Swapnil Yadav, Haoan Wang, Sujal Alugubelli, Karthik Kumaran, Anupriya Sharma
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.12680](https://arxiv.org/abs/2608.12680)

## Summary

This paper addresses the computational inefficiency of traditional customer choice models for large item assortment optimization by proposing a restricted logit modeling approach to estimate Demand Transfer (DT) coefficients. The method combines independent item demand forecasting with adjustment coefficients that capture substitution behavior when target items are removed from the shelf. Experiments on large-scale historical transaction data demonstrate that the procedure efficiently scales to millions of items while improving demand forecasting accuracy.

## Key Contributions

- Introduces a restricted logit modeling approach to compute Demand Transfer (DT) coefficients for large item universes exceeding 1 million items.
- Combines independent item demand forecasting with adjustment coefficients that account for item availability and substitution behavior.
- Demonstrates through experiments on historical transaction data that the proposed procedure accurately estimates DT coefficients and improves demand forecasting performance.

## Limitations

Relies on certain reasonable assumptions about substitution behavior to accurately estimate underlying DT coefficients.

## Open Questions & Future Work

- [[relaxing-iia-assumption-scalable-choice-models]]
- [[customer-level-substitution-tracking-validation]]

## Archivist Review

The paper presents an application of restricted logit modeling for large-scale demand transfer estimation in retail assortment optimization. No reusable general forecasting mechanisms or dataset benchmarks warrant a permanent vault note, but the open questions regarding IIA relaxation and direct substitution tracking represent important structural bottlenecks in choice modeling and demand forecasting.

### Approved Open Questions
- Relaxing IIA in Scalable Choice Models: Relaxing IIA is critical for capturing realistic substitution patterns in retail assortment optimization without sacrificing the computational tractability required for million-item product universes.
- Direct Customer-Level Substitution Tracking: Direct validation using customer-level tracking addresses a fundamental observability bottleneck in empirical retail analytics and choice modeling.

### Rejected Candidates
- [concept] Restricted Logit Modeling for Demand Transfer (`restricted-logit-modeling-for-demand-transfer`) - not_reusable: This is a specific application of logit modeling to retail demand transfer rather than a widely reusable ML mechanism or forecasting primitive.

## Links

- [Abstract](https://arxiv.org/abs/2608.12680)
- [PDF](https://arxiv.org/pdf/2608.12680)

