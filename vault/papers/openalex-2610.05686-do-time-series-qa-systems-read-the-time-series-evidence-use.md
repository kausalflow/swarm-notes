---
# CSL-compatible fields
title: "Do Time-Series QA Systems Read the Time Series? Evidence Use and Reasoning Reliability"
author:
  - literal: "Zhuomin Chen"
  - literal: "Jingchao Ni"
  - literal: "Xu Zheng"
  - literal: "Janki Bhimani"
  - literal: "Mo Sha"
  - literal: "Wei Cheng"
  - literal: "Dongsheng Luo"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.05686"

# Custom fields
paper_id: "2610.05686"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "question-answering"
  - "benchmark"
  - "evaluation"
  - "interpretability"
  - "explainability"
  - "reasoning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:40:35Z"
created_at: "2026-10-08T11:40:35Z"
---

# Do Time-Series QA Systems Read the Time Series? Evidence Use and Reasoning Reliability

**Authors**: Zhuomin Chen, Jingchao Ni, Xu Zheng, Janki Bhimani, Mo Sha, Wei Cheng, Dongsheng Luo
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.05686](https://arxiv.org/abs/2610.05686)

## Summary

This paper investigates whether current time-series question answering (QA) systems genuinely utilize and reason over supplied numerical data rather than relying on backbone priors or fallback heuristics. The authors introduce COMMON-TSQA, a unified benchmark evaluating four prominent time-series QA systems under various input interventions. Their findings reveal that aggregate performance scores often obscure ungrounded rationale claims, invalid intermediate inferences, and a lack of genuine sensitivity to numerical input changes.

## Key Contributions

- Introduces COMMON-TSQA, a unified benchmark for evaluating time-series question answering systems across standardized representations, task definitions, and answer schemas.
- Evaluates four prominent time-series QA systems (TimeOmni-1, ChatTS, TimeOmni-VL, and Time-MQA) under original conditions and six targeted interventions.
- Demonstrates that aggregate performance scores obscure underlying evidence utilization issues, revealing fallback behaviors and ungrounded rationale claims.
- Audits generated rationales for factual grounding, inference validity, and consistency with final answers, uncovering frequent unsupported numerical claims.

## Limitations

Focuses specifically on four existing time-series QA systems and evaluation via their respective interfaces under fixed questions and targets.

## Archivist Review

Strict adherence to the review policy was applied. The proposed benchmark concept and open question were evaluated against vault standards and rejected due to lack of permanent reusability and specificity.

### Rejected Candidates
- [concept] COMMON-TSQA (`common-tsqa`) - not_novel: While useful as an evaluation suite for this specific paper, custom benchmark evaluation suites for time-series QA do not qualify as permanent fundamental vault concepts.
- [open_question] Intermediate Numerical Verification in Training (`intermediate-numerical-verification-training`) - weak_evidence: This is a standard call for better training objectives and loss supervision for reasoning models rather than a sharp, technically bounded unresolved bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.05686)
- [PDF](https://arxiv.org/pdf/2610.05686)

