---
# CSL-compatible fields
title: "DeepAffinity: Long-Term Aspect Preference Prediction in eCommerce using Small Language Models"
author:
  - literal: "Yotam Eshel"
  - literal: "Guy Hadad"
  - literal: "Guy Feigenblat"
  - literal: "Yuri M. Brovman"
  - literal: "Matt Gearhart"
  - literal: "Bracha Shapira"
issued:
  date-parts:
    - [2026, 9, 2]
url: "https://arxiv.org/abs/2609.02468"

# Custom fields
paper_id: "2609.02468"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "fine-tuning"
  - "recommendation"
  - "multimodal"
  - "sequential-recommendation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "deepaffinity"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-05T08:42:12Z"
created_at: "2026-09-05T08:42:12Z"
---

# DeepAffinity: Long-Term Aspect Preference Prediction in eCommerce using Small Language Models

**Authors**: Yotam Eshel, Guy Hadad, Guy Feigenblat, Yuri M. Brovman, Matt Gearhart, Bracha Shapira
**Date**: 2026-09-02
**Paper ID**: [openalex:2609.02468](https://arxiv.org/abs/2609.02468)

## Summary

The paper introduces DeepAffinity, a framework that models long-term eCommerce user preferences for product aspects (such as brand, size, and color) by framing preference prediction as a temporal forecasting task over interaction histories. Utilizing Small Language Models (SLMs) equipped with structured prompts and specialized prediction heads, DeepAffinity outperforms standard generative fine-tuning and general-purpose LLMs while improving recommendation quality on a large-scale multinational platform.

## Key Contributions

- Introduces the 'Aspect Affinity' task for predicting long-term eCommerce user preferences across product aspects like brand, size, and color from time-ordered interaction histories.
- Proposes DeepAffinity, a framework leveraging Small Language Models (SLMs) with structured prompts and specialized prediction heads.
- Demonstrates that DeepAffinity outperforms standard generative fine-tuning and general-purpose open-source LLMs, enhancing recommendation quality on a large-scale multinational eCommerce platform.

## Open Questions & Future Work

- [[explicit-temporal-signals-preference-drift]]

## Key Concepts

- [[deepaffinity]]: A framework that leverages small language models with structured prompts and specialized prediction heads to predict long-term user aspect preferences in eCommerce.

## Archivist Review

Approved the DeepAffinity framework concept and the open question on explicit temporal signals and preference drift, following strict scarcity and relevance criteria. Rejected the domain-specific task definition as too narrow.

### Approved Concepts
- DeepAffinity: Introduces a novel framework for predicting eCommerce user aspect preferences using small language models with structured prompts and specialized prediction heads.

### Approved Open Questions
- Explicit Temporal Signals and Preference Drift: Explicitly modeling time intervals and cyclical trends is critical for capturing long-term preference evolution and seasonal drift in user behavior, which simple event-order sequences fail to represent fully.

### Rejected Candidates
- [concept] Aspect Affinity (`aspect-affinity`) - subcomponent_of_broader_mechanism: This task definition is highly specific to eCommerce aspect preference forecasting and is too narrow or subcomponent-like to warrant a permanent universal vault note.

## Links

- [Abstract](https://arxiv.org/abs/2609.02468)
- [PDF](https://arxiv.org/pdf/2609.02468)

