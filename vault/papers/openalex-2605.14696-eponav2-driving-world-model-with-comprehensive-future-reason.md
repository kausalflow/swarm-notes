---
# CSL-compatible fields
title: "EponaV2: Driving World Model with Comprehensive Future Reasoning"
author:
  - literal: "Jiawei Xu"
  - literal: "Zhizhou Zhong"
  - literal: "Zhijian Shu"
  - literal: "Mingkai Jia"
  - literal: "Mingxiao Li"
  - literal: "Jia-Wang Bian"
  - literal: "Qian Zhang"
  - literal: "Kaicheng Zhang"
  - literal: "Jin Xie"
  - literal: "Jian Yang"
  - literal: "Wei Yin"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14696"

# Custom fields
paper_id: "2605.14696"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "autonomous-agent"
  - "planning"
  - "reinforcement-learning"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  - "NAVSIM"
concept_slugs:
  - "flow-grpo-post-training"
dataset_slugs:
  - "navsim"
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:31:30Z"
created_at: "2026-05-17T07:31:30Z"
---

# EponaV2: Driving World Model with Comprehensive Future Reasoning

**Authors**: Jiawei Xu, Zhizhou Zhong, Zhijian Shu, Mingkai Jia, Mingxiao Li, Jia-Wang Bian, Qian Zhang, Kaicheng Zhang, Jin Xie, Jian Yang, Wei Yin
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14696](https://arxiv.org/abs/2605.14696)

## Summary

EponaV2 is a perception-free driving world model that moves beyond simple next-frame image forecasting by predicting comprehensive future 3D geometry and semantic representations. This approach enables deeper scene understanding and improved reasoning for trajectory planning. Additionally, the model incorporates a flow matching group relative policy optimization (Flow-GRPO) mechanism, inspired by LLM training, to further optimize planning outputs, achieving state-of-the-art results on the NAVSIM benchmarks.

## Key Contributions

- Proposed EponaV2, a driving world model that enhances scene understanding by forecasting future 3D geometry and semantic maps.
- Introduced a flow matching group relative policy optimization mechanism to improve trajectory planning accuracy.
- Achieved SOTA performance among perception-free models on NAVSIM benchmarks, reaching +1.3 PDMS and +5.5 EPDM improvement.

## Open Questions & Future Work

- [[improving-pseudo-label-accuracy-in-driving-world-models]]

## Key Concepts

- [[flow-grpo-post-training]]: A reinforcement learning technique based on flow matching and group relative policy optimization to refine trajectory planning in world models.

## Archivist Review

The paper introduces a novel optimization mechanism, Flow-GRPO, which successfully adapts LLM training techniques to the domain of autonomous driving trajectory planning. I have approved this concept and the associated NAVSIM benchmark as a key dataset. The open question regarding pseudo-label accuracy is a well-defined, significant bottleneck for self-supervised autonomous driving models that is worthy of long-term tracking.

### Approved Concepts
- Flow-GRPO Post-Training: This is a novel adaptation of reinforcement learning techniques from LLMs for driving trajectory planning.

### Approved Open Questions
- Improving Pseudo-label Accuracy: This is the primary bottleneck identified by the authors for why their perception-free model does not yet outperform SOTA perception-based models, and it represents a core challenge for the broader field of self-supervised autonomous driving.

## Datasets

- [[navsim]]

## Links

- [Abstract](https://arxiv.org/abs/2605.14696)
- [PDF](https://arxiv.org/pdf/2605.14696)

