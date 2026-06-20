---
# CSL-compatible fields
title: "Low-dimensional representation of brain networks for seizure risk forecasting"
author:
  - literal: "Steven Rico-Aparicio"
  - literal: "Martin Guillemaud"
  - literal: "Alice Longhena"
  - literal: "Vincent Navarro"
  - literal: "Louis Cousyn"
  - literal: "Mario Chávez"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2505.00856"

# Custom fields
paper_id: "2505.00856"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "forecasting"
  - "embedding"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dimensionless-biomarker-b"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:40Z"
created_at: "2026-06-20T08:17:40Z"
---

# Low-dimensional representation of brain networks for seizure risk forecasting

**Authors**: Steven Rico-Aparicio, Martin Guillemaud, Alice Longhena, Vincent Navarro, Louis Cousyn, Mario Chávez
**Date**: 2026-06-17
**Paper ID**: [openalex:2505.00856](https://arxiv.org/abs/2505.00856)

## Summary

This paper presents a framework for seizure risk forecasting by embedding functional brain connectivity networks from intracranial EEG (iEEG) data into a low-dimensional Euclidean space. By focusing on topological features of these networks, the authors derive a novel dimensionless biomarker, B, that robustly distinguishes between interictal and preictal states. The method identifies informative electrodes through permutation-based testing and demonstrates significant predictive performance in pseudo-prospective forecasting tasks, offering a path toward individualized, real-time clinical seizure monitoring.

## Key Contributions

- Proposes a framework for embedding functional brain connectivity networks from iEEG into a low-dimensional Euclidean space to capture preictal dynamics.
- Introduces a dimensionless biomarker B that effectively discriminates between interictal and preictal states with high robustness.
- Validates the approach using pseudo-prospective forecasting and leave-one-out cross-validation, demonstrating predictive utility for real-time seizure monitoring.

## Open Questions & Future Work

- [[geometric-embedding-optimal-conditions-seizure-forecasting]]

## Key Concepts

- [[dimensionless-biomarker-b]]: A dimensionless metric derived from low-dimensional Euclidean embeddings of iEEG connectivity networks to distinguish preictal from interictal brain states.

## Archivist Review

I approved the biomarker concept as a novel clinical state discriminator and the open question regarding geometric embedding optimization as it addresses a fundamental design challenge in neuro-topological forecasting. Other candidates were not submitted. I adhered to the scarcity constraints and applied the requirement for high-level, reusable methodological contributions.

### Approved Concepts
- Dimensionless biomarker B: This biomarker is the primary innovation for classifying seizure risk states from brain network topology.

### Approved Open Questions
- Optimal Geometry for Brain Network Embeddings: The choice of geometric embedding space is a fundamental design decision in computational neuro-topology; clarifying when and why a specific space is optimal for brain network analysis is essential for transitioning these models from experimental frameworks to reliable clinical tools.

## Links

- [Abstract](https://arxiv.org/abs/2505.00856)
- [PDF](https://arxiv.org/pdf/2505.00856)

