---
# CSL-compatible fields
title: "Segmenting Human-LLM Co-authored Text via Change Point Detection"
author:
  - literal: "Mengchu Li"
  - literal: "Jin Zhu"
  - literal: "Jinglai Li"
  - literal: "Chengchun Shi"
issued:
  date-parts:
    - [2026, 5, 5]
url: "https://arxiv.org/abs/2605.03723"

# Custom fields
paper_id: "2605.03723"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "change-point-detection-for-text-segmentation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-08T06:28:09Z"
created_at: "2026-05-08T06:28:09Z"
---

# Segmenting Human-LLM Co-authored Text via Change Point Detection

**Authors**: Mengchu Li, Jin Zhu, Jinglai Li, Chengchun Shi
**Date**: 2026-05-05
**Paper ID**: [openalex:2605.03723](https://arxiv.org/abs/2605.03723)

## Summary

This paper addresses the limitation of binary authorship detection by introducing a method to localize specific human-written and LLM-generated segments within co-authored text. By formalizing text provenance as a change point detection problem, the authors adapt time-series analysis techniques to segment texts based on varying detection scores. The approach includes weighted and generalized algorithms capable of handling heterogeneous score variability, with theoretical support proving minimax optimality. Empirical results demonstrate that this framework significantly outperforms existing baselines in authorship localization.

## Key Contributions

- Proposes a novel methodology for segmenting human-LLM co-authored text by framing the task as a change point detection problem.
- Develops weighted and generalized algorithms to handle heterogeneous detection score variability across text segments.
- Establishes theoretical minimax optimality for the proposed segmentation procedure and demonstrates superior empirical performance compared to existing baselines.

## Open Questions & Future Work

- [[generalizing-assumptions-for-change-point-detection-in-hybrid-text]]

## Key Concepts

- [[change-point-detection-for-text-segmentation]]: A statistical framework that redefines the localization of human and LLM-authored text segments as a change point detection problem in time-series analysis.

## Archivist Review

I approved the concept and open question because they effectively formalize the cross-domain application of time-series change point detection to authorship localization. I rejected other candidates or kept the scope limited to ensure the vault remains focused on fundamental methodological advancements in time-series analysis rather than implementation-specific algorithms or boilerplate future work. The approved items provide a clear path for future research in robust, non-asymptotic segmentation.

### Approved Concepts
- Change Point Detection for Text Segmentation: Represents a novel framing of text provenance as a time-series change point problem, enabling the application of statistical segmentation methods to authorship localization.

### Approved Open Questions
- Relaxing assumptions in hybrid text segmentation: Generalizing these assumptions would significantly expand the applicability of minimax optimal frameworks to more realistic, complex text where token-level or sentence-level scores exhibit significant correlation.

## Links

- [Abstract](https://arxiv.org/abs/2605.03723)
- [PDF](https://arxiv.org/pdf/2605.03723)

