---
# CSL-compatible fields
title: "Disagree to Accelerate: Closing the Loop on Diffusion Feature Forecasts"
author:
  - literal: "Yanchao Li"
  - literal: "Jiaqing Xie"
  - literal: "Ben Gao"
  - literal: "Wanhao Liu"
  - literal: "Yanbo Wang"
  - literal: "T. Y. Tsui"
  - literal: "Jinfei Liu"
  - literal: "Yuqiang Li"
  - literal: "Tianfan Fu"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01740"

# Custom fields
paper_id: "2608.01740"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "stable-diffusion"
  - "generative-adversarial-network"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "racer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:31:52Z"
created_at: "2026-08-06T07:31:52Z"
---

# Disagree to Accelerate: Closing the Loop on Diffusion Feature Forecasts

**Authors**: Yanchao Li, Jiaqing Xie, Ben Gao, Wanhao Liu, Yanbo Wang, T. Y. Tsui, Jinfei Liu, Yuqiang Li, Tianfan Fu
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01740](https://arxiv.org/abs/2608.01740)

## Summary

Training-free feature forecasting in diffusion models often suffers under aggressive acceleration due to fixed-trust open-loop caching where forecast errors vary sharply. This paper introduces RACER, a closed-loop controller that uses forecast disagreement as a cheap runtime signal to shrink uncertain predictions toward computed features and dynamically adapt skipping schedules. Extensive experiments across SD3.5-Large, FLUX.1-dev, Wan2.1-14B, and HunyuanVideo show superior generation quality and sampling speed at equivalent evaluations.

## Key Contributions

- Introduces RACER, a training-free closed-loop controller that measures forecast disagreement to dynamically control trust and execution during diffusion feature forecasting.
- Achieves improved generation quality over the strongest open-loop baselines across SD3.5-Large, FLUX.1-dev, Wan2.1-14B, and HunyuanVideo at equal function evaluations on DrawBench, VBench, and COCO.
- Demonstrates theoretical validity by deriving a deterministic error bound for forecast shrinkage and empirical generalization across different forecasting designs like Taylor bases.

## Open Questions & Future Work

- [[reliable-diffusion-forecasting-control]]

## Key Concepts

- [[racer]]: A training-free closed-loop controller that dynamically adjusts trust and execution in diffusion feature forecasting based on forecast disagreement.

## Archivist Review

Approved RACER as a reusable closed-loop control mechanism for feature forecasting and acceleration. Approved the open question regarding reliable control and trust calibration in diffusion feature forecasting. No datasets were approved as DrawBench, VBench, and COCO are standard benchmarks.

### Approved Concepts
- RACER: RACER is the core proposed method (a training-free closed-loop controller for diffusion feature forecasting acceleration) that directly addresses the paper's central premise of closing the loop on diffusion feature forecasts.

### Approved Open Questions
- Reliable Control in Diffusion Forecasting: Crucial for developing robust, training-free acceleration frameworks that maintain generation fidelity under extreme compute budgets.

## Links

- [Abstract](https://arxiv.org/abs/2608.01740)
- [PDF](https://arxiv.org/pdf/2608.01740)

