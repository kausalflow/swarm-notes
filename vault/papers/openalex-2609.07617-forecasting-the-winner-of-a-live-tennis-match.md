---
# CSL-compatible fields
title: "Forecasting the Winner of a Live Tennis Match"
author:
  - literal: "Charles Xie"
  - literal: "Aneesh Muppidi"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.07617"

# Custom fields
paper_id: "2609.07617"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:16:22Z"
created_at: "2026-09-10T09:16:22Z"
---

# Forecasting the Winner of a Live Tennis Match

**Authors**: Charles Xie, Aneesh Muppidi
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.07617](https://arxiv.org/abs/2609.07617)

## Summary

This study investigates live tennis match winner forecasting by effectively integrating pre-match statistics and real-time in-game data across over 1.5 million points from Grand Slam matches. Five distinct models were evaluated on a chronological train-validation-test split. The proposed hybrid model, Trace, demonstrated strong predictive performance, achieving win-probability accuracy milestones of 76.06%, 82.15%, and 88.34% at 25%, 50%, and 75% of match progress.

## Key Contributions

- Evaluated five models on 8,222 Grand Slam matches comprising over 1.5 million points using a chronological split (2011-2021 training, 2022 validation, 2023-2024 testing)
- Proposed and tested a hybrid forecasting model named Trace that integrates pre-match and live information
- Achieved live prediction accuracies of 76.06%, 82.15%, and 88.34% at 25%, 50%, and 75% match progress respectively

## Open Questions & Future Work

- [[comprehensive-live-tennis-features]]

## Archivist Review

Adhered strictly to the scarcity principle. No concepts met the high bar for reusable foundational machine learning methodology. One open question regarding live tennis features was approved as it details specific limitations in sports forecasting features and scope.

### Approved Open Questions
- Comprehensive Live Tennis Features: Incorporating multi-faceted contextual features and surface-specific metrics is critical for improving generalizability and accuracy across diverse professional tennis tournaments.

### Rejected Candidates
- [dataset] Grand Slam matches dataset (`grand-slam-matches-dataset`) - low_impact: The dataset is described generically as Grand Slam matches without a distinct, standard open repository name or canonical identifier.

## Links

- [Abstract](https://arxiv.org/abs/2609.07617)
- [PDF](https://arxiv.org/pdf/2609.07617)

