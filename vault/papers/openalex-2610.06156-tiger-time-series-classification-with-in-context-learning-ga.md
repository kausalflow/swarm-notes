---
# CSL-compatible fields
title: "TIGER: Time-Series Classification with In-Context-Learning Gated Ensemble of Representations"
author:
  - literal: "Johann Faouzi"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06156"

# Custom fields
paper_id: "2610.06156"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "text-classification"
  - "in-context-learning"
  - "ensemble"
  - "benchmark"
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
processed_at: "2026-10-08T11:40:48Z"
created_at: "2026-10-08T11:40:48Z"
---

# TIGER: Time-Series Classification with In-Context-Learning Gated Ensemble of Representations

**Authors**: Johann Faouzi
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06156](https://arxiv.org/abs/2610.06156)

## Summary

TIGER introduces a time-series classification framework that extracts features using four distinct representation families, applies three general-purpose classifiers to form a meta-feature matrix, and leverages an adaptive meta-classification rule combining majority voting and TabICLv2 based on dataset characteristics. Evaluated on a 142-dataset benchmark from the UCR archive, TIGER outperforms state-of-the-art methods including HIVE-COTE 2.0 in mean accuracy, balanced accuracy, and F1-score.

## Key Contributions

- Proposes TIGER, an in-context-learning gated ensemble of representations for time series classification that applies a portfolio of general-purpose classifiers across four representation families.
- Uses an adaptive meta-classification rule combining weighted hard majority voting and TabICLv2 based on the training sample size per class.
- Achieves best mean accuracy, balanced accuracy, and F1-score across a 142-dataset UCR archive benchmark compared to six algorithms including HIVE-COTE 2.0.

## Limitations

Hyperparameters tuned on a small 20-dataset development subset; relies on combining fixed representations and general-purpose classifiers.

## Archivist Review

Reviewed all candidates against vault policies. TabICLv2 is already present in the vault under the canonical slug 'tabicl'. The open question regarding multivariate and regression extension is standard boilerplate future work and lacks specific architectural novelty. Thus, no new candidates are approved.

### Rejected Candidates
- [concept] TabICLv2 (`tabicl`) - duplicate_existing: Already present in the vault under the canonical slug 'tabicl'.
- [open_question] Multivariate and Regression Extension (`multivariate-time-series-and-regression-extension`) - low_impact: Extending univariate models to multivariate or regression tasks is standard boilerplate future work.

## Links

- [Abstract](https://arxiv.org/abs/2610.06156)
- [PDF](https://arxiv.org/pdf/2610.06156)

