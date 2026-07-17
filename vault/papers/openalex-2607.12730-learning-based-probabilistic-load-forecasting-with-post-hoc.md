---
# CSL-compatible fields
title: "Learning-based Probabilistic Load Forecasting with Post-hoc and In-model Uncertainty"
author:
  - literal: "Sarah Al-Shareeda"
  - literal: "Gulcihan Ozdemir"
  - literal: "Heung Seok Jeon"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12730"

# Custom fields
paper_id: "2607.12730"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "attention-mechanism"
  - "uncertainty-aware-forecasting"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "unified-probabilistic-load-forecasting-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:10:00Z"
created_at: "2026-07-17T07:10:00Z"
---

# Learning-based Probabilistic Load Forecasting with Post-hoc and In-model Uncertainty

**Authors**: Sarah Al-Shareeda, Gulcihan Ozdemir, Heung Seok Jeon
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12730](https://arxiv.org/abs/2607.12730)

## Summary

This paper investigates the impact of input reconstruction uncertainty on one-day-ahead probabilistic load forecasting in smart buildings. The authors compare modular post-hoc residual-quantile schemes with integrated in-model quantile-learning across three deep learning architectures: recurrent models, hybrid recurrent models, and Temporal Fusion Transformers (TFT). The results reveal that integrated quantile learning with TFT backbones produces more reliable intervals and superior predictive performance compared to post-hoc methods. Furthermore, the study identifies that models do not inherently account for reconstruction-induced uncertainty, necessitating deliberate placement of uncertainty estimation within the forecasting pipeline.

## Key Contributions

- Introduces a unified probabilistic load forecasting framework that systematically addresses uncertainty propagation from input reconstruction.
- Demonstrates that integrated quantile learning significantly outperforms post-hoc residual-quantile schemes when using attention-based backbones like the Temporal Fusion Transformer.
- Quantifies the failure of standard models to automatically absorb reconstruction-induced uncertainty, highlighting that such inputs increase Quantile Score by 106% despite unchanged interval width.

## Open Questions & Future Work

- [[uncertainty-quantification-in-reconstructed-inputs]]

## Key Concepts

- [[unified-probabilistic-load-forecasting-framework]]: A forecasting architecture that explicitly addresses input reconstruction uncertainty through integrated or modular quantile learning.

## Archivist Review

The approved concept and open question capture a significant, reusable methodological challenge in modern forecasting: how to account for input-side data quality issues within probabilistic pipelines. The framework and the identified uncertainty bottleneck are central to the paper's contribution and provide a standard for evaluating future models that operate on reconstructed or sparse inputs. No datasets were approved as none were identified as primary, named, or unique beyond standard usage.

### Approved Concepts
- Unified Probabilistic Load Forecasting Framework: Provides a systematic methodology for addressing input reconstruction uncertainty propagation in forecasting pipelines, particularly when deploying models on feature-limited data.

### Approved Open Questions
- Calibrating uncertainty with reconstructed inputs: This bottleneck is critical for reliable operational scheduling, where miscalibrated intervals lead to sub-optimal resource management; tracking this distinguishes between model capacity and input-side quality limitations.

## Links

- [Abstract](https://arxiv.org/abs/2607.12730)
- [PDF](https://arxiv.org/pdf/2607.12730)

