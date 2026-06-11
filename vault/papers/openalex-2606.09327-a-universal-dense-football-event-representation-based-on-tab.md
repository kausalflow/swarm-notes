---
# CSL-compatible fields
title: "A Universal Dense Football Event Representation Based on TabTransformer"
author:
  - literal: "Weiran Yang"
  - literal: "Daniel Memmert"
  - literal: "Maximilian Klemp-Weins"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09327"

# Custom fields
paper_id: "2606.09327"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "attention-mechanism"
  - "embedding"
  - "pre-training"
  - "evaluation"
architectures:
  - "transformer"
datasets:
  []
concept_slugs:
  - "universal-dense-football-event-representation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:08:22Z"
created_at: "2026-06-11T09:08:22Z"
---

# A Universal Dense Football Event Representation Based on TabTransformer

**Authors**: Weiran Yang, Daniel Memmert, Maximilian Klemp-Weins
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09327](https://arxiv.org/abs/2606.09327)

## Summary

This paper presents a Transformer-based approach to generate dense, semantically rich representations of football event data. By moving beyond traditional one-hot or ordinal encoding, the model learns latent interdependencies between categorical features like action types and outcomes through a pretraining phase. The resulting embeddings significantly improve performance and probability calibration on downstream analytical tasks, including action value estimation and tactical play style recognition.

## Key Contributions

- Introduces a Transformer-based model to learn latent dependencies among heterogeneous categorical football event features.
- Replaces standard one-hot/ordinal encoding with learned dense embedding vectors that capture sport-specific action semantics during pretraining.
- Demonstrates superior probability calibration (Brier score) on downstream tasks like action value estimation and play style recognition compared to baselines.

## Open Questions & Future Work

- [[improving-within-role-entity-discriminability]]

## Key Concepts

- [[universal-dense-football-event-representation]]: A Transformer-based method for learning semantically rich, dense representations of heterogeneous football event data via categorical embedding pretraining.

## Archivist Review

I approved the concept for universal event representation because it effectively generalizes TabTransformer-based approaches to sports domains. The open question was narrowed to be more generally applicable across domains beyond just football, moving it away from local implementation details. I rejected the second open question as it was too generic.

### Approved Concepts
- Universal Dense Football Event Representation: It provides a novel way to encode high-dimensional, heterogeneous sports event data into semantically meaningful dense vectors using self-attention.

### Approved Open Questions
- Improving Within-Role Entity Discriminability: Improving the granularity of agent style representations is essential for practical analytical and scouting applications, where distinguishing between entities with similar roles is critical.

### Rejected Candidates
- [open_question] Advanced Pretraining Objectives for Events (`advanced-pretraining-objectives-football-events`) - generic: This is a broad, generic research direction that lacks the specificity required for a standalone vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2606.09327)
- [PDF](https://arxiv.org/pdf/2606.09327)

