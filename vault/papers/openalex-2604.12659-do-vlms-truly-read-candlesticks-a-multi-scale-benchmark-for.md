---
# CSL-compatible fields
title: "Do VLMs Truly \"Read\" Candlesticks? A Multi-Scale Benchmark for Visual Stock Price Forecasting"
author:
  - literal: "Kaiqi Hu"
  - literal: "Linda Xiao"
  - literal: "Shiyue Xu"
  - literal: "Ziyi Tang"
  - literal: "Mingwen Liu"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2604.12659"

# Custom fields
paper_id: "2604.12659"
paper_source: "openalex"
domain: "finance"
tags:
  - "multimodal"
  - "vision-language-model"
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "multi-scale-candlestick-charts-dataset"
concept_slugs:
  []
dataset_slugs:
  - "multi-scale-candlestick-charts-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:29:16Z"
created_at: "2026-04-17T06:29:16Z"
---

# Do VLMs Truly "Read" Candlesticks? A Multi-Scale Benchmark for Visual Stock Price Forecasting

**Authors**: Kaiqi Hu, Linda Xiao, Shiyue Xu, Ziyi Tang, Mingwen Liu
**Date**: 2026-04-14
**Paper ID**: [openalex:2604.12659](https://arxiv.org/abs/2604.12659)

## Summary

This paper investigates whether Vision-Language Models (VLMs) genuinely comprehend visual candlestick patterns for stock price forecasting. The authors introduce a multi-scale dataset and a rigorous evaluation framework to test if models can integrate information from different time horizons. Experimental results reveal that VLMs struggle with common market scenarios and show limited temporal reasoning, often failing to adapt to specified forecast horizons.

## Key Contributions

- Constructs a multi-scale candlestick chart dataset designed to test VLM integration of disparate temporal market dynamics.
- Introduces a standardized evaluation framework utilizing confusion-matrix diagnostics and IC metrics to probe VLM temporal reasoning capabilities.
- Demonstrates that current state-of-the-art VLMs exhibit strong performance biases toward persistent trends and lack precise temporal sensitivity to specified forecast horizons.

## Open Questions & Future Work

- [[vlm-financial-chart-reasoning-capability]]

## Archivist Review

The paper identifies a significant gap in evaluating whether VLMs actually understand financial charts rather than just performing superficial pattern matching. I approved the new multi-scale candlestick dataset as a reusable resource for the community. The open question was refined to emphasize the need for semantic-level evaluation of financial concepts, which is a critical bottleneck in deploying multimodal models for technical analysis.

### Approved Open Questions
- Evaluating VLM Financial Chart Reasoning: Distinguishing between surface-level pattern matching and conceptual understanding is necessary to build trustworthy financial decision-support systems.

### Rejected Candidates
- [dataset] Multi-scale Candlestick Charts Dataset (`multi-scale-candlestick-charts-dataset`) - other: The dataset is approved, but the concept/framework surrounding it was not sufficiently distinct or reusable outside this specific VLM-finance context.

## Datasets

- [[multi-scale-candlestick-charts-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2604.12659)
- [PDF](https://arxiv.org/pdf/2604.12659)

