---
# CSL-compatible fields
title: "A Resilient Solution for Sewer Overflow Monitoring across Cloud and Edge"
author:
  - literal: "Vipin Singh"
  - literal: "Tianheng Ling"
  - literal: "Peter Ghaly"
  - literal: "Felix Grimmeisen"
  - literal: "Gregor Schiele"
  - literal: "Felix Bießmann"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10592"

# Custom fields
paper_id: "2605.10592"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:38:46Z"
created_at: "2026-05-14T07:38:46Z"
---

# A Resilient Solution for Sewer Overflow Monitoring across Cloud and Edge

**Authors**: Vipin Singh, Tianheng Ling, Peter Ghaly, Felix Grimmeisen, Gregor Schiele, Felix Bießmann
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10592](https://arxiv.org/abs/2605.10592)

## Summary

This paper addresses the critical environmental issue of combined sewer overflows (CSO) by proposing a hybrid cloud-edge monitoring and forecasting system. The system enables the prediction of filling dynamics in overflow basins to mitigate capacity exceedance during extreme weather events. By deploying deep learning models on both cloud infrastructure and edge devices, the framework ensures operational resilience and continued monitoring capability during intermittent network outages.

## Key Contributions

- Developed a web-based demonstrator for real-time combined sewer overflow (CSO) monitoring and basin filling dynamics forecasting.
- Integrated deep learning-based forecasting pipelines into both cloud and edge environments.
- Designed an interactive monitoring framework that maintains resilient functionality during network outages by utilizing edge-side inference.

## Open Questions & Future Work

- [[robustness-sewer-monitoring-data-anomalies]]

## Archivist Review

The paper focuses on an application-specific deployment of cloud-edge forecasting for sewer systems. As the framework does not introduce a novel forecasting architecture or a distinct theoretical contribution to time-series methodology, I have rejected all concept candidates. The identified open question regarding robustness to data anomalies in safety-critical monitoring is a valid research direction worthy of tracking.

### Approved Open Questions
- Robustness of Sewer Forecasting Models: Sewer overflow management is safety-critical; understanding how forecasting models degrade or recover in the presence of real-world sensor anomalies is essential for reliable decision-making.

## Links

- [Abstract](https://arxiv.org/abs/2605.10592)
- [PDF](https://arxiv.org/pdf/2605.10592)

