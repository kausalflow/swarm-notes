---
# CSL-compatible fields
title: "Effective attractive and repulsive interactions behind lift synchronization"
author:
  - literal: "Mitsusuke Tarama"
  - literal: "Sakurako Tanida"
issued:
  date-parts:
    - [2026, 4, 1]
url: "https://arxiv.org/abs/2604.00425"

# Custom fields
paper_id: "2604.00425"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "agent"
  - "autonomous-agent"
architectures:
  []
datasets:
  []
concept_slugs:
  - "effective-interaction-decomposition-multi-agent"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-04T05:50:22Z"
created_at: "2026-04-04T05:50:22Z"
---

# Effective attractive and repulsive interactions behind lift synchronization

**Authors**: Mitsusuke Tarama, Sakurako Tanida
**Date**: 2026-04-01
**Paper ID**: [openalex:2604.00425](https://arxiv.org/abs/2604.00425)

## Summary

This paper investigates the underlying mechanisms of lift synchronization by analyzing time-series data from a rule-based discrete model of stochastic passenger demand. The authors discover that synchronization is driven by a delicate balance of effective attractive and repulsive interactions between lifts. By manipulating model parameters, they demonstrate the ability to control system dynamics, facilitating transitions between in-phase and anti-phase behaviors. This analytical framework offers a practical approach for optimizing transportation systems and improving social sustainability.

## Key Contributions

- Identified that lift synchronization in rule-based discrete models is governed by a competition between effective attractive and repulsive interactions.
- Demonstrated that tuning the ratio of these effective interactions allows for precise control over the transition between in-phase and anti-phase synchronization.
- Established a framework for analyzing real-world lift time-series data to optimize transport efficiency and sustainability.

## Open Questions & Future Work

- [[optimal-synchronization-regimes-for-transportation]]

## Key Concepts

- [[effective-interaction-decomposition-multi-agent]]: A framework for modeling the synchronization of multi-agent systems by decomposing their aggregate time-series behavior into competing effective attractive and repulsive interaction terms.

## Archivist Review

The paper provides a compelling framework for interpreting multi-agent synchronization through effective force decomposition. I generalized the concepts and open questions to ensure they are applicable beyond the specific domain of elevator systems, aligning them with broader research in multi-agent system dynamics and transportation optimization.

### Approved Concepts
- Effective Interaction Decomposition for Multi-Agent Systems: Provides a generalizable analytical framework for interpreting synchronization phenomena in stochastic, rule-based multi-agent systems by decomposing dynamics into effective forces.

### Approved Open Questions
- Optimal synchronization for transportation: Directly informs the design of smart transportation infrastructure by moving beyond mere observation of synchronization toward purposeful, performance-oriented control.

### Rejected Candidates
- [concept] Effective Lift Interaction Modeling (`effective-lift-interaction-modeling`) - subcomponent_of_broader_mechanism: Too narrow; generalized to 'Effective Interaction Decomposition for Multi-Agent Systems' to be reusable across domains.
- [open_question] Efficiency of lift synchronization (`lift-synchronization-efficiency-optimization`) - duplicate_existing: Too closely tied to a specific system; rephrased to emphasize general transportation synchronization optimization.

## Links

- [Abstract](https://arxiv.org/abs/2604.00425)
- [PDF](https://arxiv.org/pdf/2604.00425)

