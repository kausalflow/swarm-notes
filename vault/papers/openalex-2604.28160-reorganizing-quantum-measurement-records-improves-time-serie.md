---
# CSL-compatible fields
title: "Reorganizing Quantum Measurement Records Improves Time-Series Prediction"
author:
  - literal: "Markus Baumann"
  - literal: "Maximilian Zorn"
  - literal: "Thomas Gabor"
  - literal: "Claudia Linnhoff-Popien, Jonas Stein"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.28160"

# Custom fields
paper_id: "2604.28160"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "quantum-reservoir-computing"
  - "evaluation"
architectures:
  - "rwkv"
datasets:
  []
concept_slugs:
  - "split-ensemble-training"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:14:08Z"
created_at: "2026-05-03T07:14:08Z"
---

# Reorganizing Quantum Measurement Records Improves Time-Series Prediction

**Authors**: Markus Baumann, Maximilian Zorn, Thomas Gabor, Claudia Linnhoff-Popien, Jonas Stein
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.28160](https://arxiv.org/abs/2604.28160)

## Summary

Near-term quantum computing often relies on repeated circuit executions that produce noisy measurement records, typically averaged into a single feature vector per time step. This approach limits training data availability, potentially degrading the performance of quantum reservoir computing readouts. The authors introduce split-ensemble training, which redistributes measurement shots into multiple partially-denoised feature vectors per target. This method significantly improves prediction accuracy across various time-series forecasting tasks, particularly in experimental hardware settings where training data efficiency is critical.

## Key Contributions

- Introduces split-ensemble training, a method to augment training data density in quantum reservoir computing by partitioning measurement shots into multiple partially-denoised feature vectors.
- Demonstrates that the proposed method improves forecasting accuracy on both simulated and real quantum hardware by addressing data starvation issues in standard averaging approaches.
- Provides a hardware-agnostic algorithmic lever that enhances prediction performance for near-term quantum devices without additional measurement budget costs.

## Open Questions & Future Work

- [[generalizing-split-ensemble-qrc]]

## Key Concepts

- [[split-ensemble-training]]: A data-reorganization technique for quantum machine learning that increases training set density by splitting repeated measurement shots into multiple partially-denoised feature vectors.

## Archivist Review

I approved the split-ensemble training concept as it offers a novel, hardware-agnostic algorithmic solution to data scarcity in quantum machine learning, satisfying the reusability and impact criteria. The associated open question was approved for its focus on the fundamental trade-offs and architectural scalability of this data-partitioning approach. I applied strict selectivity, confirming no other candidates reached the necessary threshold of broad, recurring utility.

### Approved Concepts
- Split-Ensemble Training: This technique addresses data starvation in near-term quantum learning by partitioning measurement outcomes to expand training set size without increasing the hardware budget.

### Approved Open Questions
- Generalizing Split-Ensemble Training Boundaries: Understanding these boundaries is necessary to evolve the technique from a specialized improvement for linear QRC readouts into a robust, general-purpose tool for quantum-classical interface optimization.

## Links

- [Abstract](https://arxiv.org/abs/2604.28160)
- [PDF](https://arxiv.org/pdf/2604.28160)

