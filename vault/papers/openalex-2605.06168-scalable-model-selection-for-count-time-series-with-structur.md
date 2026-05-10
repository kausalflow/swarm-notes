---
# CSL-compatible fields
title: "Scalable model selection for count time series with structural breaks: application to solid-organ transplantation during and after COVID-19 in the USA and Italy"
author:
  - literal: "Tobia Filosi"
  - literal: "Emiliano Ceccarelli"
  - literal: "Emilio Porcu"
  - literal: "Elena Del Sordo"
  - literal: "Libia Lara-Carrión"
  - literal: "Giuseppe Iuppa"
  - literal: "Francesca Puoti"
  - literal: "Silvia Trapani"
  - literal: "Silvia Testa"
  - literal: "Giovanna Jona Lasinio"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06168"

# Custom fields
paper_id: "2605.06168"
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
processed_at: "2026-05-10T07:20:52Z"
created_at: "2026-05-10T07:20:52Z"
---

# Scalable model selection for count time series with structural breaks: application to solid-organ transplantation during and after COVID-19 in the USA and Italy

**Authors**: Tobia Filosi, Emiliano Ceccarelli, Emilio Porcu, Elena Del Sordo, Libia Lara-Carrión, Giuseppe Iuppa, Francesca Puoti, Silvia Trapani, Silvia Testa, Giovanna Jona Lasinio
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06168](https://arxiv.org/abs/2605.06168)

## Summary

This paper addresses the challenges of forecasting non-negative healthcare count time series subjected to structural disruptions, such as the COVID-19 pandemic. The authors implement a systematic model selection approach for Poisson and negative-binomial processes that incorporates temporal dynamics, calendar effects, and structural break indicators. Through an application to organ transplantation data in the USA and Italy, the study finds that autoregressive specifications provide robust forecasting performance, outperforming models dependent on auxiliary pandemic-burden covariates. Results indicate that post-pandemic activity patterns are primarily driven by endogenous structural factors rather than external pandemic metrics.

## Key Contributions

- Develops a scalable model selection framework for count time series featuring structural breaks, tailored for non-negative weekly healthcare activity.
- Evaluates model performance across 4, 8, and 12-week horizons on US and Italian solid-organ transplantation data using an expanding-window validation design.
- Demonstrates that autoregressive and calendar-effect models effectively capture post-pandemic recovery trajectories, rendering auxiliary COVID-burden covariates statistically negligible.

## Open Questions & Future Work

- [[modeling-heterogeneous-systemic-shocks]]

## Archivist Review

The paper presents a specific application of count time-series modeling for healthcare data with structural breaks. The proposed model selection framework is a standard statistical approach (using BIC on a predefined portfolio of count models) and does not introduce a novel algorithmic concept. The open question regarding systemic shocks is valuable for the field of time-series modeling under external disruptions.

### Approved Open Questions
- Modeling Complex Systemic Shocks: This is critical because simple intervention proxies often fail to capture the nuanced, multi-phasic nature of large-scale healthcare shocks, which in turn limits the reliability of long-term predictive models and the ability of policymakers to accurately assess the resilience of medical systems.

## Links

- [Abstract](https://arxiv.org/abs/2605.06168)
- [PDF](https://arxiv.org/pdf/2605.06168)

