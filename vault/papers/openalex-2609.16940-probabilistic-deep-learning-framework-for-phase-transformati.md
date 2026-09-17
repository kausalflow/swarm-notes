---
# CSL-compatible fields
title: "Probabilistic Deep Learning Framework for Phase Transformation Forecasting aided by In Situ High temperature Microscopy"
author:
  - literal: "Ioannis Kouroudis"
  - literal: "Niki Balestrieri"
  - literal: "Stefan Rotzsche"
  - literal: "Niccolo Radice"
  - literal: "Peter Mayr"
  - literal: "Alessio Gagliardi"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.16940"

# Custom fields
paper_id: "2609.16940"
paper_source: "openalex"
domain: "materials"
tags:
  - "time-series"
  - "forecasting"
  - "variational-autoencoder"
  - "vae"
  - "transformer"
  - "uncertainty-estimation"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:44:49Z"
created_at: "2026-09-17T09:44:49Z"
---

# Probabilistic Deep Learning Framework for Phase Transformation Forecasting aided by In Situ High temperature Microscopy

**Authors**: Ioannis Kouroudis, Niki Balestrieri, Stefan Rotzsche, Niccolo Radice, Peter Mayr, Alessio Gagliardi
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.16940](https://arxiv.org/abs/2609.16940)

## Summary

The paper introduces a probabilistic deep-learning framework to forecast phase transformations and microstructure evolution, such as the Widmanstatten ferrite ratio, under arbitrary thermal histories using in situ high-temperature microscopy data. By combining a beta-variational autoencoder for surface image compression, a temporal fusion transformer for sequential prediction, and a Gaussian process for end-state correction, the method yields robust probabilistic prediction intervals across multiple cooling regimes in S235 steel.

## Key Contributions

- Introduces a probabilistic deep-learning framework that unifies image-based characterization, temporal prediction, and microstructure forecasting using in situ high-temperature confocal laser scanning microscopy data.
- Applies a beta-variational autoencoder to compress initial surface images into a low-dimensional latent space combined with temporal fusion transformers and Gaussian processes for quantile forecasting of microstructure evolution.
- Demonstrates high accuracy in predicting Widmanstatten ferrite evolution in S235 steel across five cooling regimes.

## Archivist Review

The paper presents a specialized materials science application combining standard components (beta-VAE, Temporal Fusion Transformer, Gaussian Process) to forecast phase transformations in steel. Since neither a distinct, broadly reusable forecasting methodology nor a generalizable open question is introduced beyond this specific domain, all candidates were rejected.

### Rejected Candidates
- [open_question] Multi-phase and online optimization extension (`multi-phase-and-online-optimization-extension`) - paper_local: The open question focuses on paper-specific metallurgical extensions (Widmanstätten ferrite to other phases) and closed-loop process control rather than a broad, reusable machine learning or time-series forecasting methodology bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.16940)
- [PDF](https://arxiv.org/pdf/2609.16940)

