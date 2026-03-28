---
# CSL-compatible fields
title: "Learning Response-Statistic Shifts and Parametric Roll Episodes from Wave--Vessel Time Series via LSTM Functional Models"
author:
  - literal: "José del Águila Ferrandis"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24431"

# Custom fields
paper_id: "2603.24431"
paper_source: "openalex"
domain: "time-series"
tags:
  - "lstm"
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "robustness"
  - "evaluation"
architectures:
  - "lstm"
datasets:
  []
concept_slugs:
  - "parametric-roll-episode-learning"
  - "response-statistic-shift-modeling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:06Z"
created_at: "2026-03-28T05:29:06Z"
---

# Learning Response-Statistic Shifts and Parametric Roll Episodes from Wave--Vessel Time Series via LSTM Functional Models

**Authors**: José del Águila Ferrandis
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24431](https://arxiv.org/abs/2603.24431)

## Summary

This paper introduces a stacked LSTM functional model designed to learn the nonlinear, causal mapping from incident wave time series to vessel motions, specifically targeting the rare phenomenon of parametric roll instability. The surrogate is trained on wave-elevation data, synthesized from a modified Pierson--Moskowitz spectrum via URANS simulation, and is evaluated on its ability to replicate both the time-domain trajectory and the resulting shifts in response probability density functions (PDFs). The authors explore various loss functions, demonstrating how objectives like relative-entropy and amplitude-weighting improve tail fidelity, which is critical for operational risk assessment. The developed framework is presented as data-source agnostic, applicable to data derived from physical experiments or simulations.

## Key Contributions

- Development of a data-driven stacked LSTM surrogate model that learns the non-linear, causal functional mapping from incident wave time series to vessel motions.
- Demonstration that the LSTM surrogate successfully reproduces rare parametric roll episodes and the associated statistical shifts in roll response time series.
- Comparison of loss function choices (MSE, relative-entropy, amplitude-weighted) showing the trade-off between average error and improved tail fidelity for risk assessment.
- The framework is proven to be data-source agnostic, working with data from both physical experiments (towing-tank) and high-fidelity simulations (URANS).

## Limitations

The training data generation relied on a URANS numerical wave tank simulation with a fixed forward speed, potentially limiting the generalizability to all possible operating conditions.

## Key Concepts

- [[parametric-roll-episode-learning]]: A learned functional mapping designed to explicitly model and reproduce rare, high-consequence regime shifts in vessel response time series, such as those caused by parametric roll instability.
- [[response-statistic-shift-modeling]]: A modeling objective focusing on reproducing the change in the statistical properties (like the PDF) of a time series response following a dynamic regime shift.

## Archivist Review

Two concepts were approved as they represent specific, reusable methodologies for handling high-risk, non-linear regime shifts in time-series modeling. 'Parametric Roll Episode Learning' captures the novelty of modeling rare events, while 'Response-Statistic Shift Modeling' highlights the crucial evaluation aspect of capturing distributional changes (PDFs) rather than just mean error. No datasets or open questions were deemed strong enough for permanent vault entries.

### Approved Concepts
- Parametric Roll Episode Learning: Parametric roll is a high-consequence, non-linear instability event in naval dynamics that this model is specifically trained to capture, which is a significant task beyond standard time-series forecasting.
- Response-Statistic Shift Modeling: The model's ability to capture changes in the probability density functions (PDFs) of the output, not just the time-domain trajectory, is crucial for accurate risk assessment.

## Links

- [Abstract](https://arxiv.org/abs/2603.24431)
- [PDF](https://arxiv.org/pdf/2603.24431)

