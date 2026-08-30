---
# CSL-compatible fields
title: "Reservoir: A Large-Scale Simulated Dataset for Training and Evaluating Epidemiological Models"
author:
  - literal: "Carson Dudley"
  - literal: "Reiden Magdaleno"
  - literal: "Marisa Eisenberg"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.27408"

# Custom fields
paper_id: "2608.27408"
paper_source: "openalex"
domain: "biology"
tags:
  - "dataset"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "reservoir"
concept_slugs:
  - "reservoir"
dataset_slugs:
  - "reservoir"
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:10:56Z"
created_at: "2026-08-30T10:10:56Z"
---

# Reservoir: A Large-Scale Simulated Dataset for Training and Evaluating Epidemiological Models

**Authors**: Carson Dudley, Reiden Magdaleno, Marisa Eisenberg
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.27408](https://arxiv.org/abs/2608.27408)

## Summary

This paper introduces Reservoir, a large-scale open simulator and dataset containing 500,000 realistic epidemic outbreak trajectories across one billion simulated days. Designed to address the data scarcity and unobservability challenges in infectious disease epidemiology, Reservoir provides complete ground-truth labels including true infection counts, reproduction numbers, and counterfactual intervention effects. The framework enables training, forecasting, and surveillance-design studies at a scale previously unattainable with real-world data alone.

## Key Contributions

- Introduces Reservoir, a large-scale open simulator and dataset of 500,000 realistic epidemic trajectories spanning one billion simulated days.
- Provides complete ground-truth labels for unmeasurable real-world quantities, including true infection counts, time-varying reproduction numbers, and counterfactual intervention effects.
- Enables training and evaluation of large-scale AI epidemiological forecasting, surveillance-design, and counterfactual intervention models beyond real-world data constraints.

## Limitations

Evaluated primarily on simulated trajectories rather than direct real-world transfer without domain adaptation.

## Open Questions & Future Work

- [[behavioral-feedback-and-spatial-dynamics-in-epidemiological-simulators]]

## Key Concepts

- [[reservoir]]: A large-scale open simulator and dataset of realistic epidemic simulations providing complete ground-truth labels for training AI epidemiological models.

## Archivist Review

Approved the Reservoir concept and dataset as a valuable, newly introduced benchmark for epidemiological AI modeling, along with its specific open question on simulator fidelity and behavioral feedback. All constraints and vault standards were strictly followed.

### Approved Concepts
- Reservoir: It introduces a massive, foundational simulated dataset and open simulator specifically designed for training and evaluating large-scale AI epidemiological models with complete ground-truth labels.

### Approved Open Questions
- Behavioral Feedback and Spatial Dynamics in Epidemiological Simulators: Enhancing simulator realism with behavioral feedbacks, resource constraints, and empirical spatial-demographic data is critical for training robust foundation models that generalize effectively to complex real-world outbreaks.

## Datasets

- [[reservoir]]

## Links

- [Abstract](https://arxiv.org/abs/2608.27408)
- [PDF](https://arxiv.org/pdf/2608.27408)

