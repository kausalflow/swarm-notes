---
# CSL-compatible fields
title: "A Temporal Knowledge Graph for Music Festival Lineup Forecasting"
author:
  - literal: "Julia Gastinger"
  - literal: "Thilo Dieing"
  - literal: "Christian Meilicke"
  - literal: "Heiner Stuckenschmidt"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24467"

# Custom fields
paper_id: "2609.24467"
paper_source: "openalex"
domain: "nlp"
tags:
  - "knowledge-graph"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "zero-shot-learning"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:38:47Z"
created_at: "2026-09-24T09:38:47Z"
---

# A Temporal Knowledge Graph for Music Festival Lineup Forecasting

**Authors**: Julia Gastinger, Thilo Dieing, Christian Meilicke, Heiner Stuckenschmidt
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24467](https://arxiv.org/abs/2609.24467)

## Summary

This paper introduces a temporal knowledge graph (TKG) dataset covering 380 music festivals over 55 years with more than 90K performance quadruples to evaluate TKG forecasting methods. The authors formalize festival lineup forecasting as a temporal link prediction task between artists and festivals at future timestamps. Through extensive evaluation, six TKG forecasting models are benchmarked and compared against zero-shot Large Language Models, demonstrating the value of this real-world domain for forecasting research.

## Key Contributions

- Introduced a temporal knowledge graph dataset covering 380 festivals over 55 years with over 90K festival performance quadruples for TKG forecasting evaluation.
- Formalized music festival lineup forecasting as a temporal link prediction task between artists and festivals at future timestamps.
- Evaluated six TKG forecasting models and compared their performance against zero-shot Large Language Models on the proposed real-world benchmark.

## Open Questions & Future Work

- [[multimodal-tkg-festival-forecasting]]

## Archivist Review

Approved one open question regarding multimodal extensions for temporal knowledge graph festival forecasting, while rejecting routine dataset introductions and generic scalability questions.

### Approved Open Questions
- Multimodal TKG Festival Forecasting: Extending TKG forecasting with multimodal data, fine-grained spatial modeling, and unstructured external knowledge addresses the current performance bottleneck where models struggle to capture the complex, real-world constraints of festival booking.

### Rejected Candidates
- [open_question] Efficient TKG Reasoning Scalability (`efficient-tkg-reasoning-scalability`) - low_impact: Too generic of a systems and scalability bottleneck rather than a specific algorithmic or theoretical gap.

## Links

- [Abstract](https://arxiv.org/abs/2609.24467)
- [PDF](https://arxiv.org/pdf/2609.24467)

