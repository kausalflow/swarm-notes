---
# CSL-compatible fields
title: "Federated Learning for Early Prediction of EV Charging Demand"
author:
  - literal: "Vasilis Perifanis"
  - literal: "Foteini Nikolaidou"
  - literal: "Nikolaos Pavlidis"
  - literal: "Panagiotis Thomakos"
  - literal: "Andreas Sendros"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04993"

# Custom fields
paper_id: "2605.04993"
paper_source: "openalex"
domain: "time-series"
tags:
  - "federated-learning"
  - "time-series"
  - "forecasting"
  - "privacy"
  - "dataset"
architectures:
  []
datasets:
  - "adaptive-charging-network-acn-dataset"
concept_slugs:
  []
dataset_slugs:
  - "adaptive-charging-network-acn-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:03:15Z"
created_at: "2026-05-09T07:03:15Z"
---

# Federated Learning for Early Prediction of EV Charging Demand

**Authors**: Vasilis Perifanis, Foteini Nikolaidou, Nikolaos Pavlidis, Panagiotis Thomakos, Andreas Sendros
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04993](https://arxiv.org/abs/2605.04993)

## Summary

This paper addresses the challenge of early prediction for electric vehicle (EV) charging energy demand, allowing network operators to make actionable decisions while sessions are active. By utilizing session metadata and measurements from the initial minutes of charging, the authors evaluate various predictive models on the Adaptive Charging Network (ACN) dataset. The study specifically investigates the effectiveness of federated learning (FL) in training these models across station-level client partitions, showing that FL achieves performance near-centralized levels while ensuring data locality and privacy. This approach provides a scalable and privacy-aware solution for infrastructure planning and grid stability.

## Key Contributions

- Presents a framework for early prediction of EV charging session energy using data only from the plug-in time and the initial charging phase.
- Constructs a session-level feature set from the ACN dataset that integrates user intent, temporal patterns, and initial charging dynamics.
- Demonstrates that federated learning allows training accurate EV demand models across distributed station-level partitions while maintaining data privacy and achieving performance comparable to centralized approaches.

## Open Questions & Future Work

- [[cross-depot-federated-learning-scalability]]

## Archivist Review

The paper applies established federated learning techniques to an EV charging domain. I approved the ACN dataset as it is a specific, actionable resource for charging infrastructure research. I approved the cross-depot scalability open question as it identifies a concrete, domain-specific transition from isolated site forecasting to network-wide scaling. Other candidates were rejected for being generic to the broader federated learning literature rather than novel contributions of this work.

### Approved Open Questions
- Cross-depot FL Scalability: Addressing cross-depot scalability is essential for real-world adoption, as charging networks are geographically distributed rather than localized to a single depot.

### Rejected Candidates
- [open_question] Federated aggregation methods evaluation (`federated-aggregation-methods-ev-charging`) - generic: Evaluating federated aggregation strategies is a generic challenge in the field of federated learning, not specific to EV charging demand.

## Datasets

- [[adaptive-charging-network-acn-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.04993)
- [PDF](https://arxiv.org/pdf/2605.04993)

