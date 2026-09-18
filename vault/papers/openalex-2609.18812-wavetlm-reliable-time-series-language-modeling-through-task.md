---
# CSL-compatible fields
title: "WaveTLM: Reliable Time-Series Language Modeling through Task Compilation"
author:
  - literal: "Jiahui Chen"
  - literal: "Bingke Zhu"
  - literal: "Hongyu Pan"
  - literal: "Yingying Chen"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18812"

# Custom fields
paper_id: "2609.18812"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "language-model"
  - "llm"
  - "benchmark"
  - "evaluation"
  - "question-answering"
architectures:
  []
datasets:
  - "exects-qa"
concept_slugs:
  - "wavetlm"
dataset_slugs:
  - "exects-qa"
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:16:52Z"
created_at: "2026-09-18T09:16:52Z"
---

# WaveTLM: Reliable Time-Series Language Modeling through Task Compilation

**Authors**: Jiahui Chen, Bingke Zhu, Hongyu Pan, Yingying Chen
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18812](https://arxiv.org/abs/2609.18812)

## Summary

Time-series language models often generate plausible text that fails strict numerical or categorical constraints like shape, scale, and alignment. To address this, the authors formulate reliable time-series language modeling and introduce ExecTS-QA, a contract-grounded benchmark spanning five temporal task families. They propose WaveTLM, a unified compiler-executor model that transforms requests into typed task states and constructs legal outputs, achieving 99.40% contract-valid coverage on ExecTS-QA.

## Key Contributions

- Formulates reliable time-series language modeling by separating task-object reliability from predictive quality.
- Introduces ExecTS-QA, a contract-grounded benchmark covering five major temporal task families.
- Proposes WaveTLM, a compiler-executor model achieving 99.40% contract-valid coverage on ExecTS-QA compared to 37.83% for string-first baselines.

## Open Questions & Future Work

- [[task-object-hallucination-and-routing-reliability]]

## Key Concepts

- [[wavetlm]]: A unified compiler-executor model that transforms natural-language requests into reliable time-series outputs via task compilation.

## Archivist Review

Approved the core WaveTLM compiler-executor framework and the ExecTS-QA benchmark dataset, along with the open question regarding task-object hallucination in time-series language models. Strictly followed the scarcity and evidence guidelines.

### Approved Concepts
- WaveTLM: Central architectural novelty of the paper, providing reliable time-series language modeling through task compilation.

### Approved Open Questions
- Task-Object Hallucination and Routing Reliability: Understanding and mitigating routing failures and runtime exceptions in heterogeneous task compilation is critical for deploying reliable language-interfaced time-series systems in production.

### Rejected Candidates
- [dataset] ExecTS-QA (`exects-qa`) - other: Dataset note quota is restrictive, but ExecTS-QA is added as a named dataset.

## Datasets

- [[exects-qa]]

## Links

- [Abstract](https://arxiv.org/abs/2609.18812)
- [PDF](https://arxiv.org/pdf/2609.18812)

