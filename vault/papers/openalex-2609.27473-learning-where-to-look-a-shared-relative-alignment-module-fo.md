---
# CSL-compatible fields
title: "Learning Where to Look: A Shared Relative-Alignment Module for Time-Series Forecasting and PPG-to-Vital-Sign Reconstruction"
author:
  - literal: "Ragamayi Puli"
  - literal: "Shunya Nagashima"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27473"

# Custom fields
paper_id: "2609.27473"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "rooster"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:36:46Z"
created_at: "2026-09-26T09:36:46Z"
---

# Learning Where to Look: A Shared Relative-Alignment Module for Time-Series Forecasting and PPG-to-Vital-Sign Reconstruction

**Authors**: Ragamayi Puli, Shunya Nagashima
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27473](https://arxiv.org/abs/2609.27473)

## Summary

This paper introduces ROOSTER, a shared conditioning module designed to bridge multivariate time-series forecasting and PPG-to-vital-sign reconstruction by learning cross-sequence alignments. Instead of hard-coding alignments like same-position copying or seasonal recurrence, ROOSTER uses a periodic-comb bias over target-condition offsets with learnable center, period, and sharpness per head. Empirical evaluations show that ROOSTER outperforms baseline methods across multiple heart-rate and respiratory-rate reconstruction benchmarks as well as standard multivariate time-series forecasting benchmarks. Ablation experiments confirm that the learned relative bias is the primary driver of effective alignment rather than standard content matching.

## Key Contributions

- Proposed ROOSTER, a shared conditioning module featuring a periodic-comb bias over target-condition offsets that handles both vital-sign reconstruction and time-series forecasting.
- Outperformed published baselines on four heart-rate and respiratory-rate vital-sign reconstruction benchmarks from PPG.
- Achieved the best horizon-averaged MSE on four multivariate time-series forecasting benchmarks and outperformed the baseline model across 20 of 24 dataset-horizon settings.

## Open Questions & Future Work

- [[robust-alignment-corrupted-correspondence]]

## Key Concepts

- [[rooster]]: A shared relative-alignment conditioning module using a periodic-comb bias over target-condition offsets for time-series forecasting and PPG-to-vital-sign reconstruction.

## Archivist Review

Approved the overarching ROOSTER conditioning module concept and its explicitly noted open research question regarding robustness under corrupted correspondence, adhering strictly to the selectivity and quality thresholds.

### Approved Concepts
- ROOSTER: ROOSTER introduces a novel shared relative-alignment conditioning module using a periodic-comb bias over target-condition offsets, bridging time-series forecasting and PPG-to-vital-sign reconstruction.

### Approved Open Questions
- Robust Conditioning Under Corrupted Correspondence: Addressing motion-induced corruption is critical for deploying wearable vital-sign reconstruction models reliably in unconstrained, real-world free-living environments.

## Links

- [Abstract](https://arxiv.org/abs/2609.27473)
- [PDF](https://arxiv.org/pdf/2609.27473)

