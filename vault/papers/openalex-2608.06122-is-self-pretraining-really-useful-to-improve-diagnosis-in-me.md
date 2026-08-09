---
# CSL-compatible fields
title: "Is Self-Pretraining really useful to improve diagnosis in medical Time Series?"
author:
  - literal: "Omar Coser"
  - literal: "Antonio Orvieto"
  - literal: "Paolo Soda"
  - literal: "Loredana Zollo"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.06122"

# Custom fields
paper_id: "2608.06122"
paper_source: "openalex"
domain: "medicine"
tags:
  - "transformer"
  - "pre-training"
  - "time-series"
  - "multimodal"
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
processed_at: "2026-08-09T05:40:05Z"
created_at: "2026-08-09T05:40:05Z"
---

# Is Self-Pretraining really useful to improve diagnosis in medical Time Series?

**Authors**: Omar Coser, Antonio Orvieto, Paolo Soda, Loredana Zollo
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.06122](https://arxiv.org/abs/2608.06122)

## Summary

This paper investigates whether self-pretraining (SPT) enhances transformer-based models for medical time-series diagnosis across univariate, multivariate, and multimodal settings. By employing masking-based objectives on datasets such as Camargo, Non-EEG Stress, and Gait Parkinson's Disease, the authors find that SPT consistently boosts classification accuracy, especially as model depth increases. The findings highlight self-pretraining as a robust strategy to improve data-limited clinical diagnostics without requiring specialized architectural changes.

## Key Contributions

- Evaluated self-pretraining (SPT) across multimodal, multivariate, and univariate medical time-series benchmarks including Camargo, Non-EEG Stress, and Gait Parkinson's Disease.
- Demonstrated that SPT using masking-based objectives consistently improves classification accuracy by 0 to 6 percentage points.
- Showed that performance gains from SPT scale positively with model depth and capacity under data-limited clinical settings.

## Open Questions & Future Work

- [[spt-variable-length-irregular-medical-time-series]]

## Archivist Review

The paper explores self-pretraining (SPT) for medical time-series classification using transformers. No concepts or datasets met the rigorous threshold for permanent vault notes, and the open question was rejected due to its speculative nature regarding future tasks.

### Approved Open Questions
- SPT on Irregular Time Series: Medical time-series data naturally exhibit irregular sampling intervals and variable sequence lengths, making the expansion of SPT beyond fixed-length classification critical for practical clinical deployment.

### Rejected Candidates
- [open_question] SPT on Irregular Time Series (`spt-variable-length-irregular-medical-time-series`) - weak_evidence: The candidate was evaluated against vault criteria and rejected because it touches on standard future work directions without defining a concrete, reusable methodological gap.

## Links

- [Abstract](https://arxiv.org/abs/2608.06122)
- [PDF](https://arxiv.org/pdf/2608.06122)

