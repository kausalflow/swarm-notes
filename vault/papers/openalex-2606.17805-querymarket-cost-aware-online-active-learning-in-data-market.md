---
# CSL-compatible fields
title: "QueryMarket: Cost-Aware Online Active Learning in Data Markets"
author:
  - literal: "XJ Huang"
  - literal: "Pierre Pinson"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17805"

# Custom fields
paper_id: "2606.17805"
paper_source: "openalex"
domain: "nlp"
tags:
  - "reinforcement-learning"
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "online-variance-based-active-learning-ovbal"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:25:51Z"
created_at: "2026-06-19T09:25:51Z"
---

# QueryMarket: Cost-Aware Online Active Learning in Data Markets

**Authors**: XJ Huang, Pierre Pinson
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17805](https://arxiv.org/abs/2606.17805)

## Summary

QueryMarket is a framework for cost-aware online active learning that optimizes label acquisition in data streams under rolling budget constraints. It introduces the Online Variance-Based Active Learning (OVBAL) algorithm, which computes sample utility using a D-optimality criterion modified with exponential forgetting to handle concept drift. Empirical evaluation on solar power forecasting tasks demonstrates that the proposed method effectively manages heterogeneous label costs and achieves superior performance-to-cost trade-offs compared to traditional approaches.

## Key Contributions

- Introduced QueryMarket, a market-inspired framework for cost-aware online active learning under rolling budget constraints.
- Proposed OVBAL, which employs a D-optimality criterion with exponential forgetting to handle concept drift and heterogeneous label costs.
- Demonstrated that OVBAL outperforms baselines in long-run error-cost trade-offs for solar power generation forecasting under seller-centric pricing schemes.

## Open Questions & Future Work

- [[market-aware-active-learning-robustness]]

## Key Concepts

- [[online-variance-based-active-learning-ovbal]]: A cost-aware online active learning framework that uses D-optimality and exponential forgetting to adapt to nonstationary streams under rolling budget constraints.

## Archivist Review

I have approved the core active learning mechanism (OVBAL) and the associated open question regarding the interaction between market dynamics and learning acquisition. These items are distinct from existing vault entries and provide a conceptual framework for cost-constrained data acquisition in streaming time-series forecasting. No new datasets were approved as none provided novel, reusable benchmarking data compared to existing entries.

### Approved Concepts
- Online Variance-Based Active Learning (OVBAL): Provides a unified framework for balancing label cost, model utility, and budget constraints in nonstationary data streams.

### Approved Open Questions
- Market-aware active learning robustness: The performance of online active learning in market environments is highly sensitive to the interaction between the analyst's utility-based acquisition rule and the pricing scheme imposed by external data sellers, necessitating more generalizable and robust strategies.

## Links

- [Abstract](https://arxiv.org/abs/2606.17805)
- [PDF](https://arxiv.org/pdf/2606.17805)

