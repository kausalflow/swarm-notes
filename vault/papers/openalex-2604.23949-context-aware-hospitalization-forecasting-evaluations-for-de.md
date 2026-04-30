---
# CSL-compatible fields
title: "Context-Aware Hospitalization Forecasting Evaluations for Decision Support using LLMs"
author:
  - literal: "Rhea Makkuni"
  - literal: "Ananya Joshi"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.23949"

# Custom fields
paper_id: "2604.23949"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "decision-support"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hybridarx"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:24:01Z"
created_at: "2026-04-30T07:24:01Z"
---

# Context-Aware Hospitalization Forecasting Evaluations for Decision Support using LLMs

**Authors**: Rhea Makkuni, Ananya Joshi
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.23949](https://arxiv.org/abs/2604.23949)

## Summary

This paper evaluates the efficacy of using LLMs for real-time hospitalization forecasting during large-scale healthcare disruptions. The authors compare direct LLM forecasting against classical time-series models and a proposed hybrid approach, HybridARX, which integrates LLM-derived contextual signals into structured models. Results demonstrate that HybridARX achieves superior stability and calibration in non-stationary healthcare settings compared to standard baselines. The study underscores the importance of operational decision metrics, such as bias and lead-lag alignment, for evaluating AI-driven forecasting in medical resource management.

## Key Contributions

- Introduced HybridARX, a context-augmented pipeline that integrates LLM-derived signals into structured models to improve forecasting stability.
- Demonstrated that HybridARX outperforms classical ARX models in non-stationary healthcare resource forecasting across 60 US counties.
- Established a decision-centric evaluation framework for medical forecasting that prioritizes bias and lead-lag alignment over mere error minimization.

## Open Questions & Future Work

- [[identifying-causal-leading-indicators-healthcare-demand]]

## Key Concepts

- [[hybridarx]]: A context-augmented hybrid forecasting pipeline that integrates LLM-derived signals into structured time-series models.

## Archivist Review

I approved the HybridARX framework as a representative example of leveraging LLMs for structured temporal modeling. I also approved the open question regarding causal leading indicators, as it addresses a fundamental limitation in non-stationary forecasting where context noise is pervasive. Other candidates were rejected to maintain the vault's focus on high-impact, reusable primitives.

### Approved Concepts
- HybridARX: Central architecture proposed for leveraging LLMs in non-stationary healthcare forecasting.

### Approved Open Questions
- Identifying Causal Leading Indicators: This is a bottleneck for moving from purely reactive, short-horizon forecasting to proactive, decision-aware capacity planning in healthcare. Without understanding which signals are causal or truly leading, researchers risk including noisy variables that degrade rather than improve model performance.

## Links

- [Abstract](https://arxiv.org/abs/2604.23949)
- [PDF](https://arxiv.org/pdf/2604.23949)

