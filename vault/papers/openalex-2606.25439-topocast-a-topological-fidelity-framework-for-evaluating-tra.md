---
# CSL-compatible fields
title: "TopoCast: A Topological Fidelity Framework for Evaluating Transformer-Based Time Series Forecasting"
author:
  - literal: "Sandeepa Weerasekara"
  - literal: "Sandareka Wickramanayake"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2606.25439"

# Custom fields
paper_id: "2606.25439"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "transformer"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "topocast-framework"
  - "localized-topological-fidelity-score-ltfs"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-27T07:42:44Z"
created_at: "2026-06-27T07:42:44Z"
---

# TopoCast: A Topological Fidelity Framework for Evaluating Transformer-Based Time Series Forecasting

**Authors**: Sandeepa Weerasekara, Sandareka Wickramanayake
**Date**: 2026-06-24
**Paper ID**: [openalex:2606.25439](https://arxiv.org/abs/2606.25439)

## Summary

Current time series forecasting evaluation relies heavily on pointwise metrics like MSE, which often fail to capture structural signal properties such as phase alignment and oscillatory dynamics. This paper introduces TopoCast, a topological framework that uses Takens delay embedding and persistent homology to quantify the structural fidelity of forecasts. By combining topological features with a novel dominant cycle overlap metric, the authors propose the Localized Topological Fidelity Score (LTFS) to expose hidden model failure modes. Experiments confirm that models with identical numerical error profiles can possess vastly different structural fidelity, underscoring the necessity of topology-aware evaluation in time series modeling.

## Key Contributions

- Introduces TopoCast, a framework that uses phase-space reconstruction and persistent homology to evaluate structural fidelity in time series forecasting.
- Proposes the Localized Topological Fidelity Score (LTFS), which enables the detection of phase shifts and temporal localization errors that pointwise metrics like MSE fail to identify.
- Demonstrates through empirical evaluation on Transformer architectures that similar MSE performance can mask significant differences in structural model integrity.

## Open Questions & Future Work

- [[topology-aware-forecasting-and-evaluation]]

## Key Concepts

- [[topocast-framework]]: A topology-driven evaluation framework that utilizes persistent homology and phase-space reconstruction to assess the structural fidelity of time series forecasts.
- [[localized-topological-fidelity-score-ltfs]]: A phase-aware evaluation metric that combines topological fidelity scores with dominant cycle overlap to assess temporal localization accuracy in time series forecasting.

## Archivist Review

The approved concepts define a distinct, novel framework for evaluating the structural integrity of time series models, which is a major, reusable contribution to forecasting literature. The open question was condensed into a single high-level research direction regarding the integration of topology into both training objectives and probabilistic evaluation, as these represent the logical next steps for the field beyond current deterministic diagnostic tools.

### Approved Concepts
- TopoCast Framework: It introduces a novel paradigm for time series evaluation that moves beyond pointwise metrics to capture structural and topological properties.
- Localized Topological Fidelity Score (LTFS): Combines topological fidelity with temporal localization to specifically identify phase-shifting and timing errors in time series predictions.

### Approved Open Questions
- Topology-Aware Forecasting and Evaluation: These directions are critical for moving beyond post-hoc diagnostic tools toward models explicitly trained to preserve structural signal integrity.

## Links

- [Abstract](https://arxiv.org/abs/2606.25439)
- [PDF](https://arxiv.org/pdf/2606.25439)

