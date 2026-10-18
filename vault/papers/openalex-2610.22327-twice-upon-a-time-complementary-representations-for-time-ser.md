---
# CSL-compatible fields
title: "Twice Upon a Time: Complementary Representations for Time-Series Reasoning"
author:
  - literal: "Hedi Zisling"
  - literal: "Liran Nochumsohn"
  - literal: "Ilan Naiman"
  - literal: "Mihir Parmar"
  - literal: "Omri Azencot"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.22327"

# Custom fields
paper_id: "2610.22327"
paper_source: "openalex"
domain: "nlp"
tags:
  - "multimodal"
  - "vision-language-model"
  - "language-model"
  - "time-series"
  - "reasoning"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-decoder"
datasets:
  - "tsrbench"
  - "tsexam"
concept_slugs:
  []
dataset_slugs:
  - "tsrbench"
  - "tsexam"
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:12:40Z"
created_at: "2026-10-18T09:12:40Z"
---

# Twice Upon a Time: Complementary Representations for Time-Series Reasoning

**Authors**: Hedi Zisling, Liran Nochumsohn, Ilan Naiman, Mihir Parmar, Omri Azencot
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.22327](https://arxiv.org/abs/2610.22327)

## Summary

This paper introduces complementary representations as a design principle for Time Series Language Models (TSLMs), combining line plots (which preserve absolute measurements) and normalized delay embeddings (which factor out amplitude rescaling and offsets while exposing temporal structure). Built on Qwen3-VL-8B, the proposed dual-view model integrates both representations via visual tokens and multi-level feature fusion. Evaluated across multiple benchmarks, the dual-view approach significantly outperforms single-view ablations and dedicated TSLM baselines, achieving 53.2% on TSRBench, 89.9% on TSExam, and 86.8% numerical accuracy on multivariate ChatTS alignment.

## Key Contributions

- Introduces complementary representations as a design principle for time-series reasoning, combining line plots (preserving absolute measurements) with normalized delay embeddings (exposing temporal structure).
- Builds a dual-view model on Qwen3-VL-8B using dedicated visual encoders and multi-level feature fusion to integrate both representations into a shared language model.
- Improves overall TSRBench accuracy from 44.5% (line plots alone) to 53.2%, exceeding the strongest dedicated TSLM baseline of 36.7%.
- Achieves 89.9% accuracy on TSExam and 86.8% numerical accuracy on multivariate ChatTS alignment.

## Limitations

Depends on vision-language model architectures and visual representations of time series, which may introduce rendering or resolution bottlenecks compared to direct numerical tokenization.

## Open Questions & Future Work

- [[query-dependent-multimodal-fusion-for-tslms]]

## Archivist Review

Approved two key benchmarks (TSRBench and TSExam) central to the paper's evaluation claims, while rejecting the open question to adhere to strict scarcity guidelines.

### Approved Open Questions
- Query-Dependent Multimodal Fusion: Developing adaptive or query-dependent multimodal fusion techniques is crucial for handling diverse time-series reasoning tasks that require different representational trade-offs.

### Rejected Candidates
- [open_question] Query-Dependent Multimodal Fusion (`query-dependent-multimodal-fusion-for-tslms`) - low_impact: The open question is a valid future work direction, but we are prioritizing dataset notes and keeping concept/question approvals scarce.

## Datasets

- [[tsrbench]]
- [[tsexam]]

## Links

- [Abstract](https://arxiv.org/abs/2610.22327)
- [PDF](https://arxiv.org/pdf/2610.22327)

