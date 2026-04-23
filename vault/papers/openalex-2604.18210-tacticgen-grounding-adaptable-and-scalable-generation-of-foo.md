---
# CSL-compatible fields
title: "TacticGen: Grounding Adaptable and Scalable Generation of Football Tactics"
author:
  - literal: "Sheng Xu"
  - literal: "Guiliang Liu"
  - literal: "Tarak Kharrat"
  - literal: "Yudong Luo"
  - literal: "Mohamed Aloulou"
  - literal: "Javier López Peña"
  - literal: "Konstantin Sofeikov"
  - literal: "Adam Reid"
  - literal: "Paul Roberts"
  - literal: "Steven Spencer"
  - literal: "Joe Carnall"
  - literal: "Ian McHale"
  - literal: "Oliver Schulte"
  - literal: "Hongyuan Zha"
  - literal: "Wei‐Shi Zheng"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18210"

# Custom fields
paper_id: "2604.18210"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "transformer"
  - "diffusion-model"
  - "multimodal"
  - "multi-agent"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tacticgen"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:57:25Z"
created_at: "2026-04-23T06:57:25Z"
---

# TacticGen: Grounding Adaptable and Scalable Generation of Football Tactics

**Authors**: Sheng Xu, Guiliang Liu, Tarak Kharrat, Yudong Luo, Mohamed Aloulou, Javier López Peña, Konstantin Sofeikov, Adam Reid, Paul Roberts, Steven Spencer, Joe Carnall, Ian McHale, Oliver Schulte, Hongyuan Zha, Wei‐Shi Zheng
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18210](https://arxiv.org/abs/2604.18210)

## Summary

TacticGen addresses the challenge of tactical design in association football by modeling tactics as multi-agent spatio-temporal sequences. The model utilizes a diffusion transformer architecture featuring agent-wise self-attention and context-aware cross-attention to capture complex cooperative and competitive dynamics. By incorporating a classifier guidance mechanism, TacticGen enables the generation of strategically adaptable football tactics that can be constrained by rules, natural language, or neural objective models. Empirical evaluations and expert qualitative assessments confirm the model's effectiveness in producing realistic and strategically valuable tactical planning.

## Key Contributions

- Introduces TacticGen, a multi-agent diffusion transformer capable of modeling football tactics as sequences of player-ball interactions.
- Implements a classifier guidance mechanism that enables flexible, inference-time adaptation of generated tactics to specific strategic constraints (rules, language, or models).
- Demonstrates superior precision in player trajectory forecasting on a large-scale proprietary dataset comprising 3.3 million events and 100 million tracking frames.

## Open Questions & Future Work

- [[unified-multi-objective-tactic-adaptation]]

## Key Concepts

- [[tacticgen]]: A generative framework for multi-agent tactical planning that uses a diffusion transformer with classifier guidance to generate goal-conditioned movement sequences.

## Archivist Review

I approved TacticGen as a conceptual framework for goal-conditioned multi-agent tactical generation and the related open question concerning the unification of multi-objective guidance. The paper's contribution lies in the shift from trajectory prediction to strategic planning via diffusion-based guidance, which is a reusable architectural pattern for team sports modeling. I rejected the implicit "dataset" of 3.3 million events as it is a proprietary, unspecified aggregate rather than a distinct, named, and reusable community dataset.

### Approved Concepts
- TacticGen: TacticGen represents a distinct shift from predictive trajectory modeling to generative, goal-conditioned tactical planning in multi-agent sports environments.

### Approved Open Questions
- Unified Multi-Objective Tactic Adaptation: Moving beyond static guidance modules is necessary for deploying generative models as reliable, longitudinal decision support systems in complex multi-agent environments.

## Links

- [Abstract](https://arxiv.org/abs/2604.18210)
- [PDF](https://arxiv.org/pdf/2604.18210)

