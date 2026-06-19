---
# CSL-compatible fields
title: "Low-Cost Home Automation System for Municipal Swimming Pool: Arduino-Based Implementation and Data Analysis"
author:
  - literal: "Júlio Rocha"
  - literal: "Salviano Soares"
  - literal: "Carlos Quental"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.18038"

# Custom fields
paper_id: "2606.18038"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
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
processed_at: "2026-06-19T09:25:26Z"
created_at: "2026-06-19T09:25:26Z"
---

# Low-Cost Home Automation System for Municipal Swimming Pool: Arduino-Based Implementation and Data Analysis

**Authors**: Júlio Rocha, Salviano Soares, Carlos Quental
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.18038](https://arxiv.org/abs/2606.18038)

## Summary

This paper introduces a low-cost, Arduino-driven automation framework designed to monitor and control municipal swimming pool environments. The system captures diverse sensor data—including air quality, gas leakage, and environmental climate parameters—and streams it to a centralized web API for storage and visualization. Through statistical analysis of the resulting time-series data, the system aims to improve energy efficiency and operational decision-making.

## Key Contributions

- Designed and implemented a low-cost, Arduino-based automation system for municipal swimming pool management.
- Developed an integrated pipeline for real-time sensor data collection, transmission to a web API, and storage in a time-series database.
- Conducted comprehensive statistical data analysis using Python-based tools to support facility management decision-making.

## Open Questions & Future Work

- [[long-term-iot-monitoring-variability]]

## Archivist Review

This paper describes a specific application of IoT sensors for municipal pool management. I have rejected the proposed automation system as a concept because it is an implementation of existing technology rather than a novel or highly reusable methodological framework. I have approved the open question regarding monitoring duration, as it addresses a fundamental, recurring bottleneck in practical environmental data analysis.

### Approved Open Questions
- Long-term IoT Environmental Monitoring: Short observation windows risk failing to capture significant seasonal or usage-driven variability, which can lead to misguided operational decisions and infrastructure management strategies.

### Rejected Candidates
- [concept] Low-cost Home Automation System (`low-cost-home-automation-system`) - generic: This is a generic description of an application rather than a reusable methodological concept.

## Links

- [Abstract](https://arxiv.org/abs/2606.18038)
- [PDF](https://arxiv.org/pdf/2606.18038)

