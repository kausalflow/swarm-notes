---
# CSL-compatible fields
title: "HealthCAT: An Interpretable Encoder-only Transformer Framework for Health Indicator Prediction and Temporal Interpretation of Wearable Sensor Data"
author:
  - literal: "Xiaotong Yu"
  - literal: "Joshua Y. Kim"
  - literal: "HaeJin Lee"
  - literal: "Kalina Yacef"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.27635"

# Custom fields
paper_id: "2607.27635"
paper_source: "openalex"
domain: "biology"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "interpretability"
  - "explainability"
  - "multimodal"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:27:46Z"
created_at: "2026-08-02T07:27:46Z"
---

# HealthCAT: An Interpretable Encoder-only Transformer Framework for Health Indicator Prediction and Temporal Interpretation of Wearable Sensor Data

**Authors**: Xiaotong Yu, Joshua Y. Kim, HaeJin Lee, Kalina Yacef
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.27635](https://arxiv.org/abs/2607.27635)

## Summary

HealthCAT is an interpretable encoder-only transformer framework designed for health indicator prediction and temporal interpretation of multivariate wearable sensor data. By integrating an Attentive Class Activation Token (AttentiveCAT), the framework generates class-specific, time-step-level interpretations mapped onto behavioural cycles. Evaluations across two real-world datasets show that HealthCAT outperforms deep learning baselines by up to 17% in F1-score and 12% in accuracy while identifying predictively informative time steps.

## Key Contributions

- Introduces HealthCAT, an interpretable encoder-only transformer framework integrating an Attentive Class Activation Token (AttentiveCAT) for health indicator prediction from wearable sensor data.
- Achieves up to 17% higher F1-score and 12% higher accuracy compared to deep learning baselines on two real-world wearable sensor datasets (p < 0.05).
- Demonstrates via masking experiments that time steps identified by HealthCAT carry significantly more predictive value than random selection across all masking conditions (p < 0.05).

## Limitations

Evaluated on wearable sensor datasets involving 306 participants; broader generalizability across diverse clinical populations remains to be explored.

## Archivist Review

Reviewed candidates for HealthCAT framework paper. Rejected the paper-specific framework concept and open question following strict quality and scarcity guidelines.

### Rejected Candidates
- [concept] HealthCAT (`healthcat`) - paper_local: Paper-specific application framework combining standard encoder-only transformers with local attention tokens, lacking independent methodological novelty outside its healthcare context.
- [open_question] Multimodal Wearable Health Analytics (`multimodal-wearable-health-analytics-and-intervention`) - low_impact: Standard future work directions involving larger cohorts, more data modalities, and application deployment rather than a precise methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.27635)
- [PDF](https://arxiv.org/pdf/2607.27635)

