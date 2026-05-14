---
# CSL-compatible fields
title: "Yield Curve Forecasting using Machine Learning and Econometrics: A Comparative Analysis"
author:
  - literal: "Aman Singh"
  - literal: "Tokunbo Ogunfunmi"
  - literal: "Sanjiv Das"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.09842"

# Custom fields
paper_id: "2605.09842"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "rnn"
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
processed_at: "2026-05-14T07:37:20Z"
created_at: "2026-05-14T07:37:20Z"
---

# Yield Curve Forecasting using Machine Learning and Econometrics: A Comparative Analysis

**Authors**: Aman Singh, Tokunbo Ogunfunmi, Sanjiv Das
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.09842](https://arxiv.org/abs/2605.09842)

## Summary

This paper investigates the performance of diverse forecasting methodologies on U.S. Treasury yield curve data spanning 47 years. The study compares classical econometrics, including ARIMA and naive benchmarks, against modern machine learning and deep learning approaches like transformers and RNNs. Results indicate that traditional econometric methods remain robust for this specific financial domain, although specific machine learning models like TimeGPT and LightGBM show competitive performance. Additionally, the study assesses the impact of data stationarity on the efficacy of deep learning model inputs.

## Key Contributions

- Performs a comprehensive comparative evaluation of classical econometric, machine learning, and deep learning models on 47 years of U.S. Treasury yield curve data.
- Demonstrates that traditional econometric models like ARIMA and naive baselines generally outperform modern machine learning architectures on yield curve forecasting tasks.
- Identifies TimeGPT, LightGBM, and RNNs as the most effective machine learning-based approaches for yield curve modeling.

## Open Questions & Future Work

- [[foundation-model-fine-tuning-finance]]

## Archivist Review

The paper presents a comparative analysis between established econometric models and modern machine learning/deep learning techniques on long-term Treasury yield curve data. As the core findings reinforce the robustness of classical methods, no new architectural concepts warranting a standalone note emerged. The open question regarding the fine-tuning utility of foundation models in specialized financial domains is approved as it addresses a key unresolved bottleneck in the practical deployment of modern time-series foundation models.

### Approved Open Questions
- Foundation Model Fine-tuning Utility: Financial time-series, particularly yield curves, possess unique structural properties; evaluating whether foundation models can adapt through fine-tuning is crucial for determining their practical utility in bond market applications versus traditional ARIMA-based methods.

### Rejected Candidates
- [open_question] Foundation Model Fine-tuning Utility (`foundation-model-fine-tuning-finance`) - other: This question was approved. (Correction: The UI requires rejecting rejected items, I am not rejecting this.)

## Links

- [Abstract](https://arxiv.org/abs/2605.09842)
- [PDF](https://arxiv.org/pdf/2605.09842)

