---
# CSL-compatible fields
title: "Forecast Workflow Bench: Evaluating Language-Model Decisions with Budgeted Forecast Tools"
author:
  - literal: "Shunya Nagashima"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27385"

# Custom fields
paper_id: "2609.27385"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "agent"
  - "tool-use"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:36:57Z"
created_at: "2026-09-26T09:36:57Z"
---

# Forecast Workflow Bench: Evaluating Language-Model Decisions with Budgeted Forecast Tools

**Authors**: Shunya Nagashima
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27385](https://arxiv.org/abs/2609.27385)

## Summary

The paper introduces Forecast Workflow Bench (FWBench), a benchmark designed to evaluate how language-model agents utilize time-series foundation models (TSFMs) and forecasting tools under budget constraints to drive operational decisions. Tested on 1,251 electricity and cycle-hire cases, agents must choose models, histories, and horizons while balancing forecast accuracy and tool acquisition costs against a loss-cost objective. Results show that models like GPT-6 Astra selectively purchase inexpensive short-horizon forecasts, utilizing only 2.5% of their budget to outperform fixed baseline policies.

## Key Contributions

- Introduced FWBench, a benchmark comprising 1,251 electricity and cycle-hire cases for evaluating language-model agents making operational decisions under cost constraints.
- Evaluated two hosted and eight local configurations, demonstrating that selective short-horizon forecast acquisition achieves superior loss-cost trade-offs using minimal budget.
- Enabled reproducible evaluation of how language models select models, histories, and horizons to optimize operational decision quality.

## Limitations

Evaluated primarily on electricity and cycle-hire domains using specific simulated capacity contracts.

## Archivist Review

The submitted concept describes a benchmark framework rather than a reusable algorithmic mechanism or inductive bias, and the open question resembles broad future work rather than a concrete technical bottleneck. Following strict vault curation standards, both candidates are rejected.

### Rejected Candidates
- [concept] Forecast Workflow Bench (`forecast-workflow-bench`) - low_impact: Represents a benchmark framework rather than a reusable time-series forecasting mechanism, temporal inductive bias, or model architecture.
- [open_question] Evaluating Task-Specific Decision Models (`evaluating-task-specific-decision-models-and-agent-harnesses`) - weak_evidence: Future work direction is broad and encompasses generic experimental extensions rather than a well-defined technical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.27385)
- [PDF](https://arxiv.org/pdf/2609.27385)

