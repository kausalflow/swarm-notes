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
paper_source: "openalex"
domain: "time-series"
tags:
  - "scaling-law"
  - "time-series"
  - "forecasting"
  - "vision-transformer"
  - "efficient-transformer"
  - "distributed-training"
architectures:
  - "vision-transformer"
datasets:
  []
concept_slugs:
  - "isoflop-curves"
  - "continual-training-with-cooldowns"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:08:10Z"
created_at: "2026-03-29T06:08:10Z"
---

# On Neural Scaling Laws for Weather Emulation through Continual Training

**Authors**: Shashank Subramanian, Alexander Kiefer, Arnur Nigmetov, Amir Gholami, Dmitriy Morozov, Michael W. Mahoney
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25687](https://arxiv.org/abs/2603.25687)

## Summary

This paper investigates the applicability of neural scaling laws, standard in NLP/CV, to Scientific Machine Learning, specifically for weather forecasting emulation. The authors employ a minimal Swin Transformer architecture trained via continual training with constant learning rates and periodic cooldowns, demonstrating that this method yields predictable scaling trends and superior performance over standard schedules. By constructing IsoFLOP curves across various model and dataset sizes, they determine compute-optimal training regimes and show that scaling analysis can guide resource allocation. Furthermore, the cooldown phases are shown to be beneficial for achieving better multi-step rollouts and prediction sharpness through spectral loss adjustments.

## Key Contributions

- Established neural scaling laws for weather emulation models using a minimal Swin Transformer architecture.
- Demonstrated that continual training with constant learning rates and periodic cooldowns outperforms standard cosine learning rate schedules in this setting.
- Showed that cooldown phases can be repurposed to enhance downstream performance, specifically improving multi-step rollouts and prediction sharpness via spectral loss adjustments.
- Constructed IsoFLOP curves to identify compute-optimal training regimes for weather models and showed scaling laws can diagnose resource allocation needs.

## Limitations

The study focuses on a "minimal, scalable, general-purpose Swin Transformer," suggesting the findings might be limited by this specific architecture choice compared to more specialized weather models.

## Open Questions & Future Work

- [[weather-emulator-scaling-saturation-bottleneck]]
- [[probabilistic-weather-scaling-laws]]

## Key Concepts

- [[isoflop-curves]]: Curves that plot model performance against compute budget (FLOPs) while keeping loss constant, used to determine compute-optimal model/data scaling ratios.
- [[continual-training-with-cooldowns]]: A training methodology involving constant learning rates interspersed with periodic \"cooldowns\" used to efficiently train large models for weather emulation.

## Archivist Review

Approved two core concepts: IsoFLOP Curves as a general tool for compute-optimal scaling and Continual Training with Cooldowns as the specific reusable training methodology introduced. Two open questions were approved concerning the saturation limits of current scaling and the necessary extension to probabilistic scaling laws for chaotic systems. Other proposed open questions regarding architecture comparison and hyperparameter scaling were deemed too local or low-impact for permanent vault storage.

### Approved Concepts
- IsoFLOP Curves: These curves are a key deliverable for understanding compute-optimal training regimes in the context of scaling laws.
- Continual Training with Cooldowns: This is the specific, efficient training technique proposed to achieve predictable scaling behavior in the target domain.

### Approved Open Questions
- Saturation bottleneck in extreme scaling: Determining the true bottleneck for performance saturation (data limits vs. overfitting) is crucial for planning future resource allocation and architectural improvements in large-scale Scientific Machine Learning models.
- Scaling laws for probabilistic emulation: Understanding how scaling laws behave under probabilistic objectives is necessary to guide the development of next-generation foundation models for atmospheric science.

### Rejected Candidates
- [open_question] Scaling across different architectures (`weather-scaling-architecture-comparison`) - low_impact: This is a standard comparative experiment (testing different backbones) that is too boilerplate for a permanent open question vault note, despite the domain relevance.
- [open_question] Scaling with internal resolution (`scaling-transformer-patch-size`) - paper_local: This is an investigation of a single hyperparameter's scaling, which is a detail of the primary scaling law study, not a fundamental unresolved bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2603.25687)
- [PDF](https://arxiv.org/pdf/2603.25687)

