---
# CSL-compatible fields
title: "RopeDreamer: A Kinematic Recurrent State Space Model for Dynamics of Flexible Deformable Linear Objects"
author:
  - literal: "Tim Missal"
  - literal: "Lucas Domingues"
  - literal: "Berk Guler"
  - literal: "Simon Manschitz"
  - literal: "Jan Peters"
  - literal: "Paula Dornhofer Paro Costa"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.28161"

# Custom fields
paper_id: "2604.28161"
paper_source: "openalex"
domain: "robotics"
tags:
  - "ssm"
  - "robotics"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quaternionic-kinematic-chain-representation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:15:01Z"
created_at: "2026-05-03T07:15:01Z"
---

# RopeDreamer: A Kinematic Recurrent State Space Model for Dynamics of Flexible Deformable Linear Objects

**Authors**: Tim Missal, Lucas Domingues, Berk Guler, Simon Manschitz, Jan Peters, Paula Dornhofer Paro Costa
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.28161](https://arxiv.org/abs/2604.28161)

## Summary

RopeDreamer addresses the challenge of modeling flexible Deformable Linear Objects (DLOs) by using a latent dynamics framework based on a Recurrent State Space Model. By representing DLOs as Quaternionic Kinematic Chains, the model preserves physical constraints like link-length consistency, avoiding non-physical deformations. A dual-decoder architecture further improves latent space utility, leading to superior performance in long-horizon forecasting and topological integrity during complex contact-rich manipulation.

## Key Contributions

- Proposed a latent dynamics framework combining a Recurrent State Space Model with a Quaternionic Kinematic Chain representation to model DLO dynamics.
- Introduced a dual-decoder architecture that separates state reconstruction from future-state prediction to enforce physical consistency in the latent space.
- Achieved a 40.52% reduction in open-loop prediction error and 31.17% reduction in inference time over 50-step horizons on simulated pick-and-place trajectories compared to existing baselines.

## Open Questions & Future Work

- [[hierarchical-latent-architectures-dlo]]
- [[online-system-id-dlo-dynamics]]

## Key Concepts

- [[quaternionic-kinematic-chain-representation]]: A representation of deformable objects as a sequence of relative quaternion rotations to maintain topological integrity and link-length consistency.

## Archivist Review

The paper presents a specific kinematic representation for DLO dynamics which acts as a powerful temporal/physical inductive bias for forecasting. The approved concepts and open questions address fundamental architectural and adaptability challenges in latent dynamics models for robotics, meeting the criteria for novelty, reusability, and long-term research relevance.

### Approved Concepts
- Quaternionic Kinematic Chain Representation: Provides an inductive bias that enforces physical constraints on flexible objects, preventing non-physical stretching in dynamics forecasting.

### Approved Open Questions
- Hierarchical Latent DLO Dynamics: This is a significant architectural challenge in world models for robotics, as reducing reconstruction error is vital for precision, while hierarchical modeling could resolve the conflict between fine-grained state representation and long-horizon dynamical forecasting.
- Adaptive DLO Dynamics Prediction: Adaptive dynamics models are essential for the practical deployment of robotic systems in uncontrolled, real-world settings where physical parameters cannot be perfectly estimated beforehand.

## Links

- [Abstract](https://arxiv.org/abs/2604.28161)
- [PDF](https://arxiv.org/pdf/2604.28161)

