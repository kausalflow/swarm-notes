---
# CSL-compatible fields
title: "Not All Actions Are Equal: Rethinking Conditioning for Dexterous World Model"
author:
  - literal: "Zizhao Yuan"
  - literal: "Zhengtu Liang"
  - literal: "Taowen Wang"
  - literal: "Qiwei Liang"
  - literal: "Yichi Wang"
  - literal: "Yunheng Wang"
  - literal: "Y D Fang"
  - literal: "Lusong Li"
  - literal: "Zecui Zeng"
  - literal: "Renjing Xu"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.27325"

# Custom fields
paper_id: "2606.27325"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "robotics"
  - "autonomous-agent"
  - "planning"
architectures:
  []
datasets:
  - "egodex"
  - "egoverse"
concept_slugs:
  - "structured-action-tokenization"
dataset_slugs:
  - "egodex"
  - "egoverse"
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:17:17Z"
created_at: "2026-06-28T08:17:17Z"
---

# Not All Actions Are Equal: Rethinking Conditioning for Dexterous World Model

**Authors**: Zizhao Yuan, Zhengtu Liang, Taowen Wang, Qiwei Liang, Yichi Wang, Yunheng Wang, Y D Fang, Lusong Li, Zecui Zeng, Renjing Xu
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.27325](https://arxiv.org/abs/2606.27325)

## Summary

DexAC-WM addresses the challenge of action conditioning in high-DoF dexterous world models, where traditional monolithic compression fails to capture heterogeneous action signals. By implementing structured action tokenization alongside local refinement and global modulation, the model better aligns complex actions with visual dynamics. Furthermore, the inclusion of a semantic branch provides essential object-scene priors, significantly improving action-conditioned video prediction realism. Experiments on EgoDex and EgoVerse confirm that this approach achieves superior visual-temporal fidelity and action-following consistency.

## Key Contributions

- Introduces DexAC-WM, a world model architecture that replaces monolithic action compression with structured, dimension-level action tokenization.
- Implements a local refinement and global modulation mechanism to align heterogeneous high-DoF actions with visual dynamics.
- Incorporates a semantic branch providing object-scene priors to improve visual-temporal realism and high-level semantic grounding in video prediction.
- Demonstrates significant improvements in FID, FVD, and PCK metrics on EgoDex and EgoVerse benchmarks compared to existing action-conditioned approaches.

## Open Questions & Future Work

- [[occlusion-dexterous-world-models]]

## Key Concepts

- [[structured-action-tokenization]]: A conditioning framework that replaces monolithic action sequence compression with structured, dimension-level tokenization to preserve semantic signal heterogeneity.

## Archivist Review

Approved the structured action tokenization concept as it provides a distinct, reusable architectural methodology for high-DoF action conditioning that addresses the optimization imbalance of monolithic approaches. Occlusion in dexterous world models was retained as a substantial research bottleneck that extends beyond this specific paper. Other candidates were rejected for being model-specific implementations or overly generic boilerplate objectives.

### Approved Concepts
- Structured Action Tokenization: It shifts the paradigm from monolithic action compression to dimension-level semantics, which is a reusable methodology for high-DoF world models.

### Approved Open Questions
- Resolving Occlusion in Dexterous Modeling: Occlusion handling is a fundamental requirement for generalizing world models to real-world robotic tasks beyond controlled laboratory datasets.

### Rejected Candidates
- [concept] DexAC-WM (`dexac-wm`) - subcomponent_of_broader_mechanism: This is the specific model name; the underlying reusable mechanism is better captured as structured action tokenization.
- [open_question] Training Efficiency and Scalability (`scalable-efficient-world-model-training`) - low_impact: This is a generic, boilerplate research goal common to all large model papers.

## Datasets

- [[egodex]]
- [[egoverse]]

## Links

- [Abstract](https://arxiv.org/abs/2606.27325)
- [PDF](https://arxiv.org/pdf/2606.27325)

