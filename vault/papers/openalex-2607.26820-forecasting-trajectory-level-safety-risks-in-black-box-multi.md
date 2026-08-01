---
# CSL-compatible fields
title: "Forecasting Trajectory-Level Safety Risks in Black-Box Multi-Turn Interactions"
author:
  - literal: "Shi Lin"
  - literal: "Peng Qian"
  - literal: "Dinghao Liu"
  - literal: "Renjie Sun"
  - literal: "Sifan Wu"
  - literal: "Dezhang Kong"
  - literal: "Chenpei Wang"
  - literal: "Xun Wang"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.26820"

# Custom fields
paper_id: "2607.26820"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "alignment"
  - "agent"
  - "autonomous-agent"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "recast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-01T07:23:22Z"
created_at: "2026-08-01T07:23:22Z"
---

# Forecasting Trajectory-Level Safety Risks in Black-Box Multi-Turn Interactions

**Authors**: Shi Lin, Peng Qian, Dinghao Liu, Renjie Sun, Sifan Wu, Dezhang Kong, Chenpei Wang, Xun Wang
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.26820](https://arxiv.org/abs/2607.26820)

## Summary

The paper introduces Recast, a trajectory-level safety risk forecasting framework for multi-turn LLM interactions that predicts latent risk evolution and future safety failures proactively. By combining a dual-scale trajectory view with a causal temporal encoder, Recast models compositional risk evolution across short-term dialogue progression and long-term historical context. Experiments across 7 risk categories demonstrate high prediction accuracy with significant lead time before safety violations occur.

## Key Contributions

- Proposes Recast, a safety risk forecasting framework that shifts LLM safeguarding from reactive turn-level detection to trajectory-level risk prediction.
- Employs a dual-scale trajectory view to retrieve risk-relevant evidence from both short-term dialogue progression and long-term historical context.
- Utilizes a causal temporal encoder to model compositional risk evolution and predict future risk emergence turns across 7 risk categories, achieving 88.3% failure prediction with an average lead time of 2.41 turns.

## Open Questions & Future Work

- [[category-aware-risk-forecasting-calibration]]

## Key Concepts

- [[recast]]: A safety risk forecasting framework that predicts latent risk evolution and future safety failures across long-horizon multi-turn LLM interaction trajectories.

## Archivist Review

Applied strict selectivity standards. Approved the core framework concept 'Recast' and its associated open question on category-aware calibration for multi-turn safety forecasting. No datasets met the standalone criteria.

### Approved Concepts
- Recast: Recast introduces the core trajectory-level safety risk forecasting framework for multi-turn LLM interactions, moving beyond reactive turn-level detection.

### Approved Open Questions
- Category-Aware Risk Forecasting Calibration: Important for bridging performance gaps across highly technical or sensitive harm domains where standard temporal forecasting models struggle with high false alarm rates and calibration issues.

## Links

- [Abstract](https://arxiv.org/abs/2607.26820)
- [PDF](https://arxiv.org/pdf/2607.26820)

