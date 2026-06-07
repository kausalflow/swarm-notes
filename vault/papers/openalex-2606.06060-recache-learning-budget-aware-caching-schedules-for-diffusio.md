---
# CSL-compatible fields
title: "ReCache: Learning Budget-Aware Caching Schedules for Diffusion Models via REINFORCE"
author:
  - literal: "Mishan Aliev"
  - literal: "Eva Neudachina"
  - literal: "Il'ya Bykov"
  - literal: "Aleksandr Oganov"
  - literal: "Kirill Struminsky"
  - literal: "Aibek Alanov"
  - literal: "Denis Rakitin"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06060"

# Custom fields
paper_id: "2606.06060"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "diffusion-model"
  - "reinforcement-learning"
  - "efficient-transformer"
  - "multimodal"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "recache"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:20:55Z"
created_at: "2026-06-07T08:20:55Z"
---

# ReCache: Learning Budget-Aware Caching Schedules for Diffusion Models via REINFORCE

**Authors**: Mishan Aliev, Eva Neudachina, Il'ya Bykov, Aleksandr Oganov, Kirill Struminsky, Aibek Alanov, Denis Rakitin
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06060](https://arxiv.org/abs/2606.06060)

## Summary

ReCache is a novel framework that learns budget-aware caching schedules for diffusion models to accelerate inference while maintaining high generation quality. Unlike heuristic-based scheduling, ReCache allows users to specify a target computational budget, which the learned policy then optimizes for by selecting optimal recomputation steps. By training with policy gradients and leveraging uncached inference as a target, ReCache provides a flexible, data-free approach compatible with existing feature reuse and forecasting mechanisms.

## Key Contributions

- Introduces ReCache, a reinforcement learning-based framework that enables user-controllable budget-aware caching schedules for diffusion models.
- Demonstrates that ReCache optimizes generation quality under fixed compute budgets without requiring labeled data, using policy gradients for training.
- Achieves significant LPIPS reductions of 31% on FLUX and 65% on Wan 2.1 while maintaining or improving generation performance under substantial FLOPs reduction compared to heuristic baselines.

## Open Questions & Future Work

- [[diffusion-caching-limits-transferability]]

## Key Concepts

- [[recache]]: A budget-aware caching schedule learning framework for diffusion models using reinforcement learning to optimize inference quality under computational constraints.

## Archivist Review

I approved the core framework concept 'ReCache' as it establishes a new paradigm for budget-aware schedule learning in iterative generative inference. I also approved the open question regarding the fundamental limits of caching, as it captures a critical bottleneck in diffusion inference optimization that the paper itself acknowledges. The datasets were rejected because the candidates provided are models/architectures, not datasets.

### Approved Concepts
- ReCache: ReCache introduces a budget-aware mechanism for managing recomputation in iterative models, which is a departure from hand-tuned heuristic scheduling.

### Approved Open Questions
- Diffusion Caching Limits and Transferability: As inference latency becomes the primary bottleneck for large-scale generative models, establishing performance ceilings and characterizing the failure modes of caching mechanisms is essential for ongoing optimization research.

### Rejected Candidates
- [dataset] FLUX (`flux`) - other: FLUX is an architecture/model, not a standard static benchmarking dataset.
- [dataset] Wan 2.1 (`wan-2-1`) - other: Wan 2.1 is an architecture/model, not a standard static benchmarking dataset.

## Links

- [Abstract](https://arxiv.org/abs/2606.06060)
- [PDF](https://arxiv.org/pdf/2606.06060)

