---
# CSL-compatible fields
title: "MoTE: Mixture of Task Experts for Multi-Task Video Understanding"
author:
  - literal: "Muhammad Asad Ali"
  - literal: "Umar Khan"
  - literal: "Nadia Robertini"
  - literal: "Didier Stricker"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.24763"

# Custom fields
paper_id: "2608.24763"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "mixture-of-experts"
  - "decoder-only"
  - "transformer"
  - "llm"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "mixture-of-task-experts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T17:01:02Z"
created_at: "2026-08-28T17:01:02Z"
---

# MoTE: Mixture of Task Experts for Multi-Task Video Understanding

**Authors**: Muhammad Asad Ali, Umar Khan, Nadia Robertini, Didier Stricker
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.24763](https://arxiv.org/abs/2608.24763)

## Summary

Procedural video-language models often suffer from task entanglement when dense transformer decoders share feed-forward networks across heterogeneous tasks like action recognition, forecasting, and procedure prediction. To address this, the authors propose MoTE (Mixture of Task Experts), which converts LLM feed-forward networks into task-specific experts via sample-level task routing while maintaining a shared multimodal backbone. Evaluated on five COIN benchmarks, the resulting VideoLLM-MoTE model outperforms dense baselines and sparse token-level routing controls while maintaining compute efficiency.

## Key Contributions

- Proposes MoTE (Mixture of Task Experts), a decoder architecture that converts LLM feed-forward networks into task-specific experts with a shared multimodal backbone.
- Implements sample-level task routing where each example follows one task route, keeping computation independent of the total number of stored task experts.
- Evaluates VideoLLM-MoTE on five COIN benchmarks, outperforming dense all-expert activation and learned sparse-routing controls while activating ~2B parameters per sample.

## Open Questions & Future Work

- [[flexible-hierarchical-compositional-routing]]

## Key Concepts

- [[mixture-of-task-experts]]: A decoder architecture that converts LLM feed-forward networks into task-specific experts using sample-level task routes.

## Archivist Review

Applied strict selectivity standards. Approved the core methodological concept 'Mixture of Task Experts (MoTE)' and the corresponding open question on flexible compositional routing, while rejecting routine dataset tags and paper-local evaluations.

### Approved Concepts
- Mixture of Task Experts (MoTE): Introduces sample-level task routing for multi-task video-language decoding to prevent task entanglement.

### Approved Open Questions
- Flexible and Compositional Task Routing: Crucial for extending modular mixtures of task experts from clean, isolated academic benchmarks to real-world, open-ended conversational scenarios involving complex, multi-intent user instructions.

## Links

- [Abstract](https://arxiv.org/abs/2608.24763)
- [PDF](https://arxiv.org/pdf/2608.24763)

