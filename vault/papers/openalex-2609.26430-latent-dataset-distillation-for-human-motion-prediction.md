---
# CSL-compatible fields
title: "Latent Dataset Distillation for Human Motion Prediction"
author:
  - literal: "Tian Ge"
  - literal: "Guang Li"
  - literal: "Takahiro Ogawa"
  - literal: "Miki Haseyama"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.26430"

# Custom fields
paper_id: "2609.26430"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "time-series"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "latent-dataset-distillation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:55:07Z"
created_at: "2026-09-25T09:55:07Z"
---

# Latent Dataset Distillation for Human Motion Prediction

**Authors**: Tian Ge, Guang Li, Takahiro Ogawa, Miki Haseyama
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.26430](https://arxiv.org/abs/2609.26430)

## Summary

This paper introduces a latent dataset distillation framework for human motion prediction to overcome the limitations of direct gradient matching in high-dimensional motion spaces. By leveraging a residual-quantized variational autoencoder (RVQ-VAE) to compress motions and optimizing a learnable latent bank through a frozen decoder, the method ensures generated synthetic motions maintain pose plausibility and temporal dynamics. Experiments on Human3.6M, CMU, and 3DPW benchmarks demonstrate significant quantitative and qualitative improvements over baseline distillation strategies.

## Key Contributions

- Proposes a latent dataset distillation framework for human motion prediction that regularizes distillation using a learned motion prior from a residual-quantized VAE.
- Optimizes a learnable latent bank through a frozen quantizer and decoder, avoiding the implausible and unstable synthetic motions caused by direct gradient matching in the original high-dimensional motion space.
- Demonstrates superior performance across Human3.6M, CMU, and 3DPW datasets, outperforming direct gradient matching in 27 of 30 evaluated settings.

## Key Concepts

- [[latent-dataset-distillation]]: A dataset distillation framework for human motion prediction that optimizes a learnable latent bank through a pretrained RVQ-VAE decoder to ensure pose plausibility and temporal consistency.

## Archivist Review

Approved the primary concept of latent dataset distillation as a distinct, reusable framework for high-dimensional structured time-series and motion forecasting. Rejected the open question as boilerplate future work. No datasets were approved since Human3.6M, CMU, and 3DPW are standard or already covered in the vault.

### Approved Concepts
- Latent Dataset Distillation: Introduces a principled dataset distillation approach for human motion prediction by operating in a compressed latent space regularized by a pretrained RVQ-VAE decoder and residual quantization.

### Rejected Candidates
- [open_question] Temporal Dataset Distillation for Motion (`adapting-temporal-dataset-distillation-to-motion`) - weak_evidence: This is a boilerplate future work question about applying a method to a new domain without outlining a specific technical bottleneck or mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2609.26430)
- [PDF](https://arxiv.org/pdf/2609.26430)

