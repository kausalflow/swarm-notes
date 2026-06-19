---
# CSL-compatible fields
title: "ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation"
author:
  - literal: "Tianyi Lu"
  - literal: "Hui Zhang"
  - literal: "Zijie Diao"
  - literal: "Junke Wang"
  - literal: "Shengqi Xu"
  - literal: "Xingyao Lin"
  - literal: "Guojin Zhong"
  - literal: "Z Zhenyu Ye"
  - literal: "Peng Wang"
  - literal: "Zuxuan Wu"
  - literal: "Yi Jiang"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17937"

# Custom fields
paper_id: "2606.17937"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "vision-language-model"
  - "vlm"
  - "llm"
  - "chain-of-thought"
  - "mixture-of-experts"
  - "robotics"
  - "agent"
  - "planning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "thinkingvla"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:25:56Z"
created_at: "2026-06-19T09:25:56Z"
---

# ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation

**Authors**: Tianyi Lu, Hui Zhang, Zijie Diao, Junke Wang, Shengqi Xu, Xingyao Lin, Guojin Zhong, Z Zhenyu Ye, Peng Wang, Zuxuan Wu, Yi Jiang
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17937](https://arxiv.org/abs/2606.17937)

## Summary

ThinkingVLA addresses the limitations of standard VLA models in long-horizon robotic tasks by introducing explicit, interleaved reasoning. The model performs forward Chain-of-Thought (CoT) reasoning to predict subgoal visual states, which then serve as targets for an inverse CoT that reasons about spatial relationships and action intent. This decomposition is unified within a Mixture-of-Transformers architecture, allowing for coherent text-visual reasoning and improved action generation.

## Key Contributions

- Introduces ThinkingVLA, a generative model that decomposes manipulation planning into forward CoT-based visual forecasting and inverse dynamics grounding.
- Employs a unified Mixture-of-Transformers architecture that interleaves textual and visual reasoning in a single generation sequence.
- Achieves superior performance on long-horizon robotic manipulation tasks in both simulation and real-world benchmarks compared to state-of-the-art VLA models.

## Key Concepts

- [[thinkingvla]]: A unified VLA model that interleaves textual and visual reasoning through forward subgoal CoT and inverse dynamics prediction.

## Archivist Review

I have approved 'ThinkingVLA' as it captures a distinct, novel approach to planning in robotic vision-language models by interleaving visual forecasting and inverse dynamics. I rejected the 'Mixture-of-Transformers' as it is a subcomponent implementation detail that does not warrant a standalone note given the overarching model concept already covers the contribution. No datasets or open questions were proposed, so none were approved.

### Approved Concepts
- ThinkingVLA: It proposes a novel decomposition of robotic manipulation into forward subgoal prediction and inverse dynamics grounding via interleaved textual-visual reasoning.

### Rejected Candidates
- [concept] Mixture-of-Transformers Architecture (`mixture-of-transformers`) - subcomponent_of_broader_mechanism: This is a specific architectural choice for implementation rather than a central conceptual contribution of the paper.

## Links

- [Abstract](https://arxiv.org/abs/2606.17937)
- [PDF](https://arxiv.org/pdf/2606.17937)

