---
# CSL-compatible fields
title: "Joint Neural Posterior Estimation and Model Selection for Chemical Reaction Networks"
author:
  - literal: "J. Arturo Esquivel"
  - literal: "Jorge A. Campos-Gonzalez-Angulo"
  - literal: "Sergio Pablo‐García"
  - literal: "Alán Aspuru‐Guzik"
  - literal: "Vianey Leos-Barajas"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.18825"

# Custom fields
paper_id: "2610.18825"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "attention-mechanism"
  - "self-attention"
  - "convolutional-neural-network"
  - "cnn"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:24:42Z"
created_at: "2026-10-16T09:24:42Z"
---

# Joint Neural Posterior Estimation and Model Selection for Chemical Reaction Networks

**Authors**: J. Arturo Esquivel, Jorge A. Campos-Gonzalez-Angulo, Sergio Pablo‐García, Alán Aspuru‐Guzik, Vianey Leos-Barajas
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.18825](https://arxiv.org/abs/2610.18825)

## Summary

This paper introduces a neural inference architecture for simulation-based Bayesian inference in Chemical Reaction Networks (CRNs) that simultaneously tackles reaction pathway model selection and reaction rate constant estimation. Using shared 1D-CNNs and a permutation-invariant Set Attention mechanism, the framework learns low-dimensional summary statistics from variable-length, multi-experiment time series. These statistics condition both a model selection network for posterior model probabilities and model-specific conditional Invertible Neural Networks (cINNs) for parameter posteriors. Evaluated on a protodeboronation reaction example, the approach effectively resolves structural ambiguity and extracts kinetic parameters from competing catalyst deactivation pathways.

## Key Contributions

- Proposes a neural inference architecture for chemical reaction networks that jointly performs model selection and parameter posterior estimation from multi-experiment time-series data
- Utilizes shared 1D-CNNs and a permutation-invariant Set Attention mechanism to learn summary statistics from variable-length time series
- Combines a model selection network computing posterior model probabilities with model-specific conditional Invertible Neural Networks (cINNs)
- Demonstrates practical utility on a protodeboronation example involving competing catalyst deactivation pathways

## Archivist Review

Strictly adhered to vault guidelines by reviewing the provided candidate open question against the core time-series and dynamical systems scope, rejecting it as domain-specific chemistry inference rather than a general temporal modeling bottleneck. No concepts or datasets met the strict novelty and reusability standards.

### Rejected Candidates
- [open_question] Open-World Mechanism Discovery and Anomaly Detection (`open-world-mechanism-discovery-crn`) - low_impact: This open question pertains to open-world mechanism discovery in chemical reaction networks, which falls outside the core time-series forecasting and general temporal modeling scope of the vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.18825)
- [PDF](https://arxiv.org/pdf/2610.18825)

