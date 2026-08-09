---
# CSL-compatible fields
title: "Kastor: An efficient fine-tuning strategy for generative emulation of PDE simulations"
author:
  - literal: "Guillaume Couairon"
  - literal: "Alexis Jacq"
  - literal: "Yu-Han Wu"
  - literal: "Renu Singh"
  - literal: "Yana Hasson"
  - literal: "Quentin Berthet"
  - literal: "Romuald Elie"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.06107"

# Custom fields
paper_id: "2608.06107"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "benchmark"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "kastor"
  - "mean-prediction-regularization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:41:13Z"
created_at: "2026-08-09T05:41:13Z"
---

# Kastor: An efficient fine-tuning strategy for generative emulation of PDE simulations

**Authors**: Guillaume Couairon, Alexis Jacq, Yu-Han Wu, Renu Singh, Yana Hasson, Quentin Berthet, Romuald Elie
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.06107](https://arxiv.org/abs/2608.06107)

## Summary

Kastor is an efficient fine-tuning methodology that transforms deterministic physics foundation models into accurate generative surrogates for Partial Differential Equation (PDE) simulations. It employs a two-stage inference scheme with a large-stride causal autoregressive model and a temporal super-resolution network, coupled with Mean Prediction Regularization (MPR) and spatial gradient matching. Evaluated on diverse simulation datasets from The Well benchmark, Kastor substantially outperforms existing fine-tuning approaches like Walrus in forecasting accuracy and spectral consistency while reducing computational costs.

## Key Contributions

- Proposes Kastor, a methodology adapting deterministic physics foundation models into generative surrogate models for PDE simulations.
- Introduces a two-stage inference scheme combining large-stride causal autoregressive modeling with non-causal temporal super-resolution to reduce error accumulation.
- Presents Mean Prediction Regularization (MPR) to stabilize and enhance functional generative and diffusion-based emulators under null noise conditioning.
- Achieves a 42.9% average reduction in forecasting error compared to the Walrus fine-tuning baseline across diverse datasets from The Well benchmark.

## Open Questions & Future Work

- [[single-state-initialization-ml-emulators]]

## Key Concepts

- [[kastor]]: A comprehensive methodology for adapting deterministic physics foundation models into efficient generative surrogates for PDE simulations.
- [[mean-prediction-regularization]]: A training objective that constrains generative emulators to predict the deterministic distribution mean under null noise conditioning.

## Archivist Review

Approved the core methodology (Kastor) and its specialized training objective (Mean Prediction Regularization) as reusable contributions to generative physical emulation. Retained the open question on single-state initialization as a meaningful architectural bottleneck. Rejected 'The Well' dataset as it is an existing public benchmark collection.

### Approved Concepts
- Kastor: Kastor is the core novel methodology proposed in the paper for efficient fine-tuning of generative physics emulators.
- Mean Prediction Regularization: MPR is a novel training objective introduced to stabilize and improve generative and diffusion-based physical emulators.

### Approved Open Questions
- Single-State Initialization for Emulators: Removing the requirement for pre-computed history from numerical solvers is critical for end-to-end deployment of ML emulators in autonomous scientific discovery and real-time forecasting pipelines.

### Rejected Candidates
- [dataset] The Well (`the-well`) - not_novel: Dataset is a standard benchmark suite from prior work rather than a novel contribution of this paper.

## Links

- [Abstract](https://arxiv.org/abs/2608.06107)
- [PDF](https://arxiv.org/pdf/2608.06107)

