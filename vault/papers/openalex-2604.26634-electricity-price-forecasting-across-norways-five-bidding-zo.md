---
# CSL-compatible fields
title: "Electricity price forecasting across Norway's five bidding zones in the post-crisis era"
author:
  - literal: "My Thi Diem Phan"
  - literal: "Trung Tuyen Truong"
  - literal: "Hoai Phuong Ha"
  - literal: "Dat Thanh Nguyen"
issued:
  date-parts:
    - [2026, 4, 29]
url: "https://arxiv.org/abs/2604.26634"

# Custom fields
paper_id: "2604.26634"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-02T06:56:24Z"
created_at: "2026-05-02T06:56:24Z"
---

# Electricity price forecasting across Norway's five bidding zones in the post-crisis era

**Authors**: My Thi Diem Phan, Trung Tuyen Truong, Hoai Phuong Ha, Dat Thanh Nguyen
**Date**: 2026-04-29
**Paper ID**: [openalex:2604.26634](https://arxiv.org/abs/2604.26634)

## Summary

This paper evaluates electricity price forecasting across Norway's five bidding zones, addressing challenges posed by the post-2021 energy crisis and increased integration with Continental Europe. Using a novel 2019-2025 hourly multimodal dataset, the authors compare eight forecasting approaches, including LightGBM, ARX, and deep learning models. The findings reveal that tree-based models like LightGBM currently offer the best performance, while regime-specific analysis highlights the necessity of incorporating exogenous variables like reservoir levels to manage risk during periods of high market volatility.

## Key Contributions

- Presents a comprehensive benchmarking of eight forecasting model families across all five Norwegian Nord Pool bidding zones using a 2019-2025 multimodal hourly dataset.
- Demonstrates that LightGBM consistently outperforms other architectures, while ridge ARX remains highly competitive in northern regions.
- Shows through feature ablation and conditional regime analysis that while lagged prices are sufficient for general accuracy, external features like reservoir levels are critical for performance during stressed market regimes.

## Open Questions & Future Work

- [[probabilistic-electricity-price-forecasting]]

## Archivist Review

The paper provides a localized empirical benchmarking study of electricity price forecasting models. No novel, reusable forecasting methodology, architectural innovation, or unique theoretical concept was presented that would generalize beyond the study of the Norwegian energy market. Consequently, the concepts were rejected, but the open question regarding the necessity of transitioning from point forecasting to probabilistic frameworks in volatile energy markets was approved as it reflects a broader, persistent limitation in time-series forecasting.

### Approved Open Questions
- Probabilistic electricity price forecasting: Current models, while accurate on average, are consistently vulnerable to extreme, fast-moving price spikes that cause significant operational and financial risk. Probabilistic forecasting is essential for risk management and robust decision-making in volatile energy markets.

## Links

- [Abstract](https://arxiv.org/abs/2604.26634)
- [PDF](https://arxiv.org/pdf/2604.26634)

