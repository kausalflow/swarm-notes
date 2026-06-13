---
# CSL-compatible fields
title: "Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics"
author:
  - literal: "Sam Gijsen"
  - literal: "Michał Łukomski"
  - literal: "Marc-André Schulz"
  - literal: "Kerstin Ritter"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.11833"

# Custom fields
paper_id: "2606.11833"
paper_source: "openalex"
domain: "biology"
tags:
  - "diffusion-model"
  - "transformer"
  - "language-model"
  - "time-series"
  - "multimodal"
  - "zero-shot-learning"
  - "in-context-learning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "in-context-generative-prior-conditioning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:17:05Z"
created_at: "2026-06-13T08:17:05Z"
---

# Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics

**Authors**: Sam Gijsen, Michał Łukomski, Marc-André Schulz, Kerstin Ritter
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.11833](https://arxiv.org/abs/2606.11833)

## Summary

This paper presents a diffusion transformer architecture for generating realistic whole-cortex fMRI brain dynamics conditioned on compositional language and optional spatial priors. Unlike existing models restricted to categorical conditioning, this approach achieves zero-shot generation for unseen cognitive tasks by leveraging in-context conditioning. Experiments demonstrate that the model successfully recovers region-specific activation patterns, offering a path toward counterfactual neuroscience and in-silico experiment design. The proposed framework significantly extends the capability of generative models to handle compositional, out-of-distribution neural data.

## Key Contributions

- Introduces the first generative model of whole-cortex fMRI dynamics capable of zero-shot generation for unseen cognitive tasks.
- Demonstrates that compositional language conditioning recovers region-specific recruitment and spatial activation patterns without prior exposure to the specific task.
- Shows that spatial priors complement linguistic conditioning, improving performance in task regions where language alone is insufficient.

## Open Questions & Future Work

- [[compositional-ood-dynamics-generalization-limits]]

## Key Concepts

- [[in-context-generative-prior-conditioning]]: A technique for generating time series by conditioning generative models on compositional metadata, such as natural language or spatial priors, provided as in-context inputs.

## Archivist Review

The paper's core contribution is a method for guiding generative models via compositional, in-context metadata, which I have generalized as 'In-Context Generative Prior Conditioning'. I also defined an open question concerning the fundamental limitations of OOD compositional generalization for dynamical systems, which is a significant research challenge. No datasets were approved as they were not specific or central enough to be reusable benchmarks.

### Approved Concepts
- In-Context Generative Prior Conditioning: Enables zero-shot generation of complex dynamics for unseen conditions by using flexible, compositional metadata rather than rigid categorical labels.

### Approved Open Questions
- Compositional OOD Dynamics Generalization: This is a central bottleneck for flexible in-silico scientific design, where researchers need to test novel, non-existent experimental scenarios without new data.

### Rejected Candidates
- [concept] In-Context Priors for Brain Dynamics (`in-context-priors-for-brain-dynamics`) - duplicate_existing: Redundant with 'in-context-generative-prior-conditioning'; the latter is more general and domain-agnostic.

## Links

- [Abstract](https://arxiv.org/abs/2606.11833)
- [PDF](https://arxiv.org/pdf/2606.11833)

