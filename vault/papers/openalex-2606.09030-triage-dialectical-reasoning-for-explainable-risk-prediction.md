---
# CSL-compatible fields
title: "TRIAGE: Dialectical Reasoning for Explainable Risk Prediction on Irregularly Sampled Medical Time Series with LLMs"
author:
  - literal: "Hyeongwon Jang"
  - literal: "Gyouk Chu"
  - literal: "Changhun Kim"
  - literal: "Joonhyung Park"
  - literal: "Hangyul Yoon"
  - literal: "Eunho Yang"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09030"

# Custom fields
paper_id: "2606.09030"
paper_source: "openalex"
domain: "medicine"
tags:
  - "llm"
  - "time-series"
  - "explainability"
  - "reasoning"
  - "question-answering"
  - "medical-time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dialectical-reasoning-for-risk-prediction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:07:38Z"
created_at: "2026-06-11T09:07:38Z"
---

# TRIAGE: Dialectical Reasoning for Explainable Risk Prediction on Irregularly Sampled Medical Time Series with LLMs

**Authors**: Hyeongwon Jang, Gyouk Chu, Changhun Kim, Joonhyung Park, Hangyul Yoon, Eunho Yang
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09030](https://arxiv.org/abs/2606.09030)

## Summary

TRIAGE is a framework for explainable risk prediction on irregularly sampled medical time series that addresses the tendency of LLMs to provide overconfident binary predictions. By eliciting rationales for competing clinical outcomes—a process called dialectical reasoning—the model generates more granular, continuous, and calibrated risk scores. This approach bridges the gap between high-performance prediction and clinical interpretability, showing significant improvements in both predictive accuracy and calibration over existing baselines.

## Key Contributions

- Introduces TRIAGE, a dialectical reasoning framework that mitigates LLM risk polarization in clinical time-series forecasting.
- Achieves a 3.3% average AUPRC improvement and 81% reduction in calibration error across three ISMTS benchmarks.
- Demonstrates through LLM-as-a-judge evaluation that dialectical rationales outperform post-hoc explanations in clinical reasoning quality by 20%.

## Open Questions & Future Work

- [[dialectical-clinical-reasoning-bottlenecks]]

## Key Concepts

- [[dialectical-reasoning-for-risk-prediction]]: A forecasting approach where LLMs generate rationales for competing outcomes to produce calibrated, interpretable risk scores.

## Archivist Review

I approved the central dialectical reasoning framework as it provides a novel approach to mitigating LLM overconfidence and risk polarization in high-stakes forecasting. I also approved a consolidated open question that captures the essential research challenges regarding validation, scalability, and task complexity. No datasets were approved as none were specifically named or highlighted as a unique, reusable contribution beyond the standard benchmarks utilized.

### Approved Concepts
- Dialectical Reasoning for Risk Prediction: This framework directly addresses the problem of LLM risk polarization in medical prognosis by forcing the model to argue for competing outcomes rather than outputting a single overconfident prediction.

### Approved Open Questions
- Dialectical clinical reasoning bottlenecks: These issues are critical for the deployment of LLM-driven decision support in high-stakes clinical environments where latency, reliability, and accuracy are paramount.

## Links

- [Abstract](https://arxiv.org/abs/2606.09030)
- [PDF](https://arxiv.org/pdf/2606.09030)

