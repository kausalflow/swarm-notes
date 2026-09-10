---
# CSL-compatible fields
title: "NOAH: Learning the Full Patient Journey. A Longitudinal Multimodal Time-Aware Model for Representation and Forecasting"
author:
  - literal: "Tobias Susetzky"
  - literal: "Raphael Rehms"
  - literal: "Dmitrii Seletkov"
  - literal: "Özgün Turgut"
  - literal: "Michelle Espranita Liman"
  - literal: "Lisa Steinhelfer"
  - literal: "Rickmer Braren"
  - literal: "Daniel Rueckert"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.09140"

# Custom fields
paper_id: "2609.09140"
paper_source: "openalex"
domain: "medicine"
tags:
  - "transformer"
  - "generative-model"
  - "multimodal"
  - "time-series"
  - "healthcare"
  - "foundation-model"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "noah"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:16:17Z"
created_at: "2026-09-10T09:16:17Z"
---

# NOAH: Learning the Full Patient Journey. A Longitudinal Multimodal Time-Aware Model for Representation and Forecasting

**Authors**: Tobias Susetzky, Raphael Rehms, Dmitrii Seletkov, Özgün Turgut, Michelle Espranita Liman, Lisa Steinhelfer, Rickmer Braren, Daniel Rueckert
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.09140](https://arxiv.org/abs/2609.09140)

## Summary

The paper introduces NOAH, a time-aware, task-agnostic generative transformer model designed to represent and forecast the full multimodal patient journey across longitudinal records. Trained on hundreds of millions of clinical events from the MIMIC dataset family, NOAH integrates medical images, time-series, categorical events, and unstructured notes using bidirectional time integration and a variational latent space. The model supports flexible capabilities such as autoregressive forecasting with time control, zero-shot classification, and counterfactual simulation, outperforming prior discriminative or modality-restricted healthcare AI approaches.

## Key Contributions

- Introduces NOAH, a generative transformer foundation model that processes over 559 million clinical events across multiple modalities including medical images, time-series, categorical events, and clinical text.
- Features a bidirectional time integration and a variational latent space designed to capture continuous temporal evolution and clinical trajectory stochasticity.
- Enables task-agnostic capabilities including autoregressive forecasting with time control, zero-shot classification, and counterfactual intervention simulation, demonstrating strong performance across ICD chapters, comorbidities, and time-to-event prediction.

## Open Questions & Future Work

- [[autoregressive-exposure-bias-long-horizon-forecasting]]

## Key Concepts

- [[noah]]: A time-aware, task-agnostic, generative transformer model for representing and forecasting the full multimodal patient journey.

## Archivist Review

Approved the core framework concept 'noah' and the open question concerning autoregressive exposure bias in long-horizon clinical forecasting. No datasets were approved per vault constraints and duplication rules against existing MIMIC records.

### Approved Concepts
- NOAH: It serves as the core generative foundation model for representing and forecasting holistic multimodal longitudinal patient records.

### Approved Open Questions
- Mitigating Autoregressive Exposure Bias: Exposure bias and error propagation limit the reliability of multi-step autoregressive rollouts for long-term clinical forecasting and simulation.

## Links

- [Abstract](https://arxiv.org/abs/2609.09140)
- [PDF](https://arxiv.org/pdf/2609.09140)

