---
# CSL-compatible fields
title: "ADORN: Adaptive Drift handling for Open RAN using Reinforcement Learning"
author:
  - literal: "Ashit Subudhi"
  - literal: "Bhargav Chirumamilla"
  - literal: "Shubham Vaishnav"
  - literal: "Mduduzi C. Hlophe"
  - literal: "Praveen Kumar Donta"
  - literal: "Andrea Fumagalli"
  - literal: "Venkateswarlu Gudepu"
  - literal: "Koteswararao Kondepu"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08443"

# Custom fields
paper_id: "2607.08443"
paper_source: "openalex"
domain: "nlp"
tags:
  - "reinforcement-learning"
  - "lstm"
  - "forecasting"
  - "time-series"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adorn-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:25:05Z"
created_at: "2026-07-12T07:25:05Z"
---

# ADORN: Adaptive Drift handling for Open RAN using Reinforcement Learning

**Authors**: Ashit Subudhi, Bhargav Chirumamilla, Shubham Vaishnav, Mduduzi C. Hlophe, Praveen Kumar Donta, Andrea Fumagalli, Venkateswarlu Gudepu, Koteswararao Kondepu
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08443](https://arxiv.org/abs/2607.08443)

## Summary

ADORN is an adaptive drift handling framework for O-RAN that leverages reinforcement learning to optimize the frequency of AI/ML model retraining. By formulating the retraining task as a Markov Decision Process, the agent learns a policy that balances the trade-off between forecasting accuracy and computational cost. Additionally, the framework employs a multi-expert LSTM ensemble to enhance robustness to traffic variations and prevent catastrophic forgetting. Results demonstrate that ADORN significantly reduces retraining overhead compared to static baselines while maintaining performance within strict SLA constraints.

## Key Contributions

- Introduces ADORN, a reinforcement learning-based adaptive retraining framework that formulates model maintenance as a Markov Decision Process.
- Utilizes a multi-expert LSTM ensemble to mitigate catastrophic forgetting during traffic drift, maintaining model performance across diverse O-RAN conditions.
- Demonstrates effective reduction of computational retraining overhead compared to greedy and random baselines while ensuring adherence to Service Level Agreements (SLAs).

## Open Questions & Future Work

- [[drl-for-large-scale-oran-drift-handling]]

## Key Concepts

- [[adorn-framework]]: A reinforcement learning-based adaptive retraining framework that manages AI/ML model drift in network environments by optimizing the trade-off between forecasting accuracy and computational cost.

## Archivist Review

The ADORN framework was approved because it provides a clear, reusable methodology for optimizing the trade-off between model performance and computational cost in non-stationary environments. The associated open question was approved as it targets the fundamental scalability bottleneck of applying reinforcement learning to complex, continuous drift-handling tasks. Subcomponents like the specific LSTM ensemble were rejected as they are standard architectural choices in ensemble learning.

### Approved Concepts
- ADORN Framework: The framework introduces a reinforcement learning-based approach to balancing forecasting accuracy with retraining overhead, addressing a critical bottleneck in resource-constrained environments.

### Approved Open Questions
- Scaling Drift Handling via DRL: Addressing the scalability of drift-handling agents is a fundamental requirement for deploying reliable ML models in real-world telecommunications infrastructure.

### Rejected Candidates
- [concept] Multi-Expert LSTM Ensemble (`multi-expert-lstm-ensemble`) - subcomponent_of_broader_mechanism: This is a routine ensemble technique often treated as an implementation detail unless a novel architectural innovation is proposed.

## Links

- [Abstract](https://arxiv.org/abs/2607.08443)
- [PDF](https://arxiv.org/pdf/2607.08443)

