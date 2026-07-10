---
# CSL-compatible fields
title: "LLM-Guided Measurement Credibility Correction for Trustworthy Industrial Process Inference"
author:
  - literal: "Youcheng Zong"
  - literal: "Runda Jia"
  - literal: "Dakuo He"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.06111"

# Custom fields
paper_id: "2607.06111"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "llm-guided-measurement-credibility-correction-mcc"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:16:10Z"
created_at: "2026-07-10T08:16:10Z"
---

# LLM-Guided Measurement Credibility Correction for Trustworthy Industrial Process Inference

**Authors**: Youcheng Zong, Runda Jia, Dakuo He
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.06111](https://arxiv.org/abs/2607.06111)

## Summary

This paper addresses the problem of unreliable input measurements in industrial forecasting, where biased or stale sensor data often degrade predictive performance. The authors introduce LLM-Guided Measurement Credibility Correction (MCC), a lightweight framework that uses process documentation to establish semantic credibility references for incoming sensor streams. By correcting conflicts before they reach the forecasting backbone, MCC enhances model robustness without requiring explicit physical models or labeled fault datasets. Experimental results demonstrate that MCC significantly improves accuracy on industrial soft-sensing and forecasting tasks with minimal computational cost.

## Key Contributions

- Introduces LLM-Guided Measurement Credibility Correction (MCC), a pre-inference mechanism that converts industrial process documentation into actionable measurement semantics.
- Enables the detection and correction of measurement conflicts (e.g., stale or derived data) without relying on explicit process equations or numerical correlations.
- Achieves significant forecasting improvements, with average relative MAE reductions of 30.7% on real-test protocols and 80.3% on controlled-corruption protocols while maintaining low computational overhead (0.5--2.0k parameters).

## Open Questions & Future Work

- [[long-term-semantic-validation-and-updates]]

## Key Concepts

- [[llm-guided-measurement-credibility-correction-mcc]]: A pre-inference framework that utilizes LLM-derived measurement semantics to detect and correct conflicts in industrial sensor data before forecasting.

## Archivist Review

The paper provides a significant advancement in the trustworthiness of industrial forecasting by introducing a semantic-based pre-inference credibility layer. The concept of MCC is approved for its novelty in bridging unstructured documentation with numerical input validation, and the open question is approved for its importance in addressing the drift of semantic priors in real-world systems. All other candidates were rejected as they were paper-specific.

### Approved Concepts
- LLM-Guided Measurement Credibility Correction (MCC): Introduces a novel paradigm of using semantic information from documentation as a pre-processing filter to ensure input data trustworthiness, shifting the focus from numerical anomaly detection to semantic credibility.

### Approved Open Questions
- Long-term Semantic Validation Updates: This addresses the bottleneck of maintaining trust in AI systems that rely on potentially static knowledge bases in highly dynamic and aging industrial environments.

## Links

- [Abstract](https://arxiv.org/abs/2607.06111)
- [PDF](https://arxiv.org/pdf/2607.06111)

