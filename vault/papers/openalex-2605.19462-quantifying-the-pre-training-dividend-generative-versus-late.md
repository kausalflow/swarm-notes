---
# CSL-compatible fields
title: "Quantifying the Pre-training Dividend: Generative versus Latent Self-Supervised Learning for Time Series Foundation Models"
author:
  - literal: "Noam Major"
  - literal: "Kathy Razmadze"
  - literal: "Yoli Shavit"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.19462"

# Custom fields
paper_id: "2605.19462"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "self-supervised-learning"
  - "forecasting"
  - "anomaly-detection"
  - "classification"
  - "pre-training"
  - "foundation-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "pre-training-dividend"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:16:56Z"
created_at: "2026-05-22T08:16:56Z"
---

# Quantifying the Pre-training Dividend: Generative versus Latent Self-Supervised Learning for Time Series Foundation Models

**Authors**: Noam Major, Kathy Razmadze, Yoli Shavit
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.19462](https://arxiv.org/abs/2605.19462)

## Summary

This paper systematically evaluates the efficacy of self-supervised learning (SSL) across various time series downstream tasks, contrasting Generative and Latent Alignment paradigms. By adapting LeJEPA and DINO to incorporate Discrete Wavelet Transform augmentations, the authors find that the benefit of pre-training—termed the 'pre-training dividend'—is highly task-dependent. Their analysis reveals significant performance improvements in anomaly detection and classification but minimal impact on forecasting, underscoring a fundamental precision-invariance trade-off in learned temporal representations.

## Key Contributions

- Establishes a systematic framework to quantify the value of SSL pre-training (pre-training dividend) across forecasting, anomaly detection, and classification tasks.
- Adapts LeJEPA and DINO architectures to time series using Discrete Wavelet Transform (DWT) augmentations for local invariance.
- Demonstrates that SSL pre-training provides significant gains (up to 375%) for anomaly detection and classification, while offering only marginal improvements for forecasting.
- Identifies a precision-invariance trade-off as the governing mechanism for representational utility in time series tasks.

## Key Concepts

- [[pre-training-dividend]]: A quantitative metric measuring the utility added by self-supervised learning pre-training across a diverse set of temporal tasks.

## Archivist Review

I have approved 'Pre-training Dividend' as it introduces a novel evaluation framework for quantifying the performance gains of time series foundation models across diverse tasks. I rejected the 'Precision-Invariance Trade-off' as it functions as an interpretative finding of the study rather than a standalone methodology or architectural innovation suitable for a permanent conceptual note.

### Approved Concepts
- Pre-training Dividend: Formalizes the comparative gain of SSL pre-training across various downstream tasks beyond just forecasting.

### Rejected Candidates
- [concept] Precision-Invariance Trade-off (`precision-invariance-trade-off`) - not_novel: This is a descriptive observation of model behavior rather than a novel, reusable methodological component or architecture.

## Links

- [Abstract](https://arxiv.org/abs/2605.19462)
- [PDF](https://arxiv.org/pdf/2605.19462)

