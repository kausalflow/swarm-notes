---
# CSL-compatible fields
title: "MATA-Former & SIICU: Semantic Aware Temporal Alignment for High-Fidelity ICU Risk Prediction"
author:
  - literal: "Zhichong Zheng"
  - literal: "Xiaohang Nie"
  - literal: "Xueqi Wang"
  - literal: "Yuanjin Zhao"
  - literal: "Haitao Zhang"
  - literal: "Yichao Tang"
issued:
  date-parts:
    - [2026, 4, 2]
url: "https://arxiv.org/abs/2604.01727"

# Custom fields
paper_id: "2604.01727"
paper_source: "openalex"
domain: "medicine"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "long-context"
  - "multimodal"
architectures:
  - "transformer"
datasets:
  - "siicu"
concept_slugs:
  - "mata-former"
  - "plateau-gaussian-soft-labeling-psl"
dataset_slugs:
  - "siicu"
skill: "TimeSeriesSkill"
processed_at: "2026-04-05T06:08:52Z"
created_at: "2026-04-05T06:08:52Z"
---

# MATA-Former & SIICU: Semantic Aware Temporal Alignment for High-Fidelity ICU Risk Prediction

**Authors**: Zhichong Zheng, Xiaohang Nie, Xueqi Wang, Yuanjin Zhao, Haitao Zhang, Yichao Tang
**Date**: 2026-04-02
**Paper ID**: [openalex:2604.01727](https://arxiv.org/abs/2604.01727)

## Summary

The paper introduces the Medical-semantics Aware Time-ALiBi Transformer (MATA-Former) to improve clinical risk forecasting by prioritizing pathological event dependencies over simple chronological order. To address the limitations of binary supervision in ICU settings, the authors propose Plateau-Gaussian Soft Labeling (PSL), which reformulates risk prediction as a continuous multi-horizon regression task. Validated on the new, expert-annotated SIICU dataset and MIMIC-IV, the framework demonstrates superior performance in processing irregular, text-intensive clinical time series.

## Key Contributions

- MATA-Former architecture improves clinical forecasting by dynamically parameterizing attention weights based on event semantics rather than chronological proximity.
- Plateau-Gaussian Soft Labeling (PSL) transforms traditional binary clinical risk classification into multi-horizon regression to better capture full-trajectory risks.
- The SIICU dataset provides over 506k expert-verified events, establishing a new high-fidelity benchmark for text-intensive, irregular clinical time-series analysis.

## Key Concepts

- [[mata-former]]: A Transformer variant that dynamically parameterizes attention weights using medical event semantics to improve causal alignment in clinical risk prediction.
- [[plateau-gaussian-soft-labeling-psl]]: A soft-labeling technique that converts binary risk classifications into continuous regression targets to capture temporal risk evolution.

## Archivist Review

I have approved the MATA-Former architecture and the Plateau-Gaussian Soft Labeling (PSL) technique as they represent reusable, methodologically distinct contributions to time-series modeling in clinical domains. I have also approved the new SIICU dataset as a high-fidelity benchmark, while rejecting MIMIC-IV as a duplicate of an existing vault entry. No new open questions were approved as the paper focuses on architectural and methodological improvements rather than identifying specific open research bottlenecks.

### Approved Concepts
- Medical-semantics Aware Time-ALiBi Transformer (MATA-Former): This architecture explicitly prioritizes clinical event causality over simple chronological proximity in high-stakes time-series forecasting.
- Plateau-Gaussian Soft Labeling (PSL): PSL addresses the limitation of coarse binary clinical labels by providing continuous supervision for evolving risk trajectories.

### Rejected Candidates
- [dataset] MIMIC-IV (`mimic-iv`) - duplicate_existing: MIMIC-IV is a well-established existing dataset already present in the vault.

## Datasets

- [[siicu]]

## Links

- [Abstract](https://arxiv.org/abs/2604.01727)
- [PDF](https://arxiv.org/pdf/2604.01727)

