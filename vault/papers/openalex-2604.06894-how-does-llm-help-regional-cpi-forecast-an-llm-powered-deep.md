---
# CSL-compatible fields
title: "How Does LLM Help Regional CPI Forecast: An LLM-powered Deep Panel Modeling Framework"
author:
  - literal: "Tianchen Gao"
  - literal: "Ao Sun"
  - literal: "Yurou Wang"
  - literal: "Jingyuan Liu"
  - literal: "Chêng Hsiao"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.06894"

# Custom fields
paper_id: "2604.06894"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "bert"
  - "gpt"
  - "time-series"
  - "forecasting"
  - "conformal-prediction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "residual-joint-modeling-framework"
  - "region-wise-homogeneity-pursuit"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:54:51Z"
created_at: "2026-04-11T05:54:51Z"
---

# How Does LLM Help Regional CPI Forecast: An LLM-powered Deep Panel Modeling Framework

**Authors**: Tianchen Gao, Ao Sun, Yurou Wang, Jingyuan Liu, Chêng Hsiao
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.06894](https://arxiv.org/abs/2604.06894)

## Summary

This paper introduces a residual-joint-modeling framework that enhances regional Consumer Price Index (CPI) forecasting by integrating LLM-derived surrogates from social media data with traditional panel modeling. By leveraging GPT and fine-tuned BERT models to process high-frequency narrative data, the framework captures rapid economic fluctuations often missed by low-frequency macroeconomic indicators. The approach further incorporates a region-wise homogeneity pursuit mechanism and conformal-based prediction intervals to ensure robust performance and uncertainty quantification. Empirical results demonstrate significant improvements in forecast accuracy and responsiveness to inflationary shifts compared to standard econometric benchmarks.

## Key Contributions

- Proposes a residual-joint-modeling framework that integrates high-frequency LLM-induced surrogates from social media into regional CPI panel modeling.
- Introduces a deep panel learning procedure with region-wise homogeneity pursuit to solve joint forecasting objectives.
- Outperforms traditional econometric models in capturing abrupt inflationary shifts and reducing short-term forecasting errors while providing conformal-based prediction intervals.

## Key Concepts

- [[residual-joint-modeling-framework]]: A framework for integrating large language model-derived narrative surrogates with traditional panel modeling to enhance time-series forecasting.
- [[region-wise-homogeneity-pursuit]]: A panel learning technique that enforces or learns regional similarities to improve forecasting performance and parameter estimation.

## Archivist Review

I approved the residual-joint-modeling framework and region-wise homogeneity pursuit because they represent distinct, reusable methodological contributions to the intersection of deep learning and econometric panel modeling. I rejected the collection of Sina Weibo data as it is a specific domain-local dataset instance rather than a foundational or widely used benchmark. The review applied strict filtering to ensure only high-level mechanisms were selected over implementation-specific tasks.

### Approved Concepts
- Residual-joint-modeling framework: Provides a structured approach to bridge high-frequency LLM-extracted signals with low-frequency traditional econometric panel data.
- Region-wise homogeneity pursuit: Addresses the challenge of modeling heterogeneity in panel data by learning regional clusters or similarities within a deep learning framework.

## Links

- [Abstract](https://arxiv.org/abs/2604.06894)
- [PDF](https://arxiv.org/pdf/2604.06894)

