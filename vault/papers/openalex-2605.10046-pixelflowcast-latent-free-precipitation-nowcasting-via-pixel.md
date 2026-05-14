---
# CSL-compatible fields
title: "PixelFlowCast: Latent-Free Precipitation Nowcasting via Pixel Mean Flows"
author:
  - literal: "Yufeng Zhu"
  - literal: "Chunlei Shi"
  - literal: "Yongchao Feng"
  - literal: "Dan Niu"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10046"

# Custom fields
paper_id: "2605.10046"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "forecasting"
  - "time-series"
  - "generative-adversarial-network"
architectures:
  []
datasets:
  - "sevir"
concept_slugs:
  - "pixel-mean-flows-pmf"
dataset_slugs:
  - "sevir"
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:38:41Z"
created_at: "2026-05-14T07:38:41Z"
---

# PixelFlowCast: Latent-Free Precipitation Nowcasting via Pixel Mean Flows

**Authors**: Yufeng Zhu, Chunlei Shi, Yongchao Feng, Dan Niu
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10046](https://arxiv.org/abs/2605.10046)

## Summary

PixelFlowCast is a two-stage probabilistic forecasting framework designed for high-resolution, high-efficiency precipitation nowcasting. By utilizing a deterministic coarse-forecast stage followed by a KAN-based conditional feature extractor, the system achieves fine-grained predictions without latent space compression. The core Pixel Mean Flows (PMF) predictor employs an x-prediction mechanism to achieve high-quality generation with few-step inference, making it suitable for real-time operational deployment.

## Key Contributions

- Introduces PixelFlowCast, a two-stage latent-free precipitation nowcasting framework that avoids compression-related degradation.
- Proposes Pixel Mean Flows (PMF) to enable few-step, high-fidelity forecasting by directly modeling pixel-space probability trajectories.
- Achieves state-of-the-art performance on the SEVIR dataset with significantly reduced inference time compared to latent-based diffusion models.

## Open Questions & Future Work

- [[physics-informed-nowcasting-consistency]]

## Key Concepts

- [[pixel-mean-flows-pmf]]: A latent-free probabilistic prediction mechanism that uses flow matching directly on pixel space for high-fidelity, high-speed sequence generation.

## Archivist Review

I have approved the core Pixel Mean Flows (PMF) mechanism as a novel latent-free generative approach for forecasting, along with a high-level open question regarding the integration of physical constraints in such frameworks. I rejected the proposed KAN-based sub-network as it functions primarily as a local architectural choice rather than a reusable paradigm, and I included the SEVIR dataset which is a standard benchmark in this specific domain.

### Approved Concepts
- Pixel Mean Flows (PMF): It is the core innovation of the paper, replacing latent-space diffusion with a pixel-level flow matching approach to preserve high-frequency weather details.

### Approved Open Questions
- Physics-Informed Precipitation Nowcasting: This is a substantial bottleneck because data-driven models frequently produce predictions that are visually plausible but physically impossible or inconsistent, which reduces their utility for critical meteorological decision-making.

### Rejected Candidates
- [concept] KANCondNet (`kancondnet`) - subcomponent_of_broader_mechanism: This is a paper-local architectural subcomponent (a specific KAN-based encoder) rather than a widely reusable mechanism.

## Datasets

- [[sevir]]

## Links

- [Abstract](https://arxiv.org/abs/2605.10046)
- [PDF](https://arxiv.org/pdf/2605.10046)

