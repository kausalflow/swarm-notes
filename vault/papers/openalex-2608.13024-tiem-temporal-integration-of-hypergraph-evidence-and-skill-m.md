---
# CSL-compatible fields
title: "TIEM: Temporal Integration of Hypergraph Evidence and Skill Memory for Event-Driven Financial Forecasting"
author:
  - literal: "Wenjin Liu"
  - literal: "Shen Pang"
  - literal: "Tiesunlong Shen"
  - literal: "Zhe Cui"
  - literal: "Xiaobao Wu"
  - literal: "Anh Tuan Luu"
  - literal: "Haoran Luo"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.13024"

# Custom fields
paper_id: "2608.13024"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "agent"
  - "retrieval-augmented-generation"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-16T05:18:20Z"
created_at: "2026-08-16T05:18:20Z"
---

# TIEM: Temporal Integration of Hypergraph Evidence and Skill Memory for Event-Driven Financial Forecasting

**Authors**: Wenjin Liu, Shen Pang, Tiesunlong Shen, Zhe Cui, Xiaobao Wu, Anh Tuan Luu, Haoran Luo
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.13024](https://arxiv.org/abs/2608.13024)

## Summary

Event-driven financial forecasting often suffers from temporal leakage and training data contamination, creating an evidence chasm in LLM agents. To address this, the authors propose TIEM, a timestamp-gated framework featuring an Event-Evidence Hypergraph for multi-tier retrieval, a Case-based Skill Memory for temporal skills, and Heterogeneous Evidence-Experience Fusion Reasoning. Additionally, they introduce the FinPURE benchmark and a Name-Date Probe to rigorously evaluate model sensitivity and robustness. Experiments across five financial forecasting benchmarks demonstrate that TIEM outperforms current baselines.

## Key Contributions

- Proposes TIEM, a timestamp-gated framework for event-driven financial forecasting combining hypergraph evidence retrieval and case-based skill memory.
- Introduces FinPURE, a recent-period A-share holdout benchmark, and a Name-Date Probe to evaluate model name-date sensitivity.
- Demonstrates superior performance across five financial forecasting benchmarks compared to existing LLM agent baselines.

## Archivist Review

Applied strict standards for the knowledge vault, rejecting paper-internal architectural extensions and benchmarks to avoid cluttering the vault with non-reusable local components.

### Rejected Candidates
- [open_question] Dynamic Regime Adaptation and Incremental Hypergraph Refinement (`dynamic-regime-adaptation-and-incremental-hypergraph-refinement`) - low_impact: This open question outlines paper-specific future work directions for a particular hypergraph-and-memory financial forecasting architecture rather than a broad vault-level bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.13024)
- [PDF](https://arxiv.org/pdf/2608.13024)

