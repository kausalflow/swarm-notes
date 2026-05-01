---
# CSL-compatible fields
title: "Observation-Guided Neural Surrogate Learning for Scientific Simulation Emulation: A Single-Gauge Flood-Inundation Proof of Concept"
author:
  - literal: "Marzieh Alireza Mirhoseini"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2604.25890"

# Custom fields
paper_id: "2604.25890"
paper_source: "openalex"
domain: "time-series,computer-vision"
tags:
  - "time-series"
  - "forecasting"
  - "spatial-attention"
  - "simulation-emulation"
  - "neural-surrogate"
architectures:
  []
datasets:
  []
concept_slugs:
  - "observation-guided-neural-surrogate-learning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:23:06Z"
created_at: "2026-05-01T07:23:06Z"
---

# Observation-Guided Neural Surrogate Learning for Scientific Simulation Emulation: A Single-Gauge Flood-Inundation Proof of Concept

**Authors**: Marzieh Alireza Mirhoseini
**Date**: 2026-04-28
**Paper ID**: [openalex:2604.25890](https://arxiv.org/abs/2604.25890)

## Summary

This paper proposes an observation-guided neural surrogate framework to emulate complex LISFLOOD-FP hydrodynamic simulations. The method utilizes a coarse ensemble-approximated Gaussian process model followed by a U-Net-ASPP neural corrector to refine spatial flood-inundation maps. By using single-site gauge data as a pointwise training anchor while applying simulation-based losses elsewhere, the model achieves high accuracy and consistency against hydrodynamic benchmarks in the Chicago metropolitan area.

## Key Contributions

- Introduces a hybrid simulation-emulation framework that combines ensemble Gaussian processes with a neural correction layer to map hydrodynamic simulation results.
- Demonstrates that sparse, single-site point observation targets can effectively anchor neural surrogates to improve localized simulation accuracy (R^2 ~ 0.99).
- Provides a methodology for converting site-specific stage records into datum-consistent water-depth targets for neural model training.

## Open Questions & Future Work

- [[generalization-of-observation-guided-flood-surrogates]]

## Key Concepts

- [[observation-guided-neural-surrogate-learning]]: A framework that integrates sparse real-world point observations as a training target to refine physics-based simulation emulators.

## Archivist Review

I approved the concept of 'Observation-Guided Neural Surrogate Learning' because it represents a distinct and reusable paradigm for integrating sparse real-world data with simulation surrogates. The U-Net-ASPP architecture was rejected as a standard implementation subcomponent. The open question regarding the generalization of this framework was approved as it captures the core bottleneck of scaling localized point-anchored models to broader, multi-sensor environmental systems.

### Approved Concepts
- Observation-Guided Neural Surrogate Learning: Provides a novel way to anchor neural simulation emulators to sparse, real-world pointwise observations while training on high-fidelity simulation data.

### Approved Open Questions
- Generalizing observation-guided flood surrogates: Establishing the generalizability and robustness of observation-guided surrogates is necessary for their deployment in real-world large-scale environmental monitoring.

### Rejected Candidates
- [concept] U-Net-ASPP Neural Corrector (`u-net-aspp-neural-corrector`) - subcomponent_of_broader_mechanism: The use of U-Net and ASPP is a common architectural implementation detail rather than a distinct, reusable forecasting paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2604.25890)
- [PDF](https://arxiv.org/pdf/2604.25890)

