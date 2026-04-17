---
# CSL-compatible fields
title: "Forecasting the Past: Gradient-Based Distribution Shift Detection in Trajectory Prediction"
author:
  - literal: "Michele De Vita"
  - literal: "Julian Wiederer"
  - literal: "Vasileios Belagiannis"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2604.12425"

# Custom fields
paper_id: "2604.12425"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "forecasting"
  - "robotics"
  - "autonomous-agent"
  - "self-supervised-learning"
architectures:
  []
datasets:
  - "Argoverse"
concept_slugs:
  - "gradient-based-distribution-shift-detection"
dataset_slugs:
  - "argoverse"
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:29:28Z"
created_at: "2026-04-17T06:29:28Z"
---

# Forecasting the Past: Gradient-Based Distribution Shift Detection in Trajectory Prediction

**Authors**: Michele De Vita, Julian Wiederer, Vasileios Belagiannis
**Date**: 2026-04-14
**Paper ID**: [openalex:2604.12425](https://arxiv.org/abs/2604.12425)

## Summary

This paper introduces a post-hoc, self-supervised framework for detecting distributional shifts in trajectory prediction models, which are critical in autonomous driving contexts. The method trains a decoder to forecast the latter half of observed trajectories from the first half, using the L2 norm of the gradient of this loss to quantify distribution shifts. This approach is model-agnostic, preserving the integrity of the original trajectory prediction system while providing reliable detection capabilities. Experimental results on Shifts and Argoverse benchmarks, as well as a Highway simulator collision detection task, demonstrate the effectiveness and versatility of the proposed scoring metric.

## Key Contributions

- Introduces a post-hoc self-supervised method to detect distribution shifts by training a decoder on trajectory sub-sequences.
- Utilizes the L2 norm of the decoder's gradient as a shift indicator, ensuring no degradation of the original model's prediction performance.
- Achieves significant improvements in shift detection benchmarks on the Shifts and Argoverse datasets and demonstrates utility in collision early-detection for motion planners.

## Key Concepts

- [[gradient-based-distribution-shift-detection]]: A method for identifying out-of-distribution trajectories by monitoring the gradient norms of a self-supervised auxiliary forecasting task.

## Archivist Review

I have approved the core methodological concept of gradient-based distribution shift detection, as it provides a model-agnostic, post-hoc mechanism for reliability assessment that is highly relevant to temporal forecasting. Argoverse was approved as a standard, high-impact benchmark for trajectory modeling, while the 'Shifts' dataset was rejected for being a generic, multi-purpose benchmark rather than a specific, novel contribution or a foundational requirement for this niche. No new open questions were identified that were not already sufficiently covered by existing general robustness queries.

### Approved Concepts
- Gradient-Based Distribution Shift Detection: Provides a post-hoc, non-intrusive method for detecting distributional shifts in trajectory prediction without modifying the base model.

### Rejected Candidates
- [dataset] Shifts (`Shifts`) - generic: The dataset is too generic and commonly used across various machine learning contexts.

## Datasets

- [[argoverse]]

## Links

- [Abstract](https://arxiv.org/abs/2604.12425)
- [PDF](https://arxiv.org/pdf/2604.12425)

