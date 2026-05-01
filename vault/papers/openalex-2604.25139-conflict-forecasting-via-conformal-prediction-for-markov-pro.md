---
# CSL-compatible fields
title: "Conflict Forecasting via Conformal Prediction for Markov Processes"
author:
  - literal: "Aditya Basarkar"
  - literal: "Emmett B. Kendall"
  - literal: "David Randahl"
  - literal: "Jonathan P. Williams"
  - literal: "Gudmund H. Hermansen"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2604.25139"

# Custom fields
paper_id: "2604.25139"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "conformal-prediction"
  - "uncertainty-quantification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "conformal-prediction-for-markov-processes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:22:27Z"
created_at: "2026-05-01T07:22:27Z"
---

# Conflict Forecasting via Conformal Prediction for Markov Processes

**Authors**: Aditya Basarkar, Emmett B. Kendall, David Randahl, Jonathan P. Williams, Gudmund H. Hermansen
**Date**: 2026-04-28
**Paper ID**: [openalex:2604.25139](https://arxiv.org/abs/2604.25139)

## Summary

This paper addresses the challenge of predicting national conflict status by applying conformal prediction to temporally-dependent Markovian data. Unlike traditional point-prediction, this approach provides valid uncertainty quantification and maintains robustness against model misspecification in high-stakes forecasting. The authors evaluate the framework on real-world conflict dynamics and provide a critical analysis of the limitations imposed by the violation of exchangeability assumptions in Markov processes.

## Key Contributions

- Proposes a conformal prediction framework to generate valid prediction sets for future conflict state-sequences in Markov processes.
- Demonstrates robustness to model misspecification by providing uncertainty quantification that outperforms standard point-prediction strategies in high-stakes conflict forecasting.
- Identifies and discusses limitations of applying conformal prediction to non-exchangeable Markovian data, highlighting challenges with existing theoretical assumptions.

## Open Questions & Future Work

- [[conformal-prediction-under-non-exchangeability]]

## Key Concepts

- [[conformal-prediction-for-markov-processes]]: A framework for generating uncertainty-quantified prediction sets for future states in Markov processes by adapting conformal prediction techniques to handle temporal dependency.

## Archivist Review

I approved the 'Conformal Prediction for Markov Processes' concept and the 'Conformal Prediction under Non-Exchangeability' open question. These capture the core methodological contribution of addressing the breakdown of exchangeability in sequential data. Other candidates were rejected for being domain-specific or failing to capture the underlying algorithmic challenge.

### Approved Concepts
- Conformal Prediction for Markov Processes: The paper addresses the challenge of extending conformal prediction—which typically assumes exchangeability—to non-exchangeable Markovian time-series data.

### Approved Open Questions
- Conformal Prediction under Non-Exchangeability: This is a fundamental bottleneck for deploying robust, distribution-free uncertainty quantification in real-world time-series forecasting.

### Rejected Candidates
- [concept] Conflict Forecasting via Conformal Prediction (`conflict-forecasting-via-conformal-prediction`) - paper_local: This is a specific application domain rather than a reusable forecasting method or mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2604.25139)
- [PDF](https://arxiv.org/pdf/2604.25139)

