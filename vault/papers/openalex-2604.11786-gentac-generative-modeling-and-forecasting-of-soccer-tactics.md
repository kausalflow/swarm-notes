---
# CSL-compatible fields
title: "GenTac: Generative Modeling and Forecasting of Soccer Tactics"
author:
  - literal: "Jiayuan Rao"
  - literal: "Tianlin Gui"
  - literal: "Haoning Wu"
  - literal: "Yanfeng Wang"
  - literal: "Weidi Xie"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11786"

# Custom fields
paper_id: "2604.11786"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "diffusion-model"
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "agent"
  - "benchmark"
architectures:
  []
datasets:
  - "tacbench"
concept_slugs:
  - "gentac-framework"
dataset_slugs:
  - "tacbench"
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:28:30Z"
created_at: "2026-04-16T06:28:30Z"
---

# GenTac: Generative Modeling and Forecasting of Soccer Tactics

**Authors**: Jiayuan Rao, Tianlin Gui, Haoning Wu, Yanfeng Wang, Weidi Xie
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11786](https://arxiv.org/abs/2604.11786)

## Summary

GenTac is a diffusion-based generative framework that models soccer tactics as a stochastic process, enabling the generation of diverse and long-horizon player trajectories and tactical events. By conditioning on contextual factors like team style and strategic objectives, the model achieves high geometric and structural fidelity while allowing for controllable counterfactual simulations. Extensive evaluation on the introduced TacBench benchmark highlights the model's ability to maintain stylistic nuance and predict future tactical outcomes, with demonstrated cross-domain generalization to other multi-agent team sports.

## Key Contributions

- Introduces GenTac, a diffusion-based framework that models soccer tactics by joint learning of continuous multi-player trajectories and discrete semantic events.
- Provides TacBench, a new benchmark for evaluating multi-agent tactical accuracy, stylistic nuance, and counterfactual simulation capabilities.
- Demonstrates controllable counterfactual simulation, allowing for strategic guidance through spatial control and expected threat metrics.
- Shows cross-domain generalization potential by applying the framework to basketball, American football, and ice hockey.

## Key Concepts

- [[gentac-framework]]: A generative framework that models multi-agent team sports as a joint stochastic process of continuous trajectories and discrete tactical events.

## Archivist Review

I approved the GenTac Framework as a distinct paradigm for modeling multi-agent systems via the fusion of continuous trajectories and discrete events. TacBench was approved as a named dataset benchmark for evaluation in this domain. I rejected the individual 'GenTac' concept as it was a duplicate of the framework, and rejected the conceptual entry for TacBench to prioritize the dataset classification.

### Approved Concepts
- GenTac Framework: It introduces a unified way to combine continuous agent trajectories with discrete event labels, which is a powerful paradigm for complex multi-agent forecasting.

### Rejected Candidates
- [concept] GenTac (`gentac`) - duplicate_existing: Redundant with GenTac Framework; the framework is the conceptual contribution, while the name is just a specific implementation.
- [concept] TacBench (`tacbench`) - other: TacBench is a dataset benchmark; it should be categorized as a dataset, not a concept.

## Datasets

- [[tacbench]]

## Links

- [Abstract](https://arxiv.org/abs/2604.11786)
- [PDF](https://arxiv.org/pdf/2604.11786)

