---
# CSL-compatible fields
title: "Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching"
author:
  - literal: "Nicole Rogalla"
  - literal: "Yuzhen Qin"
  - literal: "Mario Senden"
  - literal: "Ahmed El-Gazzar"
  - literal: "Marcel van Gerven"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11178"

# Custom fields
paper_id: "2604.11178"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
architectures:
  []
datasets:
  - "algonauts-2025-fmri-dataset"
concept_slugs:
  - "autoregressive-flow-matching-afm"
dataset_slugs:
  - "algonauts-2025-fmri-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:28:45Z"
created_at: "2026-04-16T06:28:45Z"
---

# Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching

**Authors**: Nicole Rogalla, Yuzhen Qin, Mario Senden, Ahmed El-Gazzar, Marcel van Gerven
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11178](https://arxiv.org/abs/2604.11178)

## Summary

This paper introduces Autoregressive Flow Matching (AFM), a generative framework for probabilistic forecasting of neural dynamics based on multimodal sensory input. By treating neural activity as a temporally evolving process, the model learns the conditional distribution of future BOLD responses given past neural history and concurrent stimuli. Experiments on the Algonauts 2025 fMRI dataset demonstrate that AFM outperforms conventional general linear models and non-autoregressive flow-matching baselines, particularly in capturing complex temporal dependencies. The results highlight the potential of flow-based generative modeling for high-fidelity neural forecasting and closed-loop neurotechnology applications.

## Key Contributions

- Introduces Autoregressive Flow Matching (AFM) for probabilistic forecasting of complex neural dynamics.
- Demonstrates state-of-the-art performance on the Algonauts project 2025 fMRI benchmark compared to GLM and non-autoregressive flow-matching baselines.
- Provides analytical evidence that incorporating past temporal BOLD dynamics significantly enhances short-term predictive accuracy in neural modeling.

## Key Concepts

- [[autoregressive-flow-matching-afm]]: A generative modeling framework that learns conditional distributions of future states by combining flow matching with autoregressive temporal history.

## Archivist Review

I approved Autoregressive Flow Matching (AFM) as it provides a clear, reusable methodological advancement for spatiotemporal forecasting by integrating flow-based generative modeling with autoregressive temporal conditioning. I rejected the proposed dataset as it is highly specific to a single competitive challenge and not necessarily a foundational resource for the broader time-series field. No significant open questions were identified that were not already covered by existing research directions.

### Approved Concepts
- Autoregressive Flow Matching (AFM): It is the core methodological contribution, combining flow matching with autoregressive conditioning for temporal dynamics.

### Rejected Candidates
- [dataset] Algonauts project 2025 challenge functional magnetic resonance imaging dataset (`algonauts-2025-fmri-dataset`) - low_impact: The dataset is very specific to a single challenge and lacks evidence of broader utility for future research beyond this specific fMRI benchmark.

## Datasets

- [[algonauts-2025-fmri-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2604.11178)
- [PDF](https://arxiv.org/pdf/2604.11178)

