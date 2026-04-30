---
# CSL-compatible fields
title: "DECOFFEE: Decentralized Reinforcement Learning for Time-critical Workload Offloading and Energy Efficiency across the Computing Continuum"
author:
  - literal: "Anastasios Giannopoulos"
  - literal: "Sotirios Spantideas"
  - literal: "Panagiotis Trakadas"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.24507"

# Custom fields
paper_id: "2604.24507"
paper_source: "openalex"
domain: "reinforcement-learning,nlp"
tags:
  - "reinforcement-learning,multi-agent,lstm,llm,edge-computing"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "decoffee"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:25:47Z"
created_at: "2026-04-30T07:25:47Z"
---

# DECOFFEE: Decentralized Reinforcement Learning for Time-critical Workload Offloading and Energy Efficiency across the Computing Continuum

**Authors**: Anastasios Giannopoulos, Sotirios Spantideas, Panagiotis Trakadas
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.24507](https://arxiv.org/abs/2604.24507)

## Summary

DECOFFEE is a decentralized multi-agent reinforcement learning framework designed to optimize workload offloading across the edge-cloud computing continuum. By utilizing a Double Dueling Deep Q-Network augmented with LSTM-based forecasting, the framework enables autonomous edge agents to make dynamic placement decisions that respect time-critical constraints. The approach effectively balances system delay, energy efficiency, and task success rates in stochastic, large-scale distributed environments.

## Key Contributions

- Introduces DECOFFEE, a decentralized multi-agent reinforcement learning framework that optimizes the trade-off between latency, energy consumption, and workload drop rate.
- Formulates the edge-cloud workload placement problem as parallel Markov Decision Processes using a Double Dueling DQN architecture integrated with LSTM for predictive load awareness.
- Demonstrates through extensive simulations that DECOFFEE significantly reduces system overhead and drop rates compared to traditional heuristic and rule-based placement policies.

## Open Questions & Future Work

- [[federated-collaborative-learning-edge-cloud]]
- [[heterogeneous-application-qos-offloading]]

## Key Concepts

- [[decoffee]]: A decentralized reinforcement learning framework for joint optimization of delay, energy, and workload drop rates in edge-cloud computing.

## Archivist Review

I have approved the core framework concept and two open research questions that identify critical bottlenecks in the scalability and heterogeneity of edge-cloud workload management. The rejection criteria focused on maintaining a high bar for conceptual novelty and ensuring that open questions address fundamental research gaps rather than simple performance improvement tasks. No datasets met the criteria for inclusion as they were not explicitly named or critical to the paper's claims in a way that suggests high reuse value.

### Approved Concepts
- DECOFFEE: The framework is the primary contribution and novelty of the paper, providing a structured approach to multi-agent offloading.

### Approved Open Questions
- Collaborative learning for edge-cloud: Addressing the balance between decentralized autonomy and collaborative intelligence is critical for the scalability and robustness of large-scale edge computing systems.
- Supporting heterogeneous application QoS: Standardizing performance metrics across diverse IoT services is a major bottleneck in deploying unified workload management strategies.

## Links

- [Abstract](https://arxiv.org/abs/2604.24507)
- [PDF](https://arxiv.org/pdf/2604.24507)

