---
# CSL-compatible fields
title: "Meta Models: Models that Model Learning"
author:
  - literal: "Li Peihang"
  - literal: "Ziming Liu"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.37001"

# Custom fields
paper_id: "2610.37001"
paper_source: "openalex"
domain: "nlp"
tags:
  - "meta-learning"
  - "tabular"
  - "in-context-learning"
  - "language-model"
  - "pre-training"
  - "hyperparameter-selection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:05:42Z"
created_at: "2026-10-30T11:05:42Z"
---

# Meta Models: Models that Model Learning

**Authors**: Li Peihang, Ziming Liu
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.37001](https://arxiv.org/abs/2610.37001)

## Summary

This paper introduces meta-models—models designed to predict the learning behavior, learning curves, and final performance of other neural networks before execution. Treating language-model training records as native numeric data rather than tokenized text, the authors find that an off-the-shelf tabular in-context learner (TabPFN) matches or outperforms fine-tuned LLM meta-models in seconds without weight updates. Furthermore, augmenting TabPFN with Kolmogorov-Arnold Networks enhances predictive accuracy, and the approach is validated via a pre-registered forecast of the 535B-parameter Marin Hero Run.

## Key Contributions

- Demonstrates that meta-modeling (predicting learning behavior, learning curves, and final performance) can be effectively formulated as a numeric modality rather than a text task for LLMs.
- Shows that an off-the-shelf tabular in-context learner, TabPFN, matches or outperforms fine-tuned LLM meta-models while requiring only seconds of fit-and-predict time.
- Establishes that augmenting TabPFN with Kolmogorov-Arnold Networks (KANs) further improves prediction accuracy on selected training response tasks.
- Performs a pre-registered forecast of the Marin Hero Run (a 535B-parameter public training run) to rigorously test meta-model predictions against unobserved real-world training outcomes.

## Limitations

Evaluated primarily as a first empirical step using tabular in-context learners and KAN augmentations on limited public training records; broader scaling laws across more diverse architectural families remain to be fully mapped.

## Archivist Review

I reviewed the candidate open question and rejected it because it represents a generic machine learning challenge (out-of-distribution extrapolation) rather than a specific, tightly scoped bottleneck unique to meta-modeling of training runs. No concepts or datasets met the strict novelty and reusability criteria for permanent vault notes.

### Rejected Candidates
- [open_question] Reliable Out-of-Distribution Extrapolation (`reliable-out-of-distribution-extrapolation`) - generic: The question of reliable out-of-distribution extrapolation is too general and applicable across almost all machine learning and forecasting domains rather than being uniquely specific to meta-models of learning curves.

## Links

- [Abstract](https://arxiv.org/abs/2610.37001)
- [PDF](https://arxiv.org/pdf/2610.37001)

