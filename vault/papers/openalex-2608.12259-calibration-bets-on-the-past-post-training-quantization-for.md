---
# CSL-compatible fields
title: "Calibration Bets on the Past: Post-Training Quantization for Financial Time-Series Forecasting"
author:
  - literal: "Junyi Ye"
  - literal: "Ivy Gateri Wanjiku"
issued:
  date-parts:
    - [2026, 8, 12]
url: "https://arxiv.org/abs/2608.12259"

# Custom fields
paper_id: "2608.12259"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "model-compression"
  - "quantization"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-15T05:14:48Z"
created_at: "2026-08-15T05:14:48Z"
---

# Calibration Bets on the Past: Post-Training Quantization for Financial Time-Series Forecasting

**Authors**: Junyi Ye, Ivy Gateri Wanjiku
**Date**: 2026-08-12
**Paper ID**: [openalex:2608.12259](https://arxiv.org/abs/2608.12259)

## Summary

This paper presents a systematic study of activation calibration for post-training quantization (PTQ) in cross-sectional volatility forecasting on the S&amp;P 500, evaluating 560 models across seven neural architectures and eight walk-forward test years. The authors find that activation calibration minimally impacts 8-bit quantization but acts as the primary performance determinant at 4 bits. Replacing default absolute-maximum calibration with percentile calibration substantially recovers lost predictive performance, highlighting activation calibration as a critical deployment decision for financial time-series forecasting.

## Key Contributions

- Demonstrated that activation calibration has little effect at 8 bits but becomes the primary determinant of predictive performance at 4 bits in financial forecasting PTQ.
- Showed that default absolute-maximum calibration of 4-bit weights and activations removes 11-62% of the full-precision mean information coefficient across affected architectures.
- Found that replacing absolute-maximum with percentile calibration recovers 53-94% of the performance degradation in the four most affected architectures.
- Evaluated 560 trained models across seven neural architectures and eight walk-forward test years (2018-2025) on S&amp;P 500 cross-sectional volatility forecasting.

## Archivist Review

Applied strict selectivity standards, rejecting the single candidate because it represents a straightforward adaptation of existing LLM quantization methods to time-series architectures rather than a deep foundational bottleneck.

### Rejected Candidates
- [open_question] Advanced PTQ Methods for Time-Series (`advanced-ptq-methods-for-time-series`) - low_impact: The question is a routine transfer experiment of existing LLM quantization techniques to time-series architectures rather than a foundational unresolved bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.12259)
- [PDF](https://arxiv.org/pdf/2608.12259)

