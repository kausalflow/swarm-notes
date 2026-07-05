---
# CSL-compatible fields
title: "Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs"
author:
  - literal: "Francesca Pistilli"
  - literal: "Simone Peirone"
  - literal: "Giuseppe Averta"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.02425"

# Custom fields
paper_id: "2607.02425"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "graph-neural-network"
  - "reasoning"
  - "dataset"
  - "benchmark"
architectures:
  []
datasets:
  - "sg-ego-dataset"
concept_slugs:
  - "activity-driven-graph-edit-forecasting-a-gef"
dataset_slugs:
  - "sg-ego-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:53:40Z"
created_at: "2026-07-05T07:53:40Z"
---

# Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs

**Authors**: Francesca Pistilli, Simone Peirone, Giuseppe Averta
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.02425](https://arxiv.org/abs/2607.02425)

## Summary

The paper introduces SG-Ego, an extension of the Ego4D dataset with spatio-temporal scene graphs, to address the lack of structured reasoning in embodied AI for first-person video understanding. To exploit these representations, the authors propose GLEN, a graph-based model capable of aligning scene dynamics with textual actions. Furthermore, they define the Activity-driven Graph-Edit Forecasting (A-GEF) task, which requires predicting structured scene transformations conditioned on human activity, demonstrating superior performance over raw video baselines and MLLMs in long-horizon reasoning tasks.

## Key Contributions

- Introduces SG-Ego, an extension of the Ego4D dataset providing spatio-temporal scene graph annotations for rich grounded activity understanding.
- Proposes GLEN, a graph-based model that aligns scene graph sequences with textual actions to effectively model temporal scene evolution.
- Formulates the Activity-driven Graph-Edit Forecasting (A-GEF) task, enabling structured, controllable predictions of how human actions transform environment states.

## Open Questions & Future Work

- [[spatial-prediction-for-embodied-ai]]

## Key Concepts

- [[activity-driven-graph-edit-forecasting-a-gef]]: A task formulation that models scene dynamics as a sequence of structured transformations conditioned on human activity.

## Archivist Review

I have approved the A-GEF task as a distinct, reusable forecasting paradigm that shifts the field toward structured scene evolution. I have also approved the SG-Ego dataset as a key, named resource for evaluating this task. The open question regarding spatial prediction in embodied AI addresses a critical research bottleneck in transitioning from static analysis to active robotic interaction.

### Approved Concepts
- Activity-driven Graph-Edit Forecasting (A-GEF): It shifts the focus of video forecasting from pixel-based prediction to structured, interpretable graph transformations conditioned on human intent.

### Approved Open Questions
- Spatial Prediction for Embodied AI: Bridging structured scene representation with spatial reasoning is essential for moving from passive video analysis to active robotic control and embodied AI planning.

### Rejected Candidates
- [concept] SG-Ego Dataset (`sg-ego-dataset`) - subcomponent_of_broader_mechanism: This candidate is better suited as a dataset entry; the concept of spatio-temporal scene graph annotation itself is broader than the specific dataset SG-Ego.

## Datasets

- [[sg-ego-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2607.02425)
- [PDF](https://arxiv.org/pdf/2607.02425)

