---
# CSL-compatible fields
title: "CHAIN: Calibrated LLM Forecasting via Causal-Temporal Hypergraph Inference"
author:
  - literal: "Wenjin Liu"
  - literal: "Chenxi Wang"
  - literal: "Yue Lu"
  - literal: "Zhe Cui"
  - literal: "Haoran Luo"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36689"

# Custom fields
paper_id: "2609.36689"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "reasoning"
  - "uncertainty-aware-wildfire-forecasting-framework"
  - "calibration"
  - "hypergraph"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "chain"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:47:31Z"
created_at: "2026-10-02T10:47:31Z"
---

# CHAIN: Calibrated LLM Forecasting via Causal-Temporal Hypergraph Inference

**Authors**: Wenjin Liu, Chenxi Wang, Yue Lu, Zhe Cui, Haoran Luo
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36689](https://arxiv.org/abs/2609.36689)

## Summary

Large language models often suffer from systematic calibration bias when predicting event probabilities, undermining decision-making reliability. To address this, the authors introduce CHAIN, a causal-temporal hypergraph inference framework that decomposes prediction into evidence weighting, aggregation, and source fusion. By applying stage-specific mechanisms—such as temporal decay modulation via causal topological distance, Noisy-OR chain aggregation, and adaptive source fusion—CHAIN significantly improves probability calibration and forecasting accuracy across cross-domain benchmarks.

## Key Contributions

- Proposes CHAIN, a three-stage causal-temporal hypergraph inference framework that models structural sources of calibration bias within LLM event forecasting.
- Implements stage-specific mechanisms including causal topological distance temporal decay modulation, direction-aware Noisy-OR chain aggregation, and causal coverage-driven source fusion.
- Demonstrates superior performance over existing baseline methods across expected calibration error, Brier score, and accuracy on cross-domain forecasting benchmarks.

## Key Concepts

- [[chain]]: A calibrated LLM forecasting framework using causal-temporal hypergraph inference to mitigate structural bias across evidence weighting, aggregation, and source fusion stages.

## Archivist Review

Approved the primary methodological framework concept 'CHAIN' as it introduces a distinct causal-temporal hypergraph inference approach for LLM probability calibration. The open question candidate was rejected because it lists generic catch-all future work directions instead of a specific, targeted technical bottleneck. No custom datasets were approved as none were explicitly named.

### Approved Concepts
- CHAIN: Introduces a principled three-stage causal-temporal hypergraph inference framework for calibrating LLM event forecasting.

### Rejected Candidates
- [open_question] Future Directions for Calibrated LLM Forecasting (`future-directions-calibrated-llm-forecasting`) - low_impact: Too broad and enumerates generic future work directions rather than formulating a single precise unresolved technical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.36689)
- [PDF](https://arxiv.org/pdf/2609.36689)

