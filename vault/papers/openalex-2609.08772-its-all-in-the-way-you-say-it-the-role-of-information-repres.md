---
# CSL-compatible fields
title: "It's All in the Way You Say It: The Role of Information Representation in LLM-Based Glycemic-Event Prediction"
author:
  - literal: "Andrea Apicella"
  - literal: "Pasquale Arpaïa"
  - literal: "Matteo Orefice"
  - literal: "Andrea Pollastro"
  - literal: "Roberto Prevete"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.08772"

# Custom fields
paper_id: "2609.08772"
paper_source: "openalex"
domain: "medicine"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
  - "few-shot-learning"
  - "evaluation"
  - "dataset"
architectures:
  []
datasets:
  - "ohiot1dm-dataset"
concept_slugs:
  []
dataset_slugs:
  - "ohiot1dm-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:17:01Z"
created_at: "2026-09-10T09:17:01Z"
---

# It's All in the Way You Say It: The Role of Information Representation in LLM-Based Glycemic-Event Prediction

**Authors**: Andrea Apicella, Pasquale Arpaïa, Matteo Orefice, Andrea Pollastro, Roberto Prevete
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.08772](https://arxiv.org/abs/2609.08772)

## Summary

This study investigates the role of information representation and prompt design in applying general-purpose Large Language Models (LLMs) to glycemic-event prediction (hyperglycemia and hypoglycemia) using the OhioT1DM dataset across 30, 60, and 90-minute horizons. Evaluating multiple open-weight LLMs under zero-shot and few-shot settings, the authors find that conventional supervised models excel at hyperglycemia prediction, whereas prompt-based LLMs achieve superior performance for hypoglycemia. Furthermore, the results indicate that textual representation format heavily influences effectiveness, while supplemental contextual variables do not systematically improve forecasts.

## Key Contributions

- Evaluates prompt-based general-purpose LLMs under zero-shot and few-shot inference for postprandial hyperglycemia and hypoglycemia prediction across 30, 60, and 90-minute horizons using the OhioT1DM dataset.
- Demonstrates that conventional supervised models outperform LLMs for hyperglycemia prediction, while optimal prompt-based LLM configurations improve performance for hypoglycemia across all horizons.
- Shows that textual representation of physiological information is a critical design factor, whereas adding extra contextual variables does not lead to systematic performance gains.

## Limitations

Future work could explore more advanced context representations and fine-tuning strategies for adapting general-purpose LLMs to patient-specific continuous glucose monitoring data.

## Open Questions & Future Work

- [[evaluating-pretraining-contamination-biomedical-benchmarks]]
- [[in-context-demonstration-imbalance-clinical-prediction]]

## Archivist Review

The paper studies the role of prompt-based representations for LLMs on the OhioT1DM dataset. No novel algorithmic concepts are introduced. The dataset 'ohiot1dm-dataset' already exists in the vault, and the open questions are duplicates of existing contamination and in-context learning questions. Therefore, no new concepts or open questions are approved, and the dataset is already present.

### Approved Open Questions
- Evaluating Pretraining Contamination in Biomedical Benchmarks: Data contamination can artificially inflate the zero-shot and few-shot performance of general-purpose foundation models on standard clinical benchmarks, making it critical to establish robust auditing and evaluation methodologies.
- In-Context Demonstration Impact on Imbalanced Clinical Prediction: Understanding how in-context learning behaves under extreme class imbalance is crucial for deploying reliable LLM-based clinical early-warning systems without introducing bias.

### Rejected Candidates
- [open_question] Evaluating Pretraining Contamination in Biomedical Benchmarks (`evaluating-pretraining-contamination-biomedical-benchmarks`) - duplicate_existing: Already exists in vault under a similar or identical formulation.
- [open_question] In-Context Demonstration Impact on Imbalanced Clinical Prediction (`in-context-demonstration-imbalance-clinical-prediction`) - duplicate_existing: Already exists or is too closely related to existing prompt sensitivity questions in the vault.

## Datasets

- [[ohiot1dm-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2609.08772)
- [PDF](https://arxiv.org/pdf/2609.08772)

