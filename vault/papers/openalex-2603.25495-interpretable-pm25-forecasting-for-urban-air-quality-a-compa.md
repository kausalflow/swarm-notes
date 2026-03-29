---
# CSL-compatible fields
title: "Interpretable PM2.5 Forecasting for Urban Air Quality: A Comparative Study of Operational Time-Series Models"
author:
  - literal: "Moazzam Umer Gondal"
  - literal: "Hamad ul Qudous"
  - literal: "Asma Ahmad Farhan"
  - literal: "Sultan Alamri"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25495"

# Custom fields
paper_id: "2603.25495"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "interpretability"
  - "time-series"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "leakage-aware-forecasting-workflow"
  - "online-residual-correction-frozen-models"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:06:32Z"
created_at: "2026-03-29T06:06:32Z"
---

# Interpretable PM2.5 Forecasting for Urban Air Quality: A Comparative Study of Operational Time-Series Models

**Authors**: Moazzam Umer Gondal, Hamad ul Qudous, Asma Ahmad Farhan, Sultan Alamri
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25495](https://arxiv.org/abs/2603.25495)

## Summary

This paper compares the performance of lightweight, interpretable time-series models (SARIMAX, Prophet, NeuralProphet) for short-term, hourly PM2.5 forecasting in Beijing, focusing on practical deployment strategies. The authors introduce a leakage-aware workflow under the Perfect Prognosis setting and evaluate models using walk-forward refitting and frozen forecasting with online residual correction. Results indicate that Facebook Prophet excelled under walk-forward retraining, while corrected SARIMAX provided the best accuracy in the frozen regime, demonstrating that simpler models can remain competitive. The work highlights the operational benefit of online residual correction in maintaining accuracy while drastically reducing the runtime overhead associated with frequent retraining.

## Key Contributions

- Demonstrated that lightweight, interpretable models like SARIMAX and Prophet can achieve competitive short-term PM2.5 forecasting accuracy against more complex models.
- Evaluated two practical deployment regimes: weekly walk-forward refitting and frozen forecasting with online residual correction.
- Showed that online residual correction significantly improved the frozen SARIMAX model's performance, achieving the lowest overall error (MAE 32.50).
- Provided a quantitative trade-off analysis, showing that corrected Prophet achieved near walk-forward accuracy with a substantial reduction in runtime (from ~15 min to ~47 sec).

## Limitations

The study focused only on PM2.5 prediction in Beijing and did not benchmark against state-of-the-art deep learning sequence models (e.g., Transformers or Mamba).

## Open Questions & Future Work

- [[lightweight-hybrid-adaptation-for-pollution-regimes]]
- [[generalizability-of-lightweight-forecasting-adaptation]]
- [[federated-learning-for-distributed-aq-forecasting]]

## Key Concepts

- [[leakage-aware-forecasting-workflow]]: A structured workflow for time-series forecasting that incorporates chronological data partitioning, feature selection, and exogenous driver modeling under the Perfect Prognosis setting to prevent information leakage.
- [[online-residual-correction-frozen-models]]: A technique to maintain the accuracy of a frozen, pre-trained time-series model by applying real-time corrections based on the residuals (errors) observed in recent predictions.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 3 open question(s), and 0 dataset(s), with 0 rejected candidate note(s).

### Approved Concepts
- Leakage-Aware Forecasting Workflow: This workflow specifically addresses data leakage in time-series forecasting by careful partitioning and integration of exogenous variables, a critical issue for model deployment.
- Online Residual Correction for Frozen Models: This technique adapts a frozen forecasting model to changing conditions by applying corrections based on recent errors, offering a trade-off between retraining cost and accuracy maintenance.

### Approved Open Questions
- Integrate lightweight hybrid techniques: This direction seeks to bridge the gap between high-accuracy complex models and the operational need for interpretable, low-overhead, and robust solutions for unpredictable pollution shifts.
- Assess lightweight adaptation generalizability: Determining the generalizability of lightweight forecasting methods is crucial for their adoption in diverse global urban air quality management systems.
- Explore federated learning schemes: This addresses the dual challenge of data privacy constraints and the need for models generalized across multiple urban areas.

## Links

- [Abstract](https://arxiv.org/abs/2603.25495)
- [PDF](https://arxiv.org/pdf/2603.25495)

