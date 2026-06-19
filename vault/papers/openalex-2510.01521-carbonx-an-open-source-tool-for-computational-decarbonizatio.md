---
# CSL-compatible fields
title: "CarbonX: An Open-Source Tool for Computational Decarbonization Using Time Series Foundation Models"
author:
  - literal: "Diptyaroop Maji"
  - literal: "Kang Yang"
  - literal: "Prashant Shenoy"
  - literal: "Ramesh K. Sitaraman"
  - literal: "Mani Srivastava"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2510.01521"

# Custom fields
paper_id: "2510.01521"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:24:20Z"
created_at: "2026-06-19T09:24:20Z"
---

# CarbonX: An Open-Source Tool for Computational Decarbonization Using Time Series Foundation Models

**Authors**: Diptyaroop Maji, Kang Yang, Prashant Shenoy, Ramesh K. Sitaraman, Mani Srivastava
**Date**: 2026-06-16
**Paper ID**: [openalex:2510.01521](https://arxiv.org/abs/2510.01521)

## Summary

CarbonX is an open-source framework designed to facilitate computational decarbonization across data centers, transportation, and built environments. By utilizing time series foundation models, the tool provides accurate carbon intensity forecasts with associated uncertainty estimates, addressing the lack of global grid data. This approach eliminates the dependency on region-specific electricity mix information and provides a unified, reliable solution for carbon-aware operational scheduling.

## Key Contributions

- Introduces CarbonX, an open-source tool for computational decarbonization that provides carbon intensity forecasting without requiring grid-specific electricity mix data.
- Leverages time series foundation models to enable global coverage of carbon intensity prediction by bypassing the need for location-specific manual grid modeling.
- Integrates uncertainty estimation into carbon intensity forecasts to enhance the reliability of carbon-aware scheduling and downstream decision-making applications.

## Open Questions & Future Work

- [[tsfm-scaling-performance-relationship]]
- [[optimizing-tsfm-domain-fine-tuning]]

## Archivist Review

The paper introduces a framework (CarbonX) that functions primarily as an application-level tool, using existing Time Series Foundation Model (TSFM) paradigms rather than introducing a distinct, reusable architectural innovation or conceptual mechanism. Consequently, no new concepts were approved. The identified open questions regarding TSFM scaling and fine-tuning are substantial and trackable bottlenecks in the broader field of foundation models for time series, justifying their inclusion in the vault.

### Approved Open Questions
- TSFM Scaling Performance Relationship: Understanding TSFM scaling behavior is critical for deploying efficient, reliable models in resource-constrained infrastructure applications like decarbonization.
- Optimizing TSFM Domain Fine-Tuning: Establishing robust, reliable fine-tuning recipes is essential to bridge the gap between zero-shot foundation model performance and task-specific accuracy in sensitive infrastructure domains.

## Links

- [Abstract](https://arxiv.org/abs/2510.01521)
- [PDF](https://arxiv.org/pdf/2510.01521)

