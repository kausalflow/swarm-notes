---
# CSL-compatible fields
title: "Design a Reliable LLM-Integrated Interface for Mortality Forecasting"
author:
  - literal: "Thi Kim Ngan Nguyen"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06235"

# Custom fields
paper_id: "2606.06235"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "agent"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:19:15Z"
created_at: "2026-06-07T08:19:15Z"
---

# Design a Reliable LLM-Integrated Interface for Mortality Forecasting

**Authors**: Thi Kim Ngan Nguyen
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06235](https://arxiv.org/abs/2606.06235)

## Summary

This paper addresses the gap between technical complexity and accessibility in mortality forecasting by developing a reliable, LLM-integrated user interface. The system utilizes a constrained LLM layer to interpret natural language requests and orchestrate a deterministic, actuarial-grade forecasting pipeline based on the CoMoMo package. Through a three-phase methodology incorporating rolling-origin validation, the framework demonstrates that LLM-driven accessibility can be achieved while maintaining strict standards for reproducibility and transparency in high-stakes decision-making.

## Key Contributions

- Introduces a constrained LLM-orchestration layer for translating natural language into structured configurations for mortality forecasting.
- Validates the system's reliability and reproducibility using the CoMoMo package as a deterministic forecasting backbone.
- Demonstrates a multi-phase forecasting workflow using rolling-origin evaluation to ensure actuarial validity in user-facing analytical tools.

## Open Questions & Future Work

- [[hybrid-llm-architecture-reliability]]

## Archivist Review

The paper proposes a specific application of LLM orchestration for actuarial mortality forecasting. I have approved the open question regarding the reliability of hybrid LLM architectures in high-stakes settings, as this is a fundamental research challenge in deploying such systems. The proposed orchestration layer concept was rejected as it is a specific implementation strategy tied to a local codebase rather than a standalone, reusable methodology.

### Approved Open Questions
- Hybrid LLM Architectures for Reliability: Ensuring the reliability of LLM-generated configurations is critical for preventing misinterpretation and errors in high-stakes domains like actuarial science.

### Rejected Candidates
- [concept] Constrained LLM-orchestration layer (`constrained-llm-orchestration-layer`) - paper_local: This is a paper-local implementation detail describing how the system uses an LLM to interface with a specific forecasting package rather than a general-purpose concept.

## Links

- [Abstract](https://arxiv.org/abs/2606.06235)
- [PDF](https://arxiv.org/pdf/2606.06235)

