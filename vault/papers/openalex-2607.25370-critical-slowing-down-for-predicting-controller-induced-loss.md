---
# CSL-compatible fields
title: "Critical slowing down for predicting controller induced loss of control in quadrotors"
author:
  - literal: "Jasper J. van Beers"
  - literal: "Prashant Solanki"
  - literal: "Erik-Jan Van Kampen"
  - literal: "Coen C. de Visser"
issued:
  date-parts:
    - [2026, 7, 28]
url: "https://arxiv.org/abs/2607.25370"

# Custom fields
paper_id: "2607.25370"
paper_source: "openalex"
domain: "robotics"
tags:
  - "robotics"
  - "anomaly-detection"
  - "forecasting"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-31T07:44:12Z"
created_at: "2026-07-31T07:44:12Z"
---

# Critical slowing down for predicting controller induced loss of control in quadrotors

**Authors**: Jasper J. van Beers, Prashant Solanki, Erik-Jan Van Kampen, Coen C. de Visser
**Date**: 2026-07-28
**Paper ID**: [openalex:2607.25370](https://arxiv.org/abs/2607.25370)

## Summary

This paper introduces a model-free forecasting scheme based on critical slowing down (CSD) to anticipate controller-induced loss of control (LOC) in quadrotors. By leveraging early warning signals from dynamical systems theory, the approach successfully predicts LOC up to 0.9 seconds in advance using real flight data without requiring data from the LOC event itself. Furthermore, the framework demonstrates strong generalization across different quadrotor architectures, controllers, and LOC scenarios without requiring re-parameterization.

## Key Contributions

- Develops a model-free forecasting scheme based on critical slowing down (CSD) to anticipate controller-induced loss of control (LOC) in quadrotors.
- Achieves a time-to-LOC forecast of up to 0.9 seconds prior to occurrence, outperforming recurrent neural network baselines in detection accuracy and data reliance.
- Demonstrates zero-shot generalization across different quadrotor architectures, flight environments, and distinct LOC scenarios without re-parameterization.

## Archivist Review

All candidates were reviewed against strict vault standards. The open question regarding automated EWS parameter selection is a general engineering preference rather than a foundational architectural bottleneck, so it was rejected to maintain high quality standards. No permanent concepts or datasets met the rigorous bar for standalone notes.

### Rejected Candidates
- [open_question] Automated Early Warning Signal Design (`automated-ews-design-parameter-selection`) - low_impact: The question asks for general parameter tuning and design simplification for early warning signals, which is too broad and routine.

## Links

- [Abstract](https://arxiv.org/abs/2607.25370)
- [PDF](https://arxiv.org/pdf/2607.25370)

