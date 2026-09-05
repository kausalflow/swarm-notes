---
# CSL-compatible fields
title: "Compositional Spectral Prompts for LLM-based Online Time Series Forecasting"
author:
  - literal: "S. K. Choi"
  - literal: "Hyunchul Kim"
  - literal: "Jae-Gil Lee"
  - literal: "Chanyoung Park"
issued:
  date-parts:
    - [2026, 9, 2]
url: "https://arxiv.org/abs/2609.02093"

# Custom fields
paper_id: "2609.02093"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "in-context-learning"
  - "few-shot-learning"
  - "adaptation"
  - "efficiency"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "cospot"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-05T08:41:35Z"
created_at: "2026-09-05T08:41:35Z"
---

# Compositional Spectral Prompts for LLM-based Online Time Series Forecasting

**Authors**: S. K. Choi, Hyunchul Kim, Jae-Gil Lee, Chanyoung Park
**Date**: 2026-09-02
**Paper ID**: [openalex:2609.02093](https://arxiv.org/abs/2609.02093)

## Summary

The paper introduces CoSPOT, an LLM-based online time series forecasting framework that achieves efficient online adaptation by keeping the pre-trained language model frozen and employing compositional spectral prompts grounded in frequency-domain bases. By decomposing time series into frequency bases and composing corresponding spectral basis prompts according to amplitudes, CoSPOT effectively represents unseen patterns as combinations of learned basis prompts, outperforming existing memory buffer-based retrieval strategies in non-stationary environments.

## Key Contributions

- Introduces CoSPOT, an LLM-based online time series forecasting framework that keeps the pre-trained backbone frozen while adapting efficiently.
- Employs compositional spectral prompts grounded in frequency-domain bases to capture overall distributions and generalize to unseen patterns.
- Demonstrates superior performance and practicality across challenging online scenarios, including extended online phases and cross-dataset settings with substantial distribution shifts.

## Open Questions & Future Work

- [[robust-long-term-adaptation-distribution-shifts]]

## Key Concepts

- [[cospot]]: An LLM-based online time series forecasting framework that uses compositional spectral prompts grounded in frequency-domain bases for efficient online adaptation.

## Archivist Review

Approved the core CoSPOT framework concept for its novel use of compositional spectral prompts for parameter-efficient online adaptation in LLM time series forecasting, and approved the open question on robust long-term adaptation under distribution shifts. Scrupulously adhered to the scarcity constraints and formatting rules.

### Approved Concepts
- CoSPOT: Central framework of the paper introducing compositional spectral prompts for online time series forecasting.

### Approved Open Questions
- Robust Long-Term Adaptation under Distribution Shifts: Crucial for scaling online time series forecasting to highly non-stationary real-world environments where new, unprecedented regimes continually emerge.

## Links

- [Abstract](https://arxiv.org/abs/2609.02093)
- [PDF](https://arxiv.org/pdf/2609.02093)

