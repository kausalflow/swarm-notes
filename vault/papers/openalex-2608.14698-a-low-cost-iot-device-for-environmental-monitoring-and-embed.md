---
# CSL-compatible fields
title: "A Low-Cost IoT Device for Environmental Monitoring and Embedded Solar Forecasting with On-Device Incremental Learning"
author:
  - literal: "Erick Michel Lara Pinal"
  - literal: "Abhinav Das"
  - literal: "Stephan Schlüter"
issued:
  date-parts:
    - [2026, 8, 30]
url: "https://arxiv.org/abs/2608.14698"

# Custom fields
paper_id: "2608.14698"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-01T09:41:07Z"
created_at: "2026-09-01T09:41:07Z"
---

# A Low-Cost IoT Device for Environmental Monitoring and Embedded Solar Forecasting with On-Device Incremental Learning

**Authors**: Erick Michel Lara Pinal, Abhinav Das, Stephan Schlüter
**Date**: 2026-08-30
**Paper ID**: [openalex:2608.14698](https://arxiv.org/abs/2608.14698)

## Summary

This paper presents a low-cost ($65 USD) ESP32-based IoT device for hyperlocal meteorological sensing and embedded solar photovoltaic voltage forecasting. The system uses a lightweight 3011-parameter feedforward neural network that performs on-device inference every 15 minutes based on 96 historical readings. An on-device incremental gradient descent mechanism allows the model to adapt post-deployment without cloud connectivity, yielding statistically significant accuracy improvements over frozen-weight models during a 115-day field deployment.

## Key Contributions

- Developed a modular ESP32-based IoT environmental monitoring and solar forecasting device costing ~$65 USD with an IP68-rated enclosure.
- Designed an on-device incremental learning mechanism using gradient descent that enables model adaptation on low-cost microcontrollers without cloud connectivity.
- Evaluated the system over a 115-day field deployment in Zapopan, Mexico, achieving a coefficient of determination of 0.9165 and a mean absolute error of 0.2975 V over a 28-day clean window.
- Demonstrated that the on-device update mechanism yields a statistically significant accuracy gain (p=0.001) compared to a frozen-weight baseline.

## Archivist Review

The paper describes an IoT hardware implementation with a standard feedforward neural network and incremental gradient descent on an ESP32 microcontroller. The proposed open question focuses on hardware sensor selection rather than an enduring algorithmic research bottleneck. Following the strict selectivity policy and zero-approval standard for paper-local hardware designs, no permanent concepts or open questions were approved.

### Rejected Candidates
- [open_question] Quantitative Irradiance Sensor Integration (`quantitative-irradiance-sensor-integration`) - low_impact: This question focuses on hardware sensor replacement rather than a fundamental algorithmic or machine learning limitation.

## Links

- [Abstract](https://arxiv.org/abs/2608.14698)
- [PDF](https://arxiv.org/pdf/2608.14698)

