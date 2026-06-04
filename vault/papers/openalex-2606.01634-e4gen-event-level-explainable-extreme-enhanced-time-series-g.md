---
# CSL-compatible fields
title: "E4GEN: Event-level Explainable Extreme-Enhanced Time-series Generation"
author:
  - literal: "Lin Jiang"
  - literal: "Dahai Yu"
  - literal: "Ximiao Li"
  - literal: "Guang Wang"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.01634"

# Custom fields
paper_id: "2606.01634"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "diffusion-model"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "e4gen-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:43:16Z"
created_at: "2026-06-04T08:43:16Z"
---

# E4GEN: Event-level Explainable Extreme-Enhanced Time-series Generation

**Authors**: Lin Jiang, Dahai Yu, Ximiao Li, Guang Wang
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.01634](https://arxiv.org/abs/2606.01634)

## Summary

E4GEN is an explainable diffusion framework designed to address the challenge of accurately generating extreme events in time-series data while maintaining overall distributional fidelity. It employs a modular architecture comprising an E-Activator for adaptive control, an E-Predictor for inferring latent extreme events, and an E-Control network for targeted signal injection. By effectively decoupling extreme-event generation from normal temporal dynamics, E4GEN provides systematic control over high-impact, rare observations without degrading the quality of regular trends. Evaluation on six benchmark datasets demonstrates significant improvements in extreme-event fidelity and downstream utility compared to existing generative approaches.

## Key Contributions

- E4GEN achieves superior overall and extreme-event fidelity compared to state-of-the-art baselines across 17 metrics and 6 datasets.
- Introduces E-Activator to decouple extreme-event control signals from trend and seasonality components during diffusion denoising.
- Implements a Self-Driven Semantic Prediction and Data-Conditioned Training mechanism that enables extreme-event generation even in the absence of explicit training labels.

## Open Questions & Future Work

- [[extreme-event-generative-fidelity-tradeoff]]

## Key Concepts

- [[e4gen-framework]]: An explainable diffusion-based time-series generation framework that enables targeted control over extreme event synthesis without distorting overall distribution fidelity.

## Archivist Review

I approved the E4GEN framework as it provides a novel approach to the critical task of generating extreme time-series events via diffusion. I also defined an open question regarding the tradeoff between extreme event fidelity and overall distribution accuracy, which is a major, unresolved bottleneck in time-series generation. Sub-components were rejected as they are best discussed within the context of the overarching framework.

### Approved Concepts
- E4GEN Framework: The framework uniquely addresses the decoupling of extreme value synthesis from underlying trends and seasonality in diffusion models, a persistent challenge in time-series generation.

### Approved Open Questions
- Extreme Event Generative Fidelity Tradeoff: This is a fundamental limitation in generative modeling for time-series, as current metrics often favor average-case performance at the expense of tail-risk and anomaly realism.

### Rejected Candidates
- [concept] E-Activator (`e-activator`) - subcomponent_of_broader_mechanism: This is a sub-component of the broader E4GEN framework and lacks sufficient independent utility outside of the proposed architecture.
- [concept] E-Predictor (`e-predictor`) - subcomponent_of_broader_mechanism: This is a sub-component of the broader E4GEN framework and does not qualify for a standalone note.
- [concept] E-Control (`e-control`) - subcomponent_of_broader_mechanism: This is a specific implementation detail for controlling signal injection and is best captured within the main framework note.

## Links

- [Abstract](https://arxiv.org/abs/2606.01634)
- [PDF](https://arxiv.org/pdf/2606.01634)

