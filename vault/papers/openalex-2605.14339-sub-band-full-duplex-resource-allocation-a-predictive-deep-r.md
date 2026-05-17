---
# CSL-compatible fields
title: "Sub-Band Full Duplex Resource Allocation: A Predictive Deep Reinforcement Learning Approach"
author:
  - literal: "Abhiram D"
  - literal: "Aiswarya Rajan"
  - literal: "Arin Shemeem"
  - literal: "Vipindev Adat Vasudevan"
  - literal: "Abdulla P"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14339"

# Custom fields
paper_id: "2605.14339"
paper_source: "openalex"
domain: "nlp"
tags:
  - "reinforcement-learning"
  - "language-model"
  - "lstm"
  - "forecasting"
architectures:
  - "recurrent-neural-network"
datasets:
  []
concept_slugs:
  - "sbfd-resource-allocation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:31:51Z"
created_at: "2026-05-17T07:31:51Z"
---

# Sub-Band Full Duplex Resource Allocation: A Predictive Deep Reinforcement Learning Approach

**Authors**: Abhiram D, Aiswarya Rajan, Arin Shemeem, Vipindev Adat Vasudevan, Abdulla P
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14339](https://arxiv.org/abs/2605.14339)

## Summary

This paper proposes a predictive deep reinforcement learning framework to optimize sub-band allocation in Sub-Band Full Duplex (SBFD) communication systems. By combining a Bi-LSTM model for traffic forecasting with a Double Deep Q-Network (DDQN) for adaptive scheduling, the system dynamically adjusts uplink and downlink ratios based on bursty traffic demands. Experimental results confirm that this proactive approach enhances spectrum utilization and prevents inefficient configurations, offering a promising solution for autonomous resource management in 6G networks.

## Key Contributions

- Introduces a hybrid Bi-LSTM and DDQN framework for predictive sub-band allocation in SBFD systems.
- Demonstrates effective proactive scheduling by integrating predicted traffic patterns with real-time queue states.
- Achieves superior spectrum utilization and reduced queue buildup compared to traditional static configurations in simulated dynamic traffic environments.

## Open Questions & Future Work

- [[scaling-sbfd-multi-cell-real-traffic]]

## Key Concepts

- [[sbfd-resource-allocation]]: A framework integrating traffic forecasting with deep reinforcement learning to optimize uplink/downlink sub-band split ratios in full-duplex communication systems.

## Archivist Review

The paper proposes an application of well-known architectures (Bi-LSTM + DDQN) to a specific domain (SBFD resource allocation). I have approved the overarching mechanism as a concept for its relevance to 6G resource management, and the open question regarding multi-cell/real-world scaling as it addresses a significant research bottleneck for these systems. Other candidates were rejected to maintain the required scarcity and focus on distinct, reusable research contributions.

### Approved Concepts
- Sub-Band Full Duplex Resource Allocation: Represents the specific application of deep reinforcement learning to balance UL/DL performance in SBFD systems, a critical task for 6G resource management.

### Approved Open Questions
- Multi-Cell Real-Traffic SBFD Scaling: Real-world deployment requires generalization across heterogeneous cells and interference patterns, which single-cell synthetic simulations fail to fully capture. Evaluating multi-agent systems is critical to managing inter-cell interference in dense network deployments.

## Links

- [Abstract](https://arxiv.org/abs/2605.14339)
- [PDF](https://arxiv.org/pdf/2605.14339)

