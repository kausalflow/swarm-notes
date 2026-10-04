---
# CSL-compatible fields
title: "Grounding Large Language Models in DSGE Simulators for Policy Generation and Forecasting"
author:
  - literal: "Aditya Dubey"
  - literal: "Namah Gupta"
  - literal: "Vinti Agarwal"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01128"

# Custom fields
paper_id: "2610.01128"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "instruction-tuning"
  - "reinforcement-learning"
  - "agent"
  - "autonomous-agent"
  - "planning"
  - "long-context"
  - "forecasting"
  - "evaluation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:49:17Z"
created_at: "2026-10-04T10:49:17Z"
---

# Grounding Large Language Models in DSGE Simulators for Policy Generation and Forecasting

**Authors**: Aditya Dubey, Namah Gupta, Vinti Agarwal
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01128](https://arxiv.org/abs/2610.01128)

## Summary

Large language models often generate plausible-sounding economic policies that lack grounding in underlying economic dynamics. To address this, the authors embed instruction-tuned language models inside six Snowdrop-backed dynamic stochastic general equilibrium (DSGE) simulators to evaluate policies based on simulated economic consequences and rewards. They examine long-horizon credit assignment challenges by comparing PPO (utilizing value functions and generalized advantage estimation) with a critic-free GRPO baseline across rolling-horizon simulations, historical shocks, and cross-simulator transfer settings.

## Key Contributions

- Proposes grounding large language models inside dynamic stochastic general equilibrium (DSGE) simulators to evaluate economic policy actions by their simulated consequences rather than fluent language alone.
- Implements a common Python interface supporting repeated rollouts, persistent shocks, state cloning, and rolling-horizon simulation across six Snowdrop-backed DSGE simulators.
- Compares PPO (using learned value functions for credit assignment in long-horizon rollout settings) against a critic-free GRPO baseline to study delayed economic reward propagation.

## Open Questions & Future Work

- [[long-horizon-credit-assignment-dsge]]

## Archivist Review

Evaluated the paper connecting LLMs with DSGE simulators. The core contributions involve applying PPO and GRPO to economic simulation rollouts, which represents an interesting application domain (macroeconomic policy simulation) rather than introducing a standalone vault concept. The open question was carefully evaluated against existing vault entries on reinforcement learning credit assignment and found to be too domain-specific/instantiated. Therefore, no concepts or open questions qualified for permanent vault notes.

### Approved Open Questions
- Long-Horizon Credit Assignment in Economic Simulators: Long-horizon credit assignment is a fundamental bottleneck in applying reinforcement learning to language agents in dynamic environments with delayed feedback, making robust algorithmic comparisons and improvements crucial.

### Rejected Candidates
- [open_question] Long-Horizon Credit Assignment in Economic Simulators (`long-horizon-credit-assignment-dsge`) - not_novel: The open question explores credit assignment in LLM-based policy generation within simulators, which is a specific instantiation of reinforcement learning credit assignment rather than a novel foundational open question distinct from existing credit assignment challenges.

## Links

- [Abstract](https://arxiv.org/abs/2610.01128)
- [PDF](https://arxiv.org/pdf/2610.01128)

