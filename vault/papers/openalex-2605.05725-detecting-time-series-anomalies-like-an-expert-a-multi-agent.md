---
# CSL-compatible fields
title: "Detecting Time Series Anomalies Like an Expert: A Multi-Agent LLM Framework with Specialized Analyzers"
author:
  - literal: "Hyeongwon Kang"
  - literal: "Jeongseob Kim"
  - literal: "Jinwoo Park"
  - literal: "Pilsung Kang"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05725"

# Custom fields
paper_id: "2605.05725"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "anomaly-detection"
  - "time-series"
  - "multi-agent"
  - "agent"
  - "interpretability"
  - "in-context-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sage-specialized-analyzer-group-for-expert-like-detection"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:21:08Z"
created_at: "2026-05-10T07:21:08Z"
---

# Detecting Time Series Anomalies Like an Expert: A Multi-Agent LLM Framework with Specialized Analyzers

**Authors**: Hyeongwon Kang, Jeongseob Kim, Jinwoo Park, Pilsung Kang
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05725](https://arxiv.org/abs/2605.05725)

## Summary

The paper introduces SAGE, a multi-agent framework designed to improve the interpretability and reliability of time series anomaly detection. By decomposing the analysis into specialized agents for point, structural, seasonal, and pattern anomalies, the system generates evidence-backed diagnostic reports instead of direct index inference. SAGE further utilizes synthetic in-context examples from normal data, achieving superior performance on standard benchmarks compared to existing general-purpose models.

## Key Contributions

- Introduces SAGE, a multi-agent framework that decomposes univariate time series anomaly diagnosis into specialized analyzers for point, structural, seasonal, and pattern anomalies.
- Implements an evidence-grounded detection mechanism that consolidates family-specific numerical and visual outputs into confidence-scored, interpretable anomaly records.
- Outperforms state-of-the-art ML, DL, and LLM-based baselines across three benchmark datasets while improving diagnostic reliability and practical utility.

## Open Questions & Future Work

- [[multivariate-tsad-extension]]

## Key Concepts

- [[sage-specialized-analyzer-group-for-expert-like-detection]]: A multi-agent framework that decomposes time series anomaly detection into specialized analyzers for distinct anomaly types to generate evidence-backed diagnostic reports.

## Archivist Review

I approved the SAGE framework as it establishes a distinct multi-agent approach to time series diagnostics that is sufficiently novel and reusable. I also approved the open question regarding multivariate extension, as it addresses a fundamental scaling challenge for this specific type of agentic architecture. The request regarding synthetic data realism was rejected as a generic research limitation.

### Approved Concepts
- SAGE (Specialized Analyzer Group for Expert-like Detection): It introduces a novel multi-agent decomposition paradigm for anomaly analysis, moving away from monolithic models towards modular, evidence-based diagnosis.

### Approved Open Questions
- Multivariate Time Series Extension: Real-world systems are typically multivariate, and anomalies often emerge from relationships across sensors rather than just individual signal deviations.

### Rejected Candidates
- [open_question] Improving Synthetic Anomaly Realism (`synthetic-data-realism`) - generic: The limitation regarding synthetic data realism is a generic observation common to almost all anomaly detection research rather than a specific, actionable research direction.

## Links

- [Abstract](https://arxiv.org/abs/2605.05725)
- [PDF](https://arxiv.org/pdf/2605.05725)

