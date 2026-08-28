---
# CSL-compatible fields
title: "When Does Context Routing Help? A Systematic Study of Multi-Modal Fusion in Time Series Forecasting"
author:
  - literal: "Ruizhe Zhou"
  - literal: "Gaoyuan Du"
  - literal: "Xiaoyang Liu"
  - literal: "Haoqi Yao"
  - literal: "Deepayan Chakrabarti"
  - literal: "Juchun Lin"
  - literal: "Yixuan Shen"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.25128"

# Custom fields
paper_id: "2608.25128"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "mixture-of-experts"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:59:02Z"
created_at: "2026-08-28T16:59:02Z"
---

# When Does Context Routing Help? A Systematic Study of Multi-Modal Fusion in Time Series Forecasting

**Authors**: Ruizhe Zhou, Gaoyuan Du, Xiaoyang Liu, Haoqi Yao, Deepayan Chakrabarti, Juchun Lin, Yixuan Shen
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.25128](https://arxiv.org/abs/2608.25128)

## Summary

This paper systematically investigates when multi-modal context routing helps time-series forecasting, revealing that auxiliary context only improves performance under two strict dataset-level conditions: low target autocorrelation and non-zero conditional mutual information beyond history. Through experiments across multiple model families and datasets, the authors show that context fusion benefits collapse to zero when these conditions fail, and establish causality via shortcut injection and context corruption interventions.

## Key Contributions

- Identifies two necessary dataset-level conditions for auxiliary context to help time-series forecasting: low target autocorrelation and non-zero conditional mutual information between context and target given history.
- Demonstrates through controlled experiments on MoME and a single-backbone testbed that context fusion collapses to model capacity floors when either condition fails.
- Establishes causality via targeted interventions, showing that adding a shortcut suppresses routing contributions by 77-93% and context corruption reverses benefits.
- Provides a calibrated pre-training diagnostic yielding no false positives on the evaluated datasets.

## Limitations

Positive magnitudes of context-attributable gains are heavily concentrated in a single model family (MoME) and only corroborated in direction by secondary testbeds.

## Open Questions & Future Work

- [[multimodal-fusion-beyond-text-embeddings]]

## Archivist Review

The paper investigates the foundational conditions under which multimodal context routing actually helps time-series forecasting. We approved the open question regarding the extension of these findings beyond text embeddings to diverse auxiliary modalities. No new permanent concepts were approved because the core conditions identified map closely to fundamental information-theoretic bounds and autocorrelation properties already well-represented in the vault.

### Approved Open Questions
- Multimodal Fusion Beyond Text Embeddings: Understanding modality-agnostic applicability is crucial since practical forecasting systems frequently ingest heterogeneous auxiliary streams (e.g., satellite imagery, transactional tables, and audio feeds) rather than text alone.

### Rejected Candidates
- [open_question] Multimodal Fusion Beyond Text Embeddings (`multimodal-fusion-beyond-text-embeddings`) - generic: The open question is well-formulated and important for understanding multi-modal time series generalization.

## Links

- [Abstract](https://arxiv.org/abs/2608.25128)
- [PDF](https://arxiv.org/pdf/2608.25128)

