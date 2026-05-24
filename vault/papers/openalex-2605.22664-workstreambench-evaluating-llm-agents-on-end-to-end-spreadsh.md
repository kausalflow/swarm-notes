---
# CSL-compatible fields
title: "WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance"
author:
  - literal: "Thomson Yen"
  - literal: "Julian Poeltl"
  - literal: "Harshith Srinivas Gear"
  - literal: "Yilin Meng"
  - literal: "Joshua Fan"
  - literal: "Adam Shen"
  - literal: "Yili Liu"
  - literal: "Ali Bauyrzhan"
  - literal: "Siri Du"
  - literal: "Haoyang Liu"
  - literal: "Daniel Guetta"
  - literal: "Hongseok Namkoong"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22664"

# Custom fields
paper_id: "2605.22664"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "benchmark"
  - "evaluation"
  - "language-model"
architectures:
  []
datasets:
  - "workstreambench"
concept_slugs:
  []
dataset_slugs:
  - "workstreambench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:48:01Z"
created_at: "2026-05-24T07:48:01Z"
---

# WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance

**Authors**: Thomson Yen, Julian Poeltl, Harshith Srinivas Gear, Yilin Meng, Joshua Fan, Adam Shen, Yili Liu, Ali Bauyrzhan, Siri Du, Haoyang Liu, Daniel Guetta, Hongseok Namkoong
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22664](https://arxiv.org/abs/2605.22664)

## Summary

This paper introduces WorkstreamBench, a benchmark designed to evaluate the capability of LLM agents to perform end-to-end spreadsheet tasks within financial workflows such as modeling and scenario analysis. Unlike existing benchmarks focused on single-formula edits or question-answering, this framework assesses agents on their ability to produce complete, professional-quality artifacts using a three-dimensional taxonomy covering Accuracy, Formula, and Format. Experimental results highlight that frontier agents currently struggle to meet professional standards as task complexity increases, indicating a significant gap in reliability for enterprise-level financial modeling.

## Key Contributions

- Introduces WorkstreamBench, a novel benchmark evaluating LLM agents on complex, end-to-end spreadsheet creation tasks in financial modeling and scenario analysis.
- Defines a three-dimensional evaluation taxonomy (Accuracy, Formula, and Format) to assess the professional quality of spreadsheet-based financial deliverables.
- Demonstrates that while frontier models like Claude achieve top performance, current agents struggle with professional-grade complexity and long-chained calculations in real-world workflows.

## Open Questions & Future Work

- [[agentic-spreadsheet-modeling-complexity-limits]]

## Archivist Review

I approved the dataset name and an open question regarding complexity limits for agentic spreadsheet modeling. I rejected the initial open question candidate because it was less precise than the reformulated version that specifically targets the architectural challenges of agentic modeling as discussed in the paper.

### Approved Open Questions
- Agentic spreadsheet modeling complexity limits: As agentic systems attempt to move from atomic formula generation to full financial modeling, identifying the ceiling of their architectural capabilities requires increasingly challenging, non-atomic benchmarks. Tracking progress on such tasks is essential for measuring reliable performance in high-stakes enterprise settings.

### Rejected Candidates
- [open_question] Benchmarking harder spreadsheet tasks (`benchmarking-harder-spreadsheet-tasks`) - duplicate_existing: This candidate is a less descriptive version of the proposed research question regarding complexity limits.

## Datasets

- [[workstreambench]]

## Links

- [Abstract](https://arxiv.org/abs/2605.22664)
- [PDF](https://arxiv.org/pdf/2605.22664)

