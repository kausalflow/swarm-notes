---
# CSL-compatible fields
title: "ChronoVAE-HOPE: Beyond Attention -- A Next-Generation VAE Foundation Model for Specialized Time Series Classification"
author:
  - literal: "José Alberto Rodríguez"
  - literal: "Luis Balderas"
  - literal: "Miguel Lastra"
  - literal: "Antonio Araúzo-Azofra"
  - literal: "José M. Benítez"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22684"

# Custom fields
paper_id: "2605.22684"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "vae"
  - "variational-autoencoder"
  - "time-series"
  - "classification"
  - "self-supervised-learning"
  - "foundation-model"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "hope-block"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:45:28Z"
created_at: "2026-05-24T07:45:28Z"
---

# ChronoVAE-HOPE: Beyond Attention -- A Next-Generation VAE Foundation Model for Specialized Time Series Classification

**Authors**: José Alberto Rodríguez, Luis Balderas, Miguel Lastra, Antonio Araúzo-Azofra, José M. Benítez
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22684](https://arxiv.org/abs/2605.22684)

## Summary

ChronoVAE-HOPE is a VAE-based foundation model designed to address efficiency and interpretability limitations in time series classification. It replaces quadratic attention with the HOPE Block, incorporating Titans modules for short-term retention and a Continuum Memory System for long-term historical context. The model disentangles latent representations into independent trend and seasonal components, enabling robust performance across diverse domains after self-supervised pre-training on the Monash archive.

## Key Contributions

- Introduces ChronoVAE-HOPE, a foundation model architecture using a HOPE Block to replace quadratic attention with dual-memory systems.
- Achieves effective time series classification by factorizing latent representations into disentangled trend and seasonal components.
- Demonstrates superior classification performance on UCR benchmark datasets using embeddings derived from a self-supervised pre-trained encoder.

## Open Questions & Future Work

- [[stricter-disentanglement-vaes]]
- [[generative-data-augmentation-tsfm]]

## Key Concepts

- [[hope-block]]: A dual-memory VAE module utilizing Titans and Continuum Memory Systems to handle temporal dynamics without quadratic attention.

## Archivist Review

The HOPE block is approved as a significant architectural shift in time series foundation models. The subcomponent 'Continuum Memory System' was rejected in favor of the overarching HOPE block. The open questions were approved as they address fundamental challenges in latent space interpretability and generative augmentation for specialized domains. No datasets were approved as they were generic archival collections rather than novel research-critical artifacts.

### Approved Concepts
- HOPE Block: Central architectural innovation replacing standard quadratic attention with a dual-memory system for efficiency.

### Approved Open Questions
- Enforcing Latent Subspace Independence: Stricter disentanglement is essential for enhancing the interpretability of foundation model embeddings, allowing users to isolate and manipulate specific temporal factors (like seasonal cycles) without affecting others (like global trends).
- Generative Data Augmentation Adaptation: Generative data augmentation provides a principled way to address data scarcity and intra-class imbalance in time series classification without requiring additional manual labeling or external data collection.

### Rejected Candidates
- [concept] Continuum Memory System (CMS) (`continuum-memory-system-cms`) - subcomponent_of_broader_mechanism: This is a subcomponent of the broader HOPE block architecture and does not warrant a standalone note.

## Links

- [Abstract](https://arxiv.org/abs/2605.22684)
- [PDF](https://arxiv.org/pdf/2605.22684)

