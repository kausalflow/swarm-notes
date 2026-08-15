---
# CSL-compatible fields
title: "Autocorrelation effects in a stochastic-process model for solving two-armed bandit problems"
author:
  - literal: "Tomoki Yamagami"
  - literal: "Mikio Hasegawa"
  - literal: "Takatomo Mihana"
  - literal: "Ryoichi Horisaki"
  - literal: "Atsushi Uchida"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2603.05559"

# Custom fields
paper_id: "2603.05559"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "reinforcement-learning"
  - "bandit"
  - "stochastic-process"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-15T05:15:27Z"
created_at: "2026-08-15T05:15:27Z"
---

# Autocorrelation effects in a stochastic-process model for solving two-armed bandit problems

**Authors**: Tomoki Yamagami, Mikio Hasegawa, Takatomo Mihana, Ryoichi Horisaki, Atsushi Uchida
**Date**: 2026-08-13
**Paper ID**: [openalex:2603.05559](https://arxiv.org/abs/2603.05559)

## Summary

This paper investigates the effects of autocorrelation in a stochastic-process model for solving two-armed bandit problems using time series driven by a threshold and a two-valued Markov signal. The authors find an environment-dependent structure where negative autocorrelation is optimal in reward-rich environments (sum of winning probabilities > 1), positive autocorrelation is optimal in reward-poor environments (sum of winning probabilities < 1), and performance is independent of autocorrelation when the sum equals one. These findings bridge physical photonic chaotic dynamics with reinforcement learning decision-making.

## Key Contributions

- Analyzed a stochastic-process model for solving two-armed bandit problems via time series with a threshold and a two-valued Markov signal.
- Revealed an environment-dependent structure showing negative autocorrelation is optimal in reward-rich environments and positive autocorrelation is optimal in reward-poor environments.
- Mathematically clarified that decision performance is independent of autocorrelation when the sum of winning probabilities equals one.

## Open Questions & Future Work

- [[multi-armed-bandit-analytical-treatment]]

## Archivist Review

Applied strict filtering standards. No standalone concepts met reusability requirements as the paper investigates a specific physical-stochastic model for two-armed bandits. The open question regarding multi-armed bandit extensions is standard incremental future work.

### Approved Open Questions

### Rejected Candidates
- [open_question] Analytical Treatment of Multi-Armed Bandits (`multi-armed-bandit-analytical-treatment`) - low_impact: The paper focuses on two-armed bandit problems and general multi-armed extensions are standard future work extensions rather than an immediate standalone methodological gap.

## Links

- [Abstract](https://arxiv.org/abs/2603.05559)
- [PDF](https://arxiv.org/pdf/2603.05559)

