---
# CSL-compatible fields
title: "GenONet: A Generative operator Network for High-Resolution Precipitation Nowcasting"
author:
  - literal: "Mohammad Kian Golkar"
  - literal: "Luciano Alves de Oliveira"
  - literal: "Mohammad Khanjani"
  - literal: "et al."
issued:
  date-parts:
    - [2026, 9, 1]
url: "https://arxiv.org/abs/2609.00544"

# Custom fields
paper_id: "2609.00544"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "gan"
  - "generative-adversarial-network"
  - "forecasting"
  - "time-series"
  - "multimodal"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-04T09:11:13Z"
created_at: "2026-09-04T09:11:13Z"
---

# GenONet: A Generative operator Network for High-Resolution Precipitation Nowcasting

**Authors**: Mohammad Kian Golkar, Luciano Alves de Oliveira, Mohammad Khanjani, et al.
**Date**: 2026-09-01
**Paper ID**: [openalex:2609.00544](https://arxiv.org/abs/2609.00544)

## Summary

The paper introduces GenONet, a Spatio-Temporal U-DeepONet integrated within a Generative Adversarial Network (GAN) framework, designed for high-resolution precipitation nowcasting up to 3 hours. By employing a Deep Operator Network (DeepONet) as a generator, the model learns continuous-time precipitation dynamics to prevent forecast blurriness over long horizons. Furthermore, an adversarial discriminator and a physics-informed loss regularizer based on the Moisture Conservation Equation ensure both structural sharpness and physical plausibility. Quantitative and qualitative evaluations demonstrate superior performance over baseline models, particularly for high-intensity storm events at extended lead times.

## Key Contributions

- Introduced GenONet, a Spatio-Temporal U-DeepONet embedded within a GAN framework for high-resolution precipitation nowcasting up to 3 hours.
- Leveraged DeepONet to learn continuous-time precipitation dynamics, mitigating forecast blurriness and degradation over long horizons.
- Incorporated a physics-informed loss regularizer derived from the Moisture Conservation Equation to enforce physical plausibility.

## Limitations

Evaluated specifically on precipitation forecasting; generalizability to other weather variables remains to be explored.

## Archivist Review

Applied strict scarcity and novelty filters. The proposed concept (GenONet) is paper-specific architecture combining DeepONet and GANs for a particular application, which is better treated as a local implementation rather than a standalone vault entry. No other concepts, open questions, or datasets were provided or met the rigorous threshold.

### Rejected Candidates
- [concept] GenONet (`genonet`) - paper_local: GenONet is a paper-specific model architecture combining existing techniques (DeepONet and GAN) rather than a broadly reusable standalone concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.00544)
- [PDF](https://arxiv.org/pdf/2609.00544)

