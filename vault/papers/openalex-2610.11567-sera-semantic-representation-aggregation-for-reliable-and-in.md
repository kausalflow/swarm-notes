---
# CSL-compatible fields
title: "Sera: Semantic Representation Aggregation for Reliable and Interpretable Battery Health Forecasting"
author:
  - literal: "Jiawei Li"
  - literal: "Fang Liu"
  - literal: "Wei Zhang"
  - literal: "Zuming Liu"
  - literal: "Ng Man-Fai"
  - literal: "Zhi Wei Seh"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11567"

# Custom fields
paper_id: "2610.11567"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "interpretable"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sera"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:52:46Z"
created_at: "2026-10-10T10:52:46Z"
---

# Sera: Semantic Representation Aggregation for Reliable and Interpretable Battery Health Forecasting

**Authors**: Jiawei Li, Fang Liu, Wei Zhang, Zuming Liu, Ng Man-Fai, Zhi Wei Seh
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11567](https://arxiv.org/abs/2610.11567)

## Summary

This paper introduces Sera, a semantic representation aggregation framework for battery state of health (SoH) forecasting that addresses nonlinear degradation and heterogeneity by integrating domain-guided degradation semantics. By combining rule-based knowledge and LLM-based interpretation with temporal model representations via gated aggregation, Sera achieves up to a 37.3% reduction in prediction error and improves model interpretability through counterfactual analysis.

## Key Contributions

- Proposes Sera, a semantic representation aggregation framework that integrates domain-guided degradation semantics with standard temporal models for battery health forecasting.
- Constructs complementary representations using rule-based knowledge and LLM-based interpretation, integrated via gated aggregations.
- Achieves up to a 37.3% reduction in prediction error over temporal baselines and demonstrates enhanced generalizability across multiple prediction horizons.
- Validates interpretability through counterfactual analysis showing consistent prediction responses to key degradation descriptors.

## Key Concepts

- [[sera]]: A semantic representation aggregation framework that complements temporal modeling with domain-guided degradation semantics for battery health forecasting.

## Archivist Review

We approved the central framework 'sera' as it introduces a reusable mechanism for combining rule-based and LLM-based degradation semantics via gated aggregation. The open question was rejected as it describes broad future work without identifying a specific unresolved technical bottleneck.

### Approved Concepts
- Sera: Sera is the central framework introduced in the paper, combining rule-based knowledge and LLM-based interpretation to aggregate degradation semantics for battery health forecasting.

### Rejected Candidates
- [open_question] Semantic Battery Health Forecasting Improvements (`semantic-battery-health-forecasting-improvements`) - weak_evidence: The question is too broad and generic about future improvements rather than a precise methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.11567)
- [PDF](https://arxiv.org/pdf/2610.11567)

