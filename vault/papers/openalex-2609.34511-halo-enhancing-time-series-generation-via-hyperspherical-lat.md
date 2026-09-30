---
# CSL-compatible fields
title: "HALO: Enhancing Time Series Generation via Hyperspherical Latents and Masked AutoregRessive Modeling"
author:
  - literal: "Chunyi Hou"
  - literal: "Xiangfei Qiu"
  - literal: "Hanyin Cheng"
  - literal: "Yutong Li"
  - literal: "Bin Yang"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34511"

# Custom fields
paper_id: "2609.34511"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "generative-model"
  - "autoregressive"
  - "vae"
  - "representation-learning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "halo"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:50:26Z"
created_at: "2026-09-30T10:50:26Z"
---

# HALO: Enhancing Time Series Generation via Hyperspherical Latents and Masked AutoregRessive Modeling

**Authors**: Chunyi Hou, Xiangfei Qiu, Hanyin Cheng, Yutong Li, Bin Yang
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34511](https://arxiv.org/abs/2609.34511)

## Summary

Existing time series generators suffer from information loss during discrete latent discretization and error accumulation during autoregressive generation. To overcome these issues, the authors propose HALO, which performs generative modeling in a continuous latent space via hyperspherical latents and masked autoregressive modeling. HALO uses a hyperspherical VAE to stabilize latent representations and a masked autoregressive model to balance parallel decoding with temporal correlation learning. Experiments demonstrate state-of-the-art generation performance and improved inference efficiency over advanced baselines.

## Key Contributions

- Proposes HALO, a time series generation framework operating in a continuous latent space using hyperspherical latents and masked autoregressive modeling.
- Introduces a hyperspherical VAE that constrains continuous latents to a fixed-radius hyperspherical shell to stabilize numerical fluctuations.
- Develops a masked autoregressive model to balance parallel decoding and temporal correlation learning, reducing inference steps and improving generation stability.
- Achieves state-of-the-art generation performance and superior inference efficiency compared to existing baselines.

## Limitations

The abstract does not specify limitations or future work directions.

## Open Questions & Future Work

- [[continuous-latent-autoregressive-time-series-generation]]

## Key Concepts

- [[halo]]: A time series generation framework that utilizes hyperspherical latents and masked autoregressive modeling to eliminate discretization loss and error accumulation.

## Archivist Review

The central framework HALO is approved as a strong representative concept for continuous latent time series generation, while its constituent blocks are appropriately pruned as subcomponents. The open question capturing the continuous-latent versus discrete-codebook generation trade-off is retained for tracking.

### Approved Concepts
- HALO: Core framework introduced for time series generation combining hyperspherical continuous latents and masked autoregressive modeling.

### Approved Open Questions
- Continuous Latent Time Series Generation: Overcoming the limitations of discrete codebooks versus continuous latent representations is crucial for improving fine-grained temporal fidelity and generation stability in time series foundation models.

### Rejected Candidates
- [concept] Hyperspherical VAE (`hyperspherical-vae`) - subcomponent_of_broader_mechanism: Subcomponent of the broader HALO framework; VAEs on hyperspheres are established architectures.
- [concept] Masked Autoregressive Model (`masked-autoregressive-model`) - subcomponent_of_broader_mechanism: Masked autoregression is a well-known paradigm in generative modeling.

## Links

- [Abstract](https://arxiv.org/abs/2609.34511)
- [PDF](https://arxiv.org/pdf/2609.34511)

