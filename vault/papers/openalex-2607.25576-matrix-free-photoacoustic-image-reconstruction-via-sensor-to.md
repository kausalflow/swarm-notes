---
# CSL-compatible fields
title: "Matrix-Free Photoacoustic Image Reconstruction via Sensor-Token Self-Attention"
author:
  - literal: "Mary John"
  - literal: "Shibili Said"
  - literal: "Imad Barhumi"
  - literal: "Sherzod Turaev"
  - literal: "Mohamed Yahia"
issued:
  date-parts:
    - [2026, 7, 28]
url: "https://arxiv.org/abs/2607.25576"

# Custom fields
paper_id: "2607.25576"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
  - "image-reconstruction"
  - "computational-imaging"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "sensor-attention-network"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-31T07:44:44Z"
created_at: "2026-07-31T07:44:44Z"
---

# Matrix-Free Photoacoustic Image Reconstruction via Sensor-Token Self-Attention

**Authors**: Mary John, Shibili Said, Imad Barhumi, Sherzod Turaev, Mohamed Yahia
**Date**: 2026-07-28
**Paper ID**: [openalex:2607.25576](https://arxiv.org/abs/2607.25576)

## Summary

Photoacoustic tomography (PAT) reconstruction is traditionally limited by the computational expense of iterative solvers and unrolled networks that rely on the system matrix during inference. To address this, the paper introduces the Sensor Attention Network (SAN), a Transformer architecture that treats each sensor's time series as a token and maps raw measurements directly to images without invoking the system matrix. Evaluated against traditional and learned baselines, SAN achieves superior image quality (SSIM 0.522, PSNR 22.09 dB) while reducing reconstruction time by an order of magnitude.

## Key Contributions

- Proposes the Sensor Attention Network (SAN), a Transformer-based architecture that bypasses the system matrix at inference for matrix-free photoacoustic image reconstruction.
- Achieves a mean SSIM of 0.522, PSNR of 22.09 dB, and NMSE of 0.233, outperforming ISTA, split-Bregman total variation, and learned ISTA (LISTA).
- Reduces reconstruction time by at least an order of magnitude compared to methods dependent on system matrix calculations.

## Limitations

Evaluated on 488 training and 46 held-out augmented samples, suggesting future work should scale to larger and more diverse in-vivo experimental datasets.

## Open Questions & Future Work

- [[3d-sensor-attention-network-pat]]

## Key Concepts

- [[sensor-attention-network]]: A Transformer-based architecture that treats sensor time series as tokens to perform matrix-free photoacoustic image reconstruction.

## Archivist Review

Approved the overarching concept 'Sensor Attention Network' as a reusable architecture for inverse problems and its explicit open question regarding 3D volume extension. No canonical dataset was provided.

### Approved Concepts
- Sensor Attention Network: Serves as the core methodological contribution, replacing traditional system matrix calculations with a matrix-free Transformer architecture.

### Approved Open Questions
- 3D Sensor Attention Network Extension: Scaling direct Transformer-based reconstruction to 3D and non-planar geometries is critical for bridging the gap between simulated 2D setups and realistic clinical 3D tomographic scanners.

## Links

- [Abstract](https://arxiv.org/abs/2607.25576)
- [PDF](https://arxiv.org/pdf/2607.25576)

