---
# CSL-compatible fields
title: "TraceBench: Controlled Evaluation of LLM Agents for Time-Series Root-Cause Attribution"
author:
  - literal: "Tommaso Bendinelli"
  - literal: "Artur Dox"
  - literal: "Christian Holz"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.27182"

# Custom fields
paper_id: "2608.27182"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "agent"
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "tracebench"
concept_slugs:
  - "tracebench"
dataset_slugs:
  - "tracebench"
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:10:25Z"
created_at: "2026-08-30T10:10:25Z"
---

# TraceBench: Controlled Evaluation of LLM Agents for Time-Series Root-Cause Attribution

**Authors**: Tommaso Bendinelli, Artur Dox, Christian Holz
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.27182](https://arxiv.org/abs/2608.27182)

## Summary

The paper introduces TraceBench, a simulation-based framework designed to evaluate Large Language Model (LLM) agents on root-cause attribution tasks using time-series data from physical dynamical systems. Through systematic evaluation of four LLM agents across controlled conditions, the authors uncover key behavioral insights, including agents' reliance on numerical console outputs over visualizations and the performance drop when required to write executable Python scripts rather than direct predictions.

## Key Contributions

- Introduces TraceBench, a simulation-based benchmark framework for generating controlled time-series root-cause attribution tasks from physical dynamical systems.
- Evaluates four LLM agents across controlled conditions, revealing that agents rely heavily on numerical console output rather than visualizations and benefit significantly from domain context.
- Demonstrates that LLM agents perform worse when tasked with generating executable Python scripts mapping samples to labels compared to submitting direct predictions.

## Open Questions & Future Work

- [[open-ended-multivariate-time-series-root-cause-attribution]]

## Key Concepts

- [[tracebench]]: A simulation-based benchmark framework for evaluating LLM agents on time-series root-cause attribution tasks.

## Archivist Review

Approved the TraceBench concept and dataset as central contributions for evaluating LLM agentic time-series reasoning, along with the open-ended multivariate root-cause attribution open question. Strict adherence to scarcity and utility standards was maintained.

### Approved Concepts
- TraceBench: TraceBench provides a novel simulation-based evaluation framework and benchmark for assessing LLM agents on time-series root-cause attribution.

### Approved Open Questions
- Open-ended Multivariate Time-Series Diagnosis: Extending controlled time-series diagnosis benchmarks to open-ended, multi-parameter, and irregularly sampled environments is critical for evaluating real-world operational readiness in complex industrial and software systems.

## Datasets

- [[tracebench]]

## Links

- [Abstract](https://arxiv.org/abs/2608.27182)
- [PDF](https://arxiv.org/pdf/2608.27182)

