---
# CSL-compatible fields
title: "LLM-as-a-Judge for Time Series Explanations"
author:
  - literal: "Preetham Sivalingam"
  - literal: "Murari Mandal"
  - literal: "Saurabh Deshpande"
  - literal: "Dhruv Kumar"
issued:
  date-parts:
    - [2026, 4, 2]
url: "https://arxiv.org/abs/2604.02118"

# Custom fields
paper_id: "2604.02118"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "time-series"
  - "benchmark"
  - "evaluation"
  - "reasoning"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "llm-as-a-judge-for-time-series-explanations"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-05T06:08:24Z"
created_at: "2026-04-05T06:08:24Z"
---

# LLM-as-a-Judge for Time Series Explanations

**Authors**: Preetham Sivalingam, Murari Mandal, Saurabh Deshpande, Dhruv Kumar
**Date**: 2026-04-02
**Paper ID**: [openalex:2604.02118](https://arxiv.org/abs/2604.02118)

## Summary

This paper addresses the difficulty of evaluating LLM-generated explanations for time series data, which currently relies on limited reference-based metrics. The authors propose using LLMs themselves as evaluators in a reference-free setting, assessing textual reasoning against the raw signal for factual consistency. They introduce a synthetic benchmark covering 350 cases to test generation and evaluation capabilities, revealing a significant asymmetry where LLMs excel at scoring explanations even when their own generative performance is inconsistent. These findings suggest that LLM-based evaluation offers a robust path toward verifying data-grounded reasoning in the time series domain.

## Key Contributions

- Introduced a reference-free evaluation methodology using LLMs to score time series explanations based on pattern identification, numeric accuracy, and faithfulness.
- Constructed a synthetic benchmark of 350 time series cases across seven query types with annotated explanation correctness.
- Demonstrated that LLM-based evaluation is more stable than generation, consistently ranking and scoring explanations even when generative performance is poor.

## Key Concepts

- [[llm-as-a-judge-for-time-series-explanations]]: A reference-free evaluation framework that uses LLMs to score and rank textual explanations of time series data based on pattern identification and numeric accuracy.

## Archivist Review

I approved the core 'LLM-as-a-Judge' concept as it introduces a reusable, high-level evaluation paradigm for the emerging field of time-series interpretability. I rejected the synthetic benchmark because it serves as a paper-specific validation tool rather than a foundational or widely adopted dataset.

### Approved Concepts
- LLM-as-a-Judge for Time Series Explanations: Establishes a methodology for evaluating the faithfulness and correctness of time series explanations without requiring ground-truth references, addressing a major bottleneck in time-series interpretability.

### Rejected Candidates
- [dataset] Synthetic benchmark of 350 time series cases (`synthetic-benchmark-for-time-series-explanations`) - paper_local: The synthetic dataset is a local experimental artifact created to validate the methodology rather than a widely applicable or externally validated community resource.

## Links

- [Abstract](https://arxiv.org/abs/2604.02118)
- [PDF](https://arxiv.org/pdf/2604.02118)

