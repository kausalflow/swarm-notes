---
# CSL-compatible fields
title: "End-to-End Learning for Partially-Observed Time Series with PyPOTS"
author:
  - literal: "Wenjie Du"
  - literal: "Yiyuan Yang"
  - literal: "Tianxiang Zhan"
  - literal: "Qingsong Wen"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.24041"

# Custom fields
paper_id: "2604.24041"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "forecasting"
  - "time-classification"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "pypots"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:23:47Z"
created_at: "2026-04-30T07:23:47Z"
---

# End-to-End Learning for Partially-Observed Time Series with PyPOTS

**Authors**: Wenjie Du, Yiyuan Yang, Tianxiang Zhan, Qingsong Wen
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.24041](https://arxiv.org/abs/2604.24041)

## Summary

The paper introduces PyPOTS, an open-source ecosystem designed to streamline the handling of partially-observed time series data by integrating missing-value imputation with downstream machine learning tasks. Traditional pipelines often separate these processes, which hinders performance and reproducibility; PyPOTS addresses this by providing unified APIs for imputation, forecasting, classification, clustering, and anomaly detection. The toolkit includes practical workflows for both practitioners and researchers to build robust, transparent, and reproducible time-series pipelines.

## Key Contributions

- Introduces PyPOTS, an open-source Python ecosystem that unifies missing-value handling with downstream tasks like forecasting and classification for partially-observed time series.
- Provides standardized workflows for missingness simulation, data preprocessing, and model training via a unified API.
- Facilitates research reproducibility by offering benchmark-oriented experiments for evaluation across multiple time-series tasks.

## Open Questions & Future Work

- [[unified-end-to-end-pots-learning]]

## Key Concepts

- [[pypots]]: An open-source Python ecosystem designed for end-to-end machine learning on partially-observed time series data.

## Archivist Review

I have approved the PyPOTS ecosystem as it provides a standardized framework for an important, recurring challenge in time-series analysis: end-to-end learning with partially observed data. I also approved the open question regarding unified POTS learning to track the research movement toward integrated imputation and downstream task modeling. No other candidates met the high bar for permanent archival in the knowledge vault.

### Approved Concepts
- PyPOTS: It acts as a centralized ecosystem for managing the end-to-end pipeline of partially-observed time series data, which is historically fragmented.

### Approved Open Questions
- Unified End-to-End POTS Learning: The transition from fragmented to end-to-end learning is critical for improving both the accuracy and the reproducibility of machine learning models trained on real-world, incomplete time series data.

## Links

- [Abstract](https://arxiv.org/abs/2604.24041)
- [PDF](https://arxiv.org/pdf/2604.24041)

