---
# CSL-compatible fields
title: "Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability"
author:
  - literal: "Nicolae Filat"
  - literal: "Ahmed Hussain"
  - literal: "Konstantinos Kalogiannis"
  - literal: "Elena Burceanu"
issued:
  date-parts:
    - [2026, 4, 23]
url: "https://arxiv.org/abs/2604.21930"

# Custom fields
paper_id: "2604.21930"
paper_source: "openalex"
domain: "nlp"
tags:
  - "continual-learning"
  - "evaluation"
  - "benchmark"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "CESNET-Timeseries24"
concept_slugs:
  - "temporal-taskification"
  - "boundary-profile-sensitivity"
dataset_slugs:
  - "cesnet-timeseries24"
skill: "TimeSeriesSkill"
processed_at: "2026-04-26T06:55:04Z"
created_at: "2026-04-26T06:55:04Z"
---

# Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability

**Authors**: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
**Date**: 2026-04-23
**Paper ID**: [openalex:2604.21930](https://arxiv.org/abs/2604.21930)

## Summary

The authors demonstrate that the standard practice of partitioning continuous streams into discrete tasks in streaming continual learning (CL) introduces significant evaluation instability. By varying temporal splits while keeping other experimental factors constant, they show that different taskifications lead to vastly different conclusions about model performance. To address this, the paper introduces a framework using plasticity/stability profiles and the Boundary-Profile Sensitivity (BPS) metric to quantify and diagnose the impact of task partitioning choices on downstream learning regimes.

## Key Contributions

- Demonstrates that temporal taskification is a first-class evaluation variable that significantly alters metrics like forecasting error and forgetting.
- Introduces a taskification-level framework based on plasticity and stability profiles to measure cross-taskification variability.
- Proposes Boundary-Profile Sensitivity (BPS) to diagnose the impact of task boundary selection on continual learning regimes prior to training.

## Open Questions & Future Work

- [[robust-automated-temporal-taskification]]

## Key Concepts

- [[temporal-taskification]]: A preprocessing step in streaming continual learning where continuous streams are divided into discrete tasks, which significantly impacts model performance outcomes.
- [[boundary-profile-sensitivity]]: A diagnostic metric that quantifies how strongly small perturbations in task boundaries change the induced distribution-level regime in continual learning.

## Archivist Review

The paper introduces a compelling framework for evaluating instability in streaming continual learning caused by arbitrary temporal task splitting. I have approved the key concepts ('Temporal Taskification' and 'Boundary-Profile Sensitivity') as they provide a necessary, reusable foundation for diagnosing evaluation bias. 'CESNET-Timeseries24' is approved as it is a specific, well-defined dataset central to the paper's claims, and the open question addresses a critical, unresolved research gap regarding the neutrality of stream partitioning.

### Approved Concepts
- Temporal Taskification: Identifies task splitting as a structural component of CL evaluation that fundamentally alters benchmark results independently of the learner.
- Boundary-Profile Sensitivity: Enables quantification of how arbitrary task boundary selection affects continual learning stability.

### Approved Open Questions
- Robust and Automated Temporal Taskification: This is critical because it addresses the core issue of benchmark instability in streaming settings, which currently limits the reproducibility and reliability of continual learning evaluations.

## Datasets

- [[cesnet-timeseries24]]

## Links

- [Abstract](https://arxiv.org/abs/2604.21930)
- [PDF](https://arxiv.org/pdf/2604.21930)

