---
# CSL-compatible fields
title: "Bridging the Last Mile of Time Series Forecasting with LLM Agents"
author:
  - literal: "Yuhua Liao"
  - literal: "Zetian Wang"
  - literal: "Qiangqiang Nie"
  - literal: "Zhenhua Zhang"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.02497"

# Custom fields
paper_id: "2606.02497"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "agent"
  - "autonomous-agent"
  - "reasoning"
  - "planning"
  - "retrieval-augmented-generation"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "last-mile-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:42:39Z"
created_at: "2026-06-04T08:42:39Z"
---

# Bridging the Last Mile of Time Series Forecasting with LLM Agents

**Authors**: Yuhua Liao, Zetian Wang, Qiangqiang Nie, Zhenhua Zhang
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.02497](https://arxiv.org/abs/2606.02497)

## Summary

This paper introduces the 'last-mile forecasting' framework to bridge the gap between statistical time series predictions and decision-ready outcomes in real-world business environments. By utilizing an LLM-agent architecture, the system incorporates unstructured contextual information—such as campaigns and historical analogs—to refine initial baseline forecasts. The framework achieves controllability and auditability through tools for evidence retrieval, structural safety constraints, and post-hoc reflection via a memory bank. Results from case studies demonstrate the system's effectiveness in producing actionable and context-aware forecasts.

## Key Contributions

- Formulates the 'last-mile forecasting' problem, which addresses the refinement of statistical baseline predictions using weakly structured external business context.
- Introduces an LLM-agent framework that integrates with forecasting backbones to enable retrieval of contextual evidence and explicit, auditable forecast revision actions.
- Implements a map-reduce-style decomposition for long-horizon forecasting and a memory-based post-hoc reflection mechanism to ensure forecast controllability and safety.

## Open Questions & Future Work

- [[last-mile-forecasting-benchmarking]]

## Key Concepts

- [[last-mile-forecasting]]: A forecasting stage focused on refining statistical model outputs using weakly structured business context, external events, and expert feedback to produce decision-ready results.

## Archivist Review

The approval is limited to the problem formulation (last-mile forecasting) and its corresponding evaluation need. The LLM-agent framework described is an implementation of this concept rather than a standalone architectural contribution requiring a permanent note, and no datasets were provided to review.

### Approved Concepts
- Last-mile forecasting: This concept explicitly addresses the under-explored gap between raw statistical output and decision-ready business forecasting by incorporating unstructured contextual evidence.

### Approved Open Questions
- Benchmarking Last-Mile Forecasting Performance: Standardizing evaluation is essential to track progress in agentic forecasting frameworks that require reliability, auditability, and context-awareness in operational settings.

## Links

- [Abstract](https://arxiv.org/abs/2606.02497)
- [PDF](https://arxiv.org/pdf/2606.02497)

