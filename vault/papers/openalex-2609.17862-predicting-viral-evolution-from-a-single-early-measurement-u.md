---
# CSL-compatible fields
title: "Predicting Viral Evolution from a Single Early Measurement Using the Target Cell Limited Model"
author:
  - literal: "Rahal Nanayakkara"
  - literal: "Paulo Tabuada"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.17862"

# Custom fields
paper_id: "2609.17862"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:18:25Z"
created_at: "2026-09-18T09:18:25Z"
---

# Predicting Viral Evolution from a Single Early Measurement Using the Target Cell Limited Model

**Authors**: Rahal Nanayakkara, Paulo Tabuada
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.17862](https://arxiv.org/abs/2609.17862)

## Summary

This paper addresses the problem of predicting viral evolution and clinical milestones—such as the time of infectiousness and peak viral load—from a single early viral load measurement using the Target Cell Limited (TCL) model. Because unobservable internal biological states make prediction challenging, the authors introduce a coordinate transformation converting the nonlinear dynamics into a monotone system. By leveraging monotone systems theory and invariant subspaces, they derive explicit analytical bounds for peak viral load and time to infectiousness.

## Key Contributions

- Introduces a coordinate transformation that converts nonlinear Target Cell Limited (TCL) viral dynamics into a monotone system.
- Derives explicit analytical formulae establishing strict upper bounds on peak viral load from a single early viral observation.
- Establishes guaranteed lower bounds on the time to infectiousness using monotone systems theory and invariant subspaces.

## Archivist Review

Applied strict criteria for vault inclusion. The paper presents a specialized biological control theory / dynamical systems application using the Target Cell Limited model rather than a broad machine learning forecasting primitive, and the open question is routine future work on parameter bounds in biological models.

### Rejected Candidates
- [open_question] Handling Parameter Uncertainty in Viral Dynamics (`parameter-uncertainty-viral-evolution`) - low_impact: Standard future work on parameter uncertainty and clinical heterogeneity in biological modeling, lacking a specific methodological bottleneck for general ML forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2609.17862)
- [PDF](https://arxiv.org/pdf/2609.17862)

