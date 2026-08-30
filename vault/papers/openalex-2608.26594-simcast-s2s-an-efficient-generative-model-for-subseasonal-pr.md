---
# CSL-compatible fields
title: "SimCast-S2S: An Efficient Generative Model for Subseasonal Precipitation Forecasting via Transfer Learning from Climate Simulations"
author:
  - literal: "Hiep V. Dang"
  - literal: "Antonios Mamalakis"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26594"

# Custom fields
paper_id: "2608.26594"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "time-series"
  - "forecasting"
  - "transfer-learning"
  - "lora"
  - "vae"
  - "uncertainty-quantification"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "simcast-s2s"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:10:49Z"
created_at: "2026-08-30T10:10:49Z"
---

# SimCast-S2S: An Efficient Generative Model for Subseasonal Precipitation Forecasting via Transfer Learning from Climate Simulations

**Authors**: Hiep V. Dang, Antonios Mamalakis
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26594](https://arxiv.org/abs/2608.26594)

## Summary

The paper introduces SimCast-S2S, an efficient generative latent-diffusion framework for probabilistic subseasonal-to-seasonal (S2S) precipitation forecasting. To overcome data scarcity and high computational costs, SimCast-S2S operates within a compact variational autoencoder latent space and leverages transfer learning with low-rank adaptation (LoRA) from climate simulations to observational reanalysis data. Experimental results demonstrate that SimCast-S2S outperforms standard deep learning baselines and remains competitive with operational systems such as ECMWF-S2S without requiring post-processing or bias correction.

## Key Contributions

- Introduces SimCast-S2S, the first data-driven generative latent-diffusion framework for probabilistic subseasonal-to-seasonal (S2S) precipitation forecasting.
- Implements a compact latent space via variational autoencoders to enable efficient large-ensemble generation.
- Utilizes simulation-to-reanalysis transfer learning with low-rank adaptation (LoRA) to overcome data scarcity in observational reanalysis datasets.
- Outperforms deep learning baselines (CNNs and U-Nets) and remains competitive with operational systems like ECMWF-S2S without post-processing or calibration.

## Limitations

Uses only a subset of atmospheric input variables and operates without explicit post-processing or bias correction.

## Open Questions & Future Work

- [[physical-consistency-latent-diffusion-s2s]]

## Key Concepts

- [[simcast-s2s]]: A generative latent-diffusion framework for probabilistic subseasonal-to-seasonal precipitation forecasting using simulation-to-reanalysis transfer learning.

## Archivist Review

Approved the core framework note SimCast-S2S and the open question regarding physical consistency in latent diffusion S2S models. The second open question on interpretability was rejected as a duplicate of broader XAI attribution themes already tracked in the vault.

### Approved Concepts
- SimCast-S2S: It represents the core framework introduced in the paper, combining latent diffusion with simulation-to-reanalysis transfer learning for S2S precipitation forecasting.

### Approved Open Questions
- Enforcing Physical Consistency in Latent-Space Diffusion Models: Ensures that data-driven climate and weather models maintain physical consistency and reliability, particularly when forecasting rare or extreme events.

### Rejected Candidates
- [open_question] Explainable AI for Latent Diffusion Climate Models (`interpretability-latent-diffusion-s2s`) - duplicate_existing: Too similar to existing open questions regarding explainability and attribution in ML-based weather and climate forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2608.26594)
- [PDF](https://arxiv.org/pdf/2608.26594)

