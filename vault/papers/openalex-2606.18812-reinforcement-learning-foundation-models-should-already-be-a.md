---
# CSL-compatible fields
title: "Reinforcement Learning Foundation Models Should Already Be A Thing"
author:
  - literal: "Abdelrahman Zighem"
  - literal: "Jill-Jênn Vie"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18812"

# Custom fields
paper_id: "2606.18812"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "reinforcement-learning"
  - "transformer"
  - "foundation-model"
  - "in-context-learning"
  - "synthetic-data"
architectures:
  - "transformer"
datasets:
  []
concept_slugs:
  - "reinforcement-learning-foundation-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:18:39Z"
created_at: "2026-06-20T08:18:39Z"
---

# Reinforcement Learning Foundation Models Should Already Be A Thing

**Authors**: Abdelrahman Zighem, Jill-Jênn Vie
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18812](https://arxiv.org/abs/2606.18812)

## Summary

This paper proposes the development of reinforcement learning foundation models by utilizing large-scale synthetic MDP sampling as an alternative to internet-scale data collection. The authors establish that MDPs can be represented by fixed-size sufficient statistics, allowing attention-based architectures to perform in-context policy optimization. As a proof of concept, they train a transformer-based model on synthetic data that achieves strong performance on held-out benchmarks in both online and offline RL settings without additional fine-tuning.

## Key Contributions

- Introduces the concept of training reinforcement learning models as foundation models by pretraining on synthetic Markov Decision Processes (MDPs).
- Demonstrates that MDPs can be compressed into fixed-size sufficient statistics, enabling the use of attention-based architectures to learn policies in-context.
- Achieves competitive performance on held-out tabular RL benchmarks without task-specific tuning, significantly outperforming traditional tabular Q-learning and UCB-VI in episode efficiency.

## Open Questions & Future Work

- [[feature-based-state-representation-in-rl]]
- [[continuous-state-action-spaces-in-rl]]

## Key Concepts

- [[reinforcement-learning-foundation-model]]: An in-context learning model trained on synthetic MDPs that maps sufficient statistics to optimal policies via attention.

## Archivist Review

The proposal of reinforcement learning foundation models through synthetic MDP pretraining is a novel shift in the field. I approved the core concept and two fundamental research bottlenecks regarding scaling beyond discrete tabular environments. The open question slugs were updated slightly for specificity.

### Approved Concepts
- Reinforcement Learning Foundation Model: Proposes a new paradigm for building foundation models for reinforcement learning by leveraging synthetic Markov Decision Processes and fixed-size sufficient statistics.

### Approved Open Questions
- Feature-based State Representations in RL: This is a fundamental bottleneck for scaling foundation models to environments where state-space size and complexity prevent simple enumeration or rely on geometric relationships.
- Continuous State Action Spaces in RL: Continuous control is necessary for applying these models to real-world tasks such as robotics, making this an essential unresolved problem for general-purpose RL foundation models.

## Links

- [Abstract](https://arxiv.org/abs/2606.18812)
- [PDF](https://arxiv.org/pdf/2606.18812)

