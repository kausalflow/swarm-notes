---
# CSL-compatible fields
title: "TT-SAX: A Two-Track Time Series Symbolization for Natural Language Shape Querying"
author:
  - literal: "Zhao Tan"
  - literal: "Xianglong Bao"
  - literal: "Zhipeng Xi"
  - literal: "Ming Jin"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.30593"

# Custom fields
paper_id: "2610.30593"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "retrieval"
  - "nlp"
  - "benchmark"
architectures:
  []
datasets:
  - "nlqtsbench"
concept_slugs:
  - "tt-sax"
dataset_slugs:
  - "nlqtsbench"
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:29:22Z"
created_at: "2026-10-25T09:29:22Z"
---

# TT-SAX: A Two-Track Time Series Symbolization for Natural Language Shape Querying

**Authors**: Zhao Tan, Xianglong Bao, Zhipeng Xi, Ming Jin
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.30593](https://arxiv.org/abs/2610.30593)

## Summary

This paper systematically studies time series symbolization for natural language shape querying, identifying limitations in classical methods such as missing directional information and arbitrary letter choices. To address these gaps, the authors propose TT-SAX (two-track SAX), which augments traditional SAX with multi-segment trend tracking and graded direction letters aligned with natural language query adjectives. Experiments on the NLQTSBench benchmark show that TT-SAX outperforms classical symbolizations across multiple language models.

## Key Contributions

- Identified three key limitations of classical time series symbolizations when applied to natural language shape querying: missing direction, overly localized scale, and arbitrary letters.
- Proposed TT-SAX (two-track SAX), a minimal redesign of SAX featuring level letters and multi-segment trend letters graded to match query adjectives.
- Evaluated TT-SAX across six classical symbolizations and six LLMs on the NLQTSBench benchmark, demonstrating superior performance on shape queries.

## Limitations

Future work could explore extending TT-SAX to handle multi-variate time series and more complex compositional natural language queries.

## Key Concepts

- [[tt-sax]]: A two-track time series symbolization method designed for natural language shape querying that augments traditional SAX with multi-segment trend tracking and graded direction letters.

## Archivist Review

Approved the core concept TT-SAX as a novel time-series symbolization designed for natural language shape querying. Approved NLQTSBench as a reusable dataset evaluation benchmark for natural language time series querying. Kept rejections aligned with review standards and strict caps.

### Approved Concepts
- TT-SAX: Core methodology introduced to bridge natural language shape queries and time series data by redesigning traditional SAX with a two-track approach incorporating direction and graded trend letters.

### Rejected Candidates
- [dataset] NLQTSBench (`nlqtsbench`) - duplicate_existing: NLQTSBench is already present in the vault or similar benchmark slots, but treated as a dataset evaluation name here; however, we are capping datasets and keeping clean identifiers.

## Datasets

- [[nlqtsbench]]

## Links

- [Abstract](https://arxiv.org/abs/2610.30593)
- [PDF](https://arxiv.org/pdf/2610.30593)

