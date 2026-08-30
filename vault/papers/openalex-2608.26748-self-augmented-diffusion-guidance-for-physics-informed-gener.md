---
# CSL-compatible fields
title: "Self-Augmented Diffusion Guidance for Physics-Informed Generation"
author:
  - literal: "Akira Osaka"
  - literal: "Naoya Takeishi"
  - literal: "Takehisa Yairi"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26748"

# Custom fields
paper_id: "2608.26748"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "time-series"
  - "robustness"
  - "generative-adversarial-network"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:11:11Z"
created_at: "2026-08-30T10:11:11Z"
---

# Self-Augmented Diffusion Guidance for Physics-Informed Generation

**Authors**: Akira Osaka, Naoya Takeishi, Takehisa Yairi
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26748](https://arxiv.org/abs/2608.26748)

## Summary

Diffusion models often generate spatiotemporal signals of physical phenomena that appear visually plausible but violate underlying physical laws. To address this, the authors propose a physics-informed diffusion guidance method using self-generated data augmentation conditioned on the degree of physical deviation. By decoupling physical equation evaluation from the diffusion sampling process, the approach avoids costly numerical simulations at every denoising step, improving both physical fidelity and generation speed.

## Key Contributions

- Proposes a physics-informed diffusion guidance approach using self-generated data augmentation to condition generation on physical deviation.
- Decouples the evaluation of governing equations from diffusion training and sampling, eliminating the need to solve expensive numerical simulations at every denoising iteration.
- Demonstrates significant reduction in physical constraint violations compared to standard diffusion models while accelerating sample generation.

## Archivist Review

Applied strict scarcity and novelty filters. The proposed open question is a routine application extension to robotics rather than a fundamental methodological bottleneck in forecasting or physics-informed generation. No concepts or datasets met the strict vault inclusion criteria.

### Rejected Candidates
- [open_question] Physics-Informed Robotics Control Generation (`physics-informed-robotics-control`) - low_impact: Too application-specific and speculative regarding robotic control extension.

## Links

- [Abstract](https://arxiv.org/abs/2608.26748)
- [PDF](https://arxiv.org/pdf/2608.26748)

