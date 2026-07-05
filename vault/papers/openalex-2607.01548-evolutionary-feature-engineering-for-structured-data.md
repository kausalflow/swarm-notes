---
# CSL-compatible fields
title: "Evolutionary Feature Engineering for Structured Data"
author:
  - literal: "Ege Onur Taga"
  - literal: "Yilin Zhuang"
  - literal: "M. Emrullah Ildız"
  - literal: "Petros Mol"
  - literal: "Abhimanyu Das"
  - literal: "Karthik Duraisamy"
  - literal: "Samet Oymak"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01548"

# Custom fields
paper_id: "2607.01548"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "feature-engineering"
  - "benchmark"
architectures:
  []
datasets:
  - "covid-deaths"
concept_slugs:
  - "evolutionary-feature-engineering-efe"
dataset_slugs:
  - "covid-deaths"
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:52:29Z"
created_at: "2026-07-05T07:52:29Z"
---

# Evolutionary Feature Engineering for Structured Data

**Authors**: Ege Onur Taga, Yilin Zhuang, M. Emrullah Ildız, Petros Mol, Abhimanyu Das, Karthik Duraisamy, Samet Oymak
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01548](https://arxiv.org/abs/2607.01548)

## Summary

Evolutionary Feature Engineering (EFE) is a framework that leverages large language models as search operators to evolve Python programs for structured data preprocessing. By utilizing dataset context and downstream performance feedback, EFE discovers effective normalization and feature transformations that can be integrated into existing machine learning pipelines. The approach is demonstrated through EFE-Time for enhancing time-series foundation models and EFE-Tab for improving tabular prediction interpretability and accuracy.

## Key Contributions

- Introduces Evolutionary Feature Engineering (EFE), a framework using LLM-based evolution to generate Python-based data preprocessing pipelines.
- Demonstrates EFE-Time achieves significant performance gains (up to 19% on COVID-Deaths) when applied as a pre-processing step for Time-Series Foundation Models like Chronos-2.
- Shows EFE-Tab improves tabular prediction accuracy and interpretability for classical models like decision trees through automated feature refinement.

## Open Questions & Future Work

- [[evolutionary-hyperparameter-tuning-dynamics]]
- [[feedback-mechanism-ablation-in-evolutionary-search]]

## Key Concepts

- [[evolutionary-feature-engineering-efe]]: An evolutionary framework that employs LLMs to discover and refine dataset-specific feature preprocessing programs for structured data.

## Archivist Review

I have approved the Evolutionary Feature Engineering (EFE) framework as a central contribution, as it defines a reusable paradigm for LLM-driven preprocessing optimization. I have also approved two open questions that target the mechanisms of evolutionary search and feedback sensitivity, which are critical research bottlenecks. I have limited the dataset to COVID-Deaths, which served as a specific benchmark for EFE-Time's evaluation.

### Approved Concepts
- Evolutionary Feature Engineering (EFE): It introduces a novel methodology for using LLMs as search operators in an evolutionary loop to automate the discovery of effective preprocessing transformations.

### Approved Open Questions
- Evolutionary Search Hyperparameter Sensitivity: Search effectiveness in EFE is highly dependent on hyperparameter configurations, and understanding these dependencies is critical for scaling the framework.
- Feedback Component Ablation: Understanding the relationship between specific feedback types and LLM improvement trajectories is essential for developing autonomous, stable evolutionary optimizers.

### Rejected Candidates
- [open_question] Evolutionary Hyperparameter Sensitivity (`evolutionary-hyperparameter-tuning`) - duplicate_existing: Renamed for better clarity and to avoid duplication with existing tuning-related questions.
- [open_question] Feedback Component Ablation (`feedback-mechanism-ablation`) - duplicate_existing: Renamed to be more specific to the context of evolutionary search.

## Datasets

- [[covid-deaths]]

## Links

- [Abstract](https://arxiv.org/abs/2607.01548)
- [PDF](https://arxiv.org/pdf/2607.01548)

