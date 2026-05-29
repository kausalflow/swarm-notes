---
# CSL-compatible fields
title: "Quality Without Usefulness: LLM-Generated XAI Narratives as Trust Heuristics Rather Than Decision Aids"
author:
  - literal: "Fabian Lukassen"
  - literal: "Jan Herrmann"
  - literal: "Christoph Weisser"
  - literal: "Alexander Silbersdorff"
  - literal: "Benjamin Saefken"
  - literal: "Thomas Kneib"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26770"

# Custom fields
paper_id: "2605.26770"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "explainability"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quality-usefulness-gap"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:38:46Z"
created_at: "2026-05-29T08:38:46Z"
---

# Quality Without Usefulness: LLM-Generated XAI Narratives as Trust Heuristics Rather Than Decision Aids

**Authors**: Fabian Lukassen, Jan Herrmann, Christoph Weisser, Alexander Silbersdorff, Benjamin Saefken, Thomas Kneib
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26770](https://arxiv.org/abs/2605.26770)

## Summary

This paper investigates whether the high quality of LLM-generated natural language explanations (NLEs) for XAI translates into improved practical decision-making in time-series forecasting. Across five controlled experiments, the authors find that NLEs consistently fail to improve task accuracy while simultaneously inflating user confidence through a placebic effect. Furthermore, these explanations provide false reassurance that can hinder the detection of out-of-distribution data, leading the authors to define this discrepancy as the 'Quality-Usefulness Gap.' The findings suggest that current text-quality metrics for XAI are insufficient and must be supplemented by rigorous downstream task performance evaluation.

## Key Contributions

- Demonstrates through five controlled experiments that LLM-generated Natural Language Explanations (NLEs) do not improve decision accuracy despite high quality scores.
- Identifies a 'placebic' effect where the mere presence of text—regardless of content—inflates user self-reported confidence in predictions.
- Shows that NLEs reduce performance on out-of-distribution detection tasks, creating false reassurance and masking underlying model failures.

## Open Questions & Future Work

- [[closing-the-xai-quality-usefulness-gap]]

## Key Concepts

- [[quality-usefulness-gap]]: The observation that high-quality, human-interpretable natural language explanations often fail to improve downstream decision-making accuracy.

## Archivist Review

The paper provides a compelling empirical investigation into the divergence between surface-level explanation quality and actual decision support. I have approved the 'Quality-Usefulness Gap' as a core concept describing this failure mode and the related open question regarding how to architect NLEs for actual utility rather than just fluency. These items are distinct, reusable, and address a critical bottleneck in XAI research.

### Approved Concepts
- Quality-Usefulness Gap: This concept identifies a fundamental discrepancy between high-quality natural language explanations and their lack of utility for decision-making tasks, which is critical for future XAI research.

### Approved Open Questions
- Closing the XAI Quality-Usefulness Gap: This question is central to the field of XAI because it challenges the reliance on surface-level quality metrics (coherence, fluency, plausibility) and highlights the danger of LLM-generated explanations acting as persuasive trust heuristics that mask model failures.

## Links

- [Abstract](https://arxiv.org/abs/2605.26770)
- [PDF](https://arxiv.org/pdf/2605.26770)

