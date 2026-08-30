---
# CSL-compatible fields
title: "DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research"
author:
  - literal: "Linsen Zhu"
  - literal: "Yi Shi"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26990"

# Custom fields
paper_id: "2608.26990"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "agent"
  - "autonomous-agent"
  - "tool-use"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:11:40Z"
created_at: "2026-08-30T10:11:40Z"
---

# DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research

**Authors**: Linsen Zhu, Yi Shi
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26990](https://arxiv.org/abs/2608.26990)

## Summary

The paper presents DSA, an evidence-aware LLM-agent orchestration framework designed for multi-market stock research. DSA structures the workflow across evidence acquisition, structured context construction, model-routed analysis, optional strategy reasoning, and report generation with diagnostics. A reference implementation demonstrates its modularity across six regional markets and fifteen strategy skills, validated through extensive offline contract testing.

## Key Contributions

- Introduces DSA, an evidence-aware LLM-agent orchestration framework for multi-market stock research that structures workflows from evidence acquisition to report generation.
- Implements a multi-profile architecture supporting default and agentic profiles sharing model-routing services with profile-specific output validation and risk safeguards.
- Features a reference implementation with six regional market paths, fifteen bundled Strategy Skills, and software contract conformance verified across 1,457 offline backend contract tests.

## Limitations

The evaluation focuses on implementation conformance via software contract tests rather than superior investment returns, forecasting accuracy, or report quality.

## Archivist Review

No new concepts required as none met the strict novelty and reusability criteria beyond existing terminology.

## Links

- [Abstract](https://arxiv.org/abs/2608.26990)
- [PDF](https://arxiv.org/pdf/2608.26990)

