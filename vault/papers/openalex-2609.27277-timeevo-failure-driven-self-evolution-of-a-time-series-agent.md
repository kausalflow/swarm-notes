---
# CSL-compatible fields
title: "TimeEvo: Failure-Driven Self-Evolution of a Time Series Agent"
author:
  - literal: "Jie Yang"
  - literal: "Yan Zheng"
  - literal: "Jiarui Sun"
  - literal: "Xiran Fan"
  - literal: "Junpeng Wang"
  - literal: "Liang Wang"
  - literal: "Zelin Xu"
  - literal: "Qinghua Liu"
  - literal: "Zhengyu Fang"
  - literal: "Yiwei Cai"
  - literal: "Philip S. Yu"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27277"

# Custom fields
paper_id: "2609.27277"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "agent"
  - "question-answering"
  - "tool-use"
  - "autonomous-agent"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:37:10Z"
created_at: "2026-09-26T09:37:10Z"
---

# TimeEvo: Failure-Driven Self-Evolution of a Time Series Agent

**Authors**: Jie Yang, Yan Zheng, Jiarui Sun, Xiran Fan, Junpeng Wang, Liang Wang, Zelin Xu, Qinghua Liu, Zhengyu Fang, Yiwei Cai, Philip S. Yu
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27277](https://arxiv.org/abs/2609.27277)

## Summary

This paper introduces TimeEvo, a failure-driven self-evolution framework for time series agents designed to overcome the limitations of static, human-curated tool libraries. The authors identify two critical issues in existing agent setups: Human-Agent Tool Misalignment and Silent Harm during generic self-revision. To resolve these issues, TimeEvo clusters diagnosed agent failures into capability gaps, synthesizes evidence-only tools dynamically, and filters candidates using a paired admission gate. Experiments across ten time series question-answering tasks and multiple backbones confirm that starting from an empty library, TimeEvo consistently improves accuracy and supports effective transfer from cheaper to stronger models.

## Key Contributions

- Identifies Human-Agent Tool Misalignment and Silent Harm in time series agent tool selection, demonstrating that static pre-configured tool libraries can degrade task performance.
- Proposes TimeEvo, a failure-driven self-evolution framework that clusters diagnosed failures into capability gaps, synthesizes evidence-only tools, and validates candidate libraries via a paired admission gate.
- Demonstrates consistent accuracy improvements across ten time series QA tasks and three backbone models starting from an empty tool library, with cross-model transferability from cheap to stronger models.

## Archivist Review

Applied strict filtering to keep the vault scarce and prevent paper-internal agent tool synthesis methods and questions from cluttering the long-lived knowledge base. No concepts or open questions met the high bar for universal reusability.

### Rejected Candidates
- [open_question] Failure-Driven Tool Evolution for Time Series Agents (`failure-driven-tool-evolution-time-series-agents`) - paper_local: Too paper-local and specific to time series agent tool synthesis and self-revision mechanics rather than a foundational open question in time series forecasting or modeling.

## Links

- [Abstract](https://arxiv.org/abs/2609.27277)
- [PDF](https://arxiv.org/pdf/2609.27277)

