---
# CSL-compatible fields
title: "Nexus : An Agentic Framework for Time Series Forecasting"
author:
  - literal: "Sarkar Snigdha Sarathi Das"
  - literal: "Palash Goyal"
  - literal: "Mihir Parmar"
  - literal: "Nanyun Peng"
  - literal: "Vishy Tirumalashetty"
  - literal: "Chunliang Li"
  - literal: "Rui Zhang"
  - literal: "Jinsung Yoon"
  - literal: "Tomas Pfister"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14389"

# Custom fields
paper_id: "2605.14389"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "agent"
  - "multimodal"
  - "reasoning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "nexus-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:29:56Z"
created_at: "2026-05-17T07:29:56Z"
---

# Nexus : An Agentic Framework for Time Series Forecasting

**Authors**: Sarkar Snigdha Sarathi Das, Palash Goyal, Mihir Parmar, Nanyun Peng, Vishy Tirumalashetty, Chunliang Li, Rui Zhang, Jinsung Yoon, Tomas Pfister
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14389](https://arxiv.org/abs/2605.14389)

## Summary

Nexus is a multi-agent forecasting framework that addresses the disconnect between TSFMs' numerical modeling and LLMs' contextual understanding. By decomposing forecasting tasks into specialized stages—macro-temporal, micro-temporal, and contextual integration—the framework synthesizes final predictions without relying on statistical anchors. Evaluations on datasets succeeding knowledge cutoffs demonstrate that Nexus consistently outperforms both TSFMs and LLM baselines, while simultaneously providing transparent, high-quality reasoning traces for each forecast.

## Key Contributions

- Nexus achieves state-of-the-art performance on Zillow real estate metrics and volatile stock market equities by outperforming dedicated Time Series Foundation Models (TSFMs) and standard LLM baselines.
- Introduces an agentic forecasting framework that decomposes complex time series prediction into macro-temporal, micro-temporal, and contextual integration stages.
- Demonstrates that current LLMs exhibit superior forecasting capabilities when numerical and contextual reasoning are systematically orchestrated within an agentic pipeline.

## Open Questions & Future Work

- [[multimodal-time-series-integration]]

## Key Concepts

- [[nexus-framework]]: A multi-agent framework that decomposes time series forecasting into distinct stages of temporal fluctuation analysis and contextual information integration.

## Archivist Review

Approved the Nexus framework as a notable shift toward agentic decomposition in time series forecasting, alongside an open question concerning the integration of multimodal (qualitative/textual) context with numerical forecasting. Rejected the Zillow metrics as a dataset because it describes a category of data sources rather than a specific, canonical benchmark. Applied strict selection criteria to emphasize architecture-level contributions and foundational research bottlenecks.

### Approved Concepts
- Nexus Framework: It shifts forecasting from monolithic sequence modeling to a multi-stage, agentic reasoning pipeline capable of synthesizing numerical and contextual data.

### Approved Open Questions
- Integrating Qualitative Contextual Forecasting: The current split between TSFMs (numerical) and LLMs (textual) creates a structural deficit in real-world forecasting; bridging this gap is essential for robust, interpretable decision-making in volatile environments.

### Rejected Candidates
- [dataset] Zillow real estate metrics (`zillow-real-estate-metrics`) - low_impact: This is a broad category of data rather than a specific, standardized dataset benchmark.

## Links

- [Abstract](https://arxiv.org/abs/2605.14389)
- [PDF](https://arxiv.org/pdf/2605.14389)

