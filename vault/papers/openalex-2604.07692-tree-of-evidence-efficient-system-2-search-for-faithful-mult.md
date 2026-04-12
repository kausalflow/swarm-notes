---
# CSL-compatible fields
title: "Tree-of-Evidence: Efficient \"System 2\" Search for Faithful Multimodal Grounding"
author:
  - literal: "Micky C. Nnamdi"
  - literal: "Benoit L. Marteau"
  - literal: "Yishan Zhong"
  - literal: "J. Ben Tamo"
  - literal: "MAY WANG"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.07692"

# Custom fields
paper_id: "2604.07692"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "llm"
  - "interpretability"
  - "explainability"
  - "reasoning"
architectures:
  []
datasets:
  - "MIMIC-IV"
  - "eICU"
concept_slugs:
  - "tree-of-evidence-toe"
dataset_slugs:
  - "mimic-iv"
  - "eicu"
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:20:58Z"
created_at: "2026-04-12T06:20:58Z"
---

# Tree-of-Evidence: Efficient "System 2" Search for Faithful Multimodal Grounding

**Authors**: Micky C. Nnamdi, Benoit L. Marteau, Yishan Zhong, J. Ben Tamo, MAY WANG
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.07692](https://arxiv.org/abs/2604.07692)

## Summary

Tree-of-Evidence (ToE) addresses the opacity of Large Multimodal Models by reframing interpretability as a discrete optimization problem rather than relying on soft attention weights. By employing lightweight Evidence Bottlenecks and a beam search strategy, ToE identifies the minimal set of data units—such as vital-sign segments or report text—necessary to replicate a model's prediction. The method demonstrates high performance across six diverse tasks, offering a faithful and auditable mechanism for understanding complex, multimodal decision-making.

## Key Contributions

- Introduces Tree-of-Evidence (ToE), a beam search-based interpretability framework that optimizes for compact, faithful evidence subsets.
- Demonstrates that ToE retains over 98% of full-model AUROC using only five discrete evidence units across diverse clinical and fault-detection tasks.
- Outperforms existing interpretability methods in decision agreement and probability fidelity error under sparse evidence constraints.

## Open Questions & Future Work

- [[discrete-interpretability-for-early-fusion-models]]

## Key Concepts

- [[tree-of-evidence-toe]]: An inference-time search algorithm that identifies minimal, discrete evidence sets from heterogeneous data streams to explain LMM predictions.

## Archivist Review

Approved Tree-of-Evidence as a distinct interpretability concept and two foundational clinical datasets. The open question was reframed to improve clarity regarding the challenge of adapting discrete interpretability to early-fusion architectures. Other candidates were rejected to maintain the required scarcity of the vault.

### Approved Concepts
- Tree-of-Evidence (ToE): It frames interpretability as a discrete optimization search problem rather than relying on standard soft attention-based saliency methods, providing a more faithful audit of LMM decision-making.

### Approved Open Questions
- Discrete Interpretability for Early-Fusion Models: Defining the limits of discrete interpretability methods relative to fusion architecture is critical for scaling auditing techniques to modern, highly integrated multimodal LLMs.

### Rejected Candidates
- [open_question] Interpretability for Early-Fusion Models (`multimodal-architecture-fusion-interpretability`) - other: Renamed to be more descriptive and avoid generic phrasing.

## Datasets

- [[mimic-iv]]
- [[eicu]]

## Links

- [Abstract](https://arxiv.org/abs/2604.07692)
- [PDF](https://arxiv.org/pdf/2604.07692)

