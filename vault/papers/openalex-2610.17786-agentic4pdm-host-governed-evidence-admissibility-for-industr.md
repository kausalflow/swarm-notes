---
# CSL-compatible fields
title: "Agentic4PDM: Host-Governed Evidence Admissibility for Industrial Fault Diagnosis"
author:
  - literal: "Nam V. Nguyen"
  - literal: "Hoang Truong"
  - literal: "Hieu D. D."
  - literal: "Duy Khuong Nguyen"
  - literal: "Quang Pham"
  - literal: "Tung Kieu"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17786"

# Custom fields
paper_id: "2610.17786"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "agent"
  - "autonomous-agent"
  - "anomaly-detection"
  - "classification"
  - "llm"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "agentic4pdm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:25:18Z"
created_at: "2026-10-16T09:25:18Z"
---

# Agentic4PDM: Host-Governed Evidence Admissibility for Industrial Fault Diagnosis

**Authors**: Nam V. Nguyen, Hoang Truong, Hieu D. D., Duy Khuong Nguyen, Quang Pham, Tung Kieu
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17786](https://arxiv.org/abs/2610.17786)

## Summary

Agentic4PDM is a framework for industrial fault diagnosis that addresses scarce labels and changing operating conditions by decoupling adaptive LLM-driven investigation from deterministic host governance. Using contract-checked gated adjudication (CCGA), a software controller strictly governs tool requests, requires batch commitment, and assigns rigorous evidence roles before the Judge Agent proposes a final diagnosis. Experiments across standard bearing/motor challenges and industrial test sets demonstrate significant macro F1 gains over existing baselines.

## Key Contributions

- Introduced Agentic4PDM, a training-free and model-inspecting diagnosis framework separating adaptive agent investigation from deterministic evidence control.
- Designed contract-checked gated adjudication (CCGA) to enforce tool batch commitment and assign strict evidence roles (corroborative support vs. advisory information).
- Demonstrated superior macro F1 performance over evaluated diagnostic and agentic baselines across benchmark bearing and motor challenges as well as real-world industrial datasets.

## Open Questions & Future Work

- [[tool-consolidation-and-functional-broadening]]

## Key Concepts

- [[agentic4pdm]]: A framework for industrial fault diagnosis that separates adaptive LLM agent investigation from deterministic host-governed evidence admissibility.

## Archivist Review

Approved the core framework concept 'Agentic4PDM' for its reusable design pattern separating LLM exploration from deterministic host governance, and approved one high-impact open question regarding tool consolidation. Rejected the second open question as it pertains to practical product feature additions rather than technical machine learning research bottlenecks.

### Approved Concepts
- Agentic4PDM: Central framework for host-governed evidence admissibility in industrial fault diagnosis using LLM agents.

### Approved Open Questions
- Tool Consolidation and Functional Broadening: Simplifying toolspaces and contexts in agentic diagnostics reduces token costs and improves reliability during multi-turn investigations.

### Rejected Candidates
- [open_question] Actionable Follow-up Recommendations for Unresolved Diagnoses (`actionable-follow-up-recommendations-for-unresolved-diagnoses`) - low_impact: Refers to future product feature extensions rather than a fundamental theoretical or methodological bottleneck in ML.

## Links

- [Abstract](https://arxiv.org/abs/2610.17786)
- [PDF](https://arxiv.org/pdf/2610.17786)

