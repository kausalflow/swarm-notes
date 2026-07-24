---
# CSL-compatible fields
title: "In-Context Time Series Classification with Random Convolutional Features"
author:
  - literal: "Joscha Cüppers"
  - literal: "Jilles Vreeken"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.19234"

# Custom fields
paper_id: "2607.19234"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "in-context-learning"
  - "foundation-model"
  - "few-shot-learning"
  - "zero-shot-learning"
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
processed_at: "2026-07-24T07:24:51Z"
created_at: "2026-07-24T07:24:51Z"
---

# In-Context Time Series Classification with Random Convolutional Features

**Authors**: Joscha Cüppers, Jilles Vreeken
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.19234](https://arxiv.org/abs/2607.19234)

## Summary

Time series classification often relies on feature extraction or heavy task-specific training. This paper introduces MASHT, a zero-shot pipeline that pairs random convolutional features from MultiRocket and Hydra with pretrained in-context tabular foundation models. By bypassing explicit model training entirely, MASHT matches or exceeds strong traditional baselines like HIVE-COTE 2.0 on univariate tasks while remaining competitive on multivariate benchmarks.

## Key Contributions

- Proposes MASHT, a pipeline combining MultiRocket and Hydra random convolutional features with pretrained in-context tabular foundation models for zero-shot time series classification.
- Bypasses task-specific model training entirely, relying solely on feature extraction and direct in-context inference.
- Achieves lower average rank than HIVE-COTE 2.0 on univariate tasks and remains highly competitive on multivariate datasets.

## Limitations

Future work could explore scaling to larger tabular foundation models and expanding to more diverse time series downstream tasks.

## Archivist Review

The proposed concept (MASHT) and open question were carefully evaluated against vault standards. MASHT represents a specific pipeline configuration combining existing feature extractors with tabular foundation models rather than an independently reusable architectural mechanism, and the open question calls for routine runtime benchmarking rather than addressing a deep theoretical or methodological barrier. Therefore, no items were approved.

### Rejected Candidates
- [concept] MASHT (`masht`) - paper_local: The MASHT pipeline is a paper-local combination of existing feature extractors (MultiRocket, Hydra) and existing tabular foundation models, lacking standalone foundational novelty.
- [open_question] Standardized Efficiency Comparisons for Time Series Classification (`standardized-efficiency-comparisons-time-series-classification`) - low_impact: This is a routine call for runtime and efficiency benchmarks rather than a deep theoretical or methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.19234)
- [PDF](https://arxiv.org/pdf/2607.19234)

