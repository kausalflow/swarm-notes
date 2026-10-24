---
# CSL-compatible fields
title: "LLM-Based Exogenous World Modeling for Dynamic Scheduling"
author:
  - literal: "Ni Zhang"
  - literal: "Haofeng Yuan"
  - literal: "Jianan Zhou"
  - literal: "Shiji Song"
  - literal: "Zhiguang Cao"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29308"

# Custom fields
paper_id: "2610.29308"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "llm"
  - "language-model"
  - "planning"
  - "reinforcement-learning"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "afterstate-world-model-planning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:12:22Z"
created_at: "2026-10-24T09:12:22Z"
---

# LLM-Based Exogenous World Modeling for Dynamic Scheduling

**Authors**: Ni Zhang, Haofeng Yuan, Jianan Zhou, Shiji Song, Zhiguang Cao
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29308](https://arxiv.org/abs/2610.29308)

## Summary

This paper introduces Afterstate World-Model Planning (AWMP), a framework that leverages pretrained large language models as exogenous components in structured world models to forecast uncertain job arrivals in dynamic scheduling. By utilizing afterstate decomposition, belief-conditioned dispatching, short scenario rollouts, and a surprise-triggered refresh mechanism with residual self-calibration, AWMP handles nonstationary arrivals effectively. Across dynamic and flexible job-shop benchmarks, AWMP significantly outperforms classical priority-dispatching rules by reducing weighted tardiness by up to 46%.

## Key Contributions

- Proposes Afterstate World-Model Planning (AWMP), utilizing a pretrained large language model as an exogenous world model to forecast uncertain job arrivals in dynamic scheduling.
- Employs an afterstate decomposition that separates deterministic shop transitions from uncertain exogenous arrivals, allowing compact belief representations.
- Introduces a surprise-triggered refresh mechanism and online residual self-calibration to handle nonstationary arrival distributions and forecast errors efficiently.
- Achieves 6-21% reduction in weighted tardiness on dynamic job-shop and 22-46% on flexible job-shop benchmarks compared to classical priority-dispatching rules.

## Open Questions & Future Work

- [[enriching-arrival-belief-job-attributes]]

## Key Concepts

- [[afterstate-world-model-planning]]: A structured world model framework combining LLM-based exogenous job arrival forecasting with belief-conditioned dispatching and short scenario rollouts for dynamic scheduling.

## Archivist Review

Approved the core conceptual framework of Afterstate World-Model Planning (AWMP) as a reusable idea for LLM-based exogenous forecasting in scheduling, along with one specific open question regarding arrival belief representations. All other redundant or subcomponent candidates were rejected in accordance with vault standards.

### Approved Concepts
- Afterstate World-Model Planning: Introduces a novel structured world model leveraging pretrained LLMs for exogenous forecasting in dynamic scheduling via afterstate decomposition and online calibration.

### Approved Open Questions
- Enriching Arrival Belief Representations: Capturing fine-grained job attributes rather than coarse aggregate counts could significantly enhance decision-making quality in heterogeneous, highly complex shop environments.

### Rejected Candidates
- [concept] Exogenous World Modeling (`exogenous-world-modeling`) - subcomponent_of_broader_mechanism: Subcomponent of broader mechanism covered by Afterstate World-Model Planning (AWMP).

## Links

- [Abstract](https://arxiv.org/abs/2610.29308)
- [PDF](https://arxiv.org/pdf/2610.29308)

