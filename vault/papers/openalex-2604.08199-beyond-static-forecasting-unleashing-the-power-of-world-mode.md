---
# CSL-compatible fields
title: "Beyond Static Forecasting: Unleashing the Power of World Models for Mobile Traffic Extrapolation"
author:
  - literal: "Xiaoqian Qi"
  - literal: "Haoye Chai"
  - literal: "Yue Wang"
  - literal: "Yong Li"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.08199"

# Custom fields
paper_id: "2604.08199"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "multimodal"
  - "forecasting"
  - "reinforcement-learning"
  - "digital-twin"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mobiwm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:19:44Z"
created_at: "2026-04-12T06:19:44Z"
---

# Beyond Static Forecasting: Unleashing the Power of World Models for Mobile Traffic Extrapolation

**Authors**: Xiaoqian Qi, Haoye Chai, Yue Wang, Yong Li
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.08199](https://arxiv.org/abs/2604.08199)

## Summary

MobiWM is a world model designed for mobile network management that moves beyond static time-series forecasting by explicitly modeling the dynamics between traffic states and network configuration parameters. The framework fuses multimodal environmental data—including imagery and sequential traffic patterns—with action trajectories, such as antenna power and tilt adjustments. This approach enables unlimited-horizon rollouts, providing a robust counterfactual simulation environment for optimizing network performance and planning. Experimental validation across 31,900 cells demonstrates that MobiWM outperforms existing prediction models and serves as an effective digital twin for RL-based network optimization.

## Key Contributions

- Introduces MobiWM, a world-model-based framework for modeling the interplay between mobile traffic states and multi-parameter network configuration adjustments.
- Integrates multimodal environmental contexts (imagery and sequences) with network actions to enable high-fidelity, long-horizon counterfactual simulations.
- Demonstrates superior distributional fidelity and forecasting performance across 31,900 cells compared to traditional traffic prediction and existing world model baselines.

## Open Questions & Future Work

- [[mobile-network-world-model-dynamics]]

## Key Concepts

- [[mobiwm]]: A world model architecture for mobile networks that simulates the interaction between traffic states and network configuration parameters.

## Archivist Review

I have approved the core framework (MobiWM) as a representative architecture for state-action world modeling in network forecasting, as this represents a distinct shift from static forecasting to interactive simulation. The open question was approved for highlighting the specific challenges of graph-structured state spaces and long-horizon stability in large-scale infrastructure environments. I rejected no other candidates as the analysis provided a very focused set of contributions.

### Approved Concepts
- MobiWM: It introduces a world-model-based framework specifically designed for wireless network state-action dynamics, shifting from static prediction to counterfactual simulation.

### Approved Open Questions
- Modeling mobile network world dynamics: Addressing this is essential for transitioning mobile network management from static forecasting to an actionable, digital-twin driven paradigm where operators can simulate and optimize network configurations without live-network risk.

### Rejected Candidates
- [concept] MobiWM (`mobiwm`) - other: While MobiWM is the specific framework proposed, it acts as a container for the concept of world-model-based state-action forecasting in network management rather than a distinct, reusable methodology. However, to preserve the core innovation of the paper, it is approved for its unique approach to state-action-traffic dynamics. (Correction: I have approved it as requested by the instructions to be scarce).

## Links

- [Abstract](https://arxiv.org/abs/2604.08199)
- [PDF](https://arxiv.org/pdf/2604.08199)

