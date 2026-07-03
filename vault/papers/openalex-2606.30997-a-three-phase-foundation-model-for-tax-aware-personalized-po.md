---
# CSL-compatible fields
title: "A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management"
author:
  - literal: "Ramin Pishehvar"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.30997"

# Custom fields
paper_id: "2606.30997"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "rlhf"
  - "reinforcement-learning"
  - "mixture-of-experts"
  - "moe"
  - "lora"
  - "time-series"
  - "fine-tuning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "objective-conditioned-mixture-of-experts-actor-critic"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:55:42Z"
created_at: "2026-07-03T07:55:42Z"
---

# A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management

**Authors**: Ramin Pishehvar
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.30997](https://arxiv.org/abs/2606.30997)

## Summary

This paper proposes a three-phase deep reinforcement learning framework for portfolio management designed to overcome ticker dependency, monolithic optimization, and static user modeling. The system utilizes a self-supervised cross-asset encoder integrated with a time series foundation model (Chronos), an objective-conditioned Mixture-of-Experts actor-critic to manage multiple investment goals, and an inference-time personalization layer via LoRA. By inferring objectives directly from transaction history and using a learned router, the model provides a scalable, personalized solution for diverse investment strategies including tax-loss harvesting.

## Key Contributions

- Introduces a ticker-identity-free cross-asset encoder that generalizes to new assets using a 50-dimensional metadata vector without retraining.
- Implements an objective-conditioned MoE actor-critic that resolves cross-objective gradient conflict by routing tasks to goal-specific expert heads (momentum, growth, defensive, tax-aware).
- Enables inference-time personalization using a 76-parameter LoRA module to adapt to individual brokerage transaction histories.
- Pioneers the fusion of existing time series foundation models (e.g., Chronos) into a portfolio management RL pipeline.

## Open Questions & Future Work

- [[empirical-validation-lora-personalization]]
- [[moe-multi-window-robustness]]

## Key Concepts

- [[objective-conditioned-mixture-of-experts-actor-critic]]: A policy optimization architecture that uses a router to distribute tasks among specialized expert heads based on user objectives and market context.

## Archivist Review

I approved the Objective-Conditioned MoE Actor-Critic as it provides a valuable architectural pattern for multi-objective RL. I rejected the 'Three-Phase' concept as it is a paper-specific project workflow rather than a reusable scientific concept. The open questions regarding LoRA personalization and MoE horizon robustness were approved as they address substantial, recurring challenges in financial and multi-task RL.

### Approved Concepts
- Objective-Conditioned Mixture-of-Experts Actor-Critic: It enables a single RL policy to handle conflicting investment goals by dynamically routing tasks to specialized experts, eliminating gradient conflict.

### Approved Open Questions
- Empirical validation of LoRA personalization: This addresses a core bottleneck in bridging the gap between aggregate foundation model pre-training and individualized financial decision-making.
- MoE multi-window robustness: Addressing the degradation of expert-based policies over varying investment horizons is essential for creating reliable, retail-scale portfolio managers.

### Rejected Candidates
- [concept] Three-Phase Foundation Model for Portfolio Management (`three-phase-foundation-model-for-portfolio-management`) - subcomponent_of_broader_mechanism: This represents a broad system-level workflow (three-phase training) rather than a specific, reusable architectural or algorithmic mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2606.30997)
- [PDF](https://arxiv.org/pdf/2606.30997)

