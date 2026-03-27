---
# CSL-compatible fields
title: "On Neural Scaling Laws for Weather Emulation through Continual Training"
author:
  - literal: "Shashank Subramanian"
  - literal: "Alexander Kiefer"
  - literal: "Arnur Nigmetov"
  - literal: "Amir Gholami"
  - literal: "Dmitriy Morozov"
  - literal: "Michael W. Mahoney"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25687"

# Custom fields
paper_id: "2603.25687"
paper_source: "arxiv"
domain: "time-series"
tags:
  - "scaling-law"
  - "time-series"
  - "forecasting"
  - "vision-transformer"
  - "continual-learning"
  - "evaluation"
  - "efficient-transformer"
architectures:
  - "vit"
datasets:
  - "Weather (Implicitly, based on domain)"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T09:10:10Z"
created_at: "2026-03-27T09:10:10Z"
---

# On Neural Scaling Laws for Weather Emulation through Continual Training

**Authors**: Shashank Subramanian, Alexander Kiefer, Arnur Nigmetov, Amir Gholami, Dmitriy Morozov, Michael W. Mahoney
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25687](https://arxiv.org/abs/2603.25687)

## Summary

This paper investigates the application of neural scaling laws, a cornerstone of NLP and Vision foundation models, to the domain of weather emulation using a scalable Swin Transformer architecture. The authors employ a continual training strategy featuring constant learning rates and periodic cooldowns, demonstrating that this minimalist approach results in predictable scaling trends that surpass standard cosine learning rate schedules. Furthermore, the cooldown phases are shown to enhance downstream performance, specifically enabling better multi-step forecasts over longer horizons and sharper predictions through spectral loss tuning. By constructing IsoFLOP curves across varied scales, the research identifies compute-optimal training regimes, suggesting that scaling laws are vital for resource planning in Scientific Machine Learning.

## Key Contributions

- Demonstrated that a minimalist Swin Transformer architecture trained with continual training (constant LR with periodic cooldowns) follows predictable neural scaling laws for weather emulation.
- Showed that periodic cooldown phases in training can be leveraged to improve multi-step rollout accuracy and spectral fidelity (sharper predictions) via spectral loss adjustments.
- Systematically constructed IsoFLOP curves across various model/dataset sizes to identify compute-optimal training regimes for weather forecasting models.
- Provided evidence that neural scaling analysis serves as a critical diagnostic tool for efficient resource allocation in Scientific ML research.

## Limitations

The study uses a Swin Transformer backbone, which is not the state-of-the-art for time-series sequence modeling compared to more specialized architectures like Mamba or RNNs, although this was chosen for its simplicity and scalability for scaling law analysis.

## Open Questions & Future Work

- [[scaling-other-dimensions-in-weather-emulation]]
- [[probabilistic-vs-deterministic-scaling]]
- [[scaling-alternative-architectures]]
- [[cross-domain-scaling-validation]]

## Key Concepts

- [IsoFLOP Curves](../concepts/isoflop-curves.md): Curves that illustrate the relationship between model performance and computational scale (FLOPs) for a fixed target performance level across different training configurations.

## Datasets

- [Weather (Implicitly, based on domain)](../datasets/weather-implicitly-based-on-domain.md)

## Limitations

The study uses a Swin Transformer backbone, which is not the state-of-the-art for time-series sequence modeling compared to more specialized architectures like Mamba or RNNs, although this was chosen for its simplicity and scalability for scaling law analysis.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25687)
- [PDF](https://arxiv.org/pdf/2603.25687)

