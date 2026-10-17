---
# CSL-compatible fields
title: "Test-Time Forecasting: Recurrent Depth Enables In-Context Dynamics Prediction"
author:
  - literal: "Jeffrey B. Lai"
  - literal: "J. Quinn"
  - literal: "Anthony Bao"
  - literal: "William Sawrey Gilpin"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19552"

# Custom fields
paper_id: "2610.19552"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "in-context-learning"
  - "scaling-law"
architectures:
  []
datasets:
  []
concept_slugs:
  - "test-time-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:54:51Z"
created_at: "2026-10-17T08:54:51Z"
---

# Test-Time Forecasting: Recurrent Depth Enables In-Context Dynamics Prediction

**Authors**: Jeffrey B. Lai, J. Quinn, Anthony Bao, William Sawrey Gilpin
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19552](https://arxiv.org/abs/2610.19552)

## Summary

This paper investigates whether foundation models can learn generalizable in-context forecasting strategies for dynamical systems, establishing a link between linear attention and dynamic mode decomposition. Building upon this, the authors propose the Test-Time Forecasting (TTF) framework, which uses iterations of gradient descent as recurrent depth to enable lightweight one-step forecasters to predict out-of-distribution ODEs and PDEs during autoregressive rollout.

## Key Contributions

- Established a theoretical link between linear attention and (extended) dynamic mode decomposition, showing looped transformers can emulate propagators for dynamical systems.
- Proposed the Test-Time Forecasting (TTF) framework, utilizing iterations of gradient descent as recurrent depth within a lightweight one-step forecaster.
- Demonstrated that TTF models trained on ODEs and PDEs successfully generalize to out-of-distribution system dynamics during autoregressive rollout.

## Open Questions & Future Work

- [[in-context-learning-mechanisms-dynamical-systems-foundation-models-1]]

## Key Concepts

- [[test-time-forecasting]]: A framework that leverages iterations of gradient descent as recurrent depth in a one-step forecaster for in-context dynamics prediction.

## Archivist Review

Approved the core Test-Time Forecasting framework concept and its foundational open question on in-context learning mechanisms in continuous dynamical systems foundation models. Rejected subcomponent ideas and over-broad research agendas following vault guidelines.

### Approved Concepts
- Test-Time Forecasting: It introduces a principled framework where a one-step forecaster leverages iterations of gradient descent as recurrent depth to achieve out-of-distribution generalization on dynamical systems.

### Approved Open Questions
- In-Context Learning in Dynamical Systems Foundation Models: Understanding the emergence of in-context learning in continuous dynamical systems bridges discrete language models and continuous scientific foundation models, guiding the design of more robust architectures.

### Rejected Candidates
- [concept] Recurrent Depth (`recurrent-depth`) - subcomponent_of_broader_mechanism: Subcomponent of the broader Test-Time Forecasting framework and shares high overlap with existing recurrent architectures.
- [open_question] Scaling and Generalizing Test-Time Forecasting Frameworks (`ttf-framework-scaling-and-generalization-directions-1`) - low_impact: Too broad and lists a multi-part agenda rather than a single focused open question.

## Links

- [Abstract](https://arxiv.org/abs/2610.19552)
- [PDF](https://arxiv.org/pdf/2610.19552)

