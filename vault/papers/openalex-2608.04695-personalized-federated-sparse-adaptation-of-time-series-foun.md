---
# CSL-compatible fields
title: "Personalized Federated Sparse Adaptation of Time-Series Foundation Models"
author:
  - literal: "Priyanka Nihalchandani"
  - literal: "Naman Srivastava"
  - literal: "Varun Ojha"
  - literal: "Pandarasamy Arjunan"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04695"

# Custom fields
paper_id: "2608.04695"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "federated-learning"
  - "mixture-of-experts"
  - "moe"
  - "parameter-efficient-fine-tuning"
  - "peft"
  - "foundation-model"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:34:12Z"
created_at: "2026-08-08T05:34:12Z"
---

# Personalized Federated Sparse Adaptation of Time-Series Foundation Models

**Authors**: Priyanka Nihalchandani, Naman Srivastava, Varun Ojha, Pandarasamy Arjunan
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04695](https://arxiv.org/abs/2608.04695)

## Summary

This paper introduces a personalized federated sparse adaptation framework for time-series foundation models applied to energy forecasting. By employing a heterogeneous temporal mixture-of-experts (MoE) adapter with a sequence-level router, the method balances client-specific customization with cross-building knowledge transfer. Evaluations across 50 buildings and multiple TSFM backbones demonstrate that personalized sparse federated adaptation outperforms both fully global and fully local training baselines.

## Key Contributions

- Proposes a personalized federated sparse adaptation framework for time-series foundation models (TSFMs) using a heterogeneous temporal mixture-of-experts adapter.
- Employs a sequence-level router mapping 168-hour context windows to top-k experts specialized in periodicity, long-range interactions, local variation, and trend-residual structure.
- Demonstrates across 50 buildings and three TSFM backbones that personalized federated learning consistently outperforms global FL and local training baselines.

## Open Questions & Future Work

- [[adaptive-expert-sharing-mechanisms]]

## Archivist Review

Evaluated the candidates under strict scarcity and novelty guidelines. The core method (personalized federated sparse adaptation of TSFMs using MoE) is too paper-local and specific to be approved as a standalone concept note. However, the open question on adaptive expert-sharing mechanisms addresses a fundamental, reusable gap in federated mixture-of-experts foundation model adaptation and is retained.

### Approved Open Questions
- Adaptive Expert-Sharing Mechanisms: Understanding how to optimally partition and dynamically share expert modules across heterogeneous clients is critical for maximizing both cross-client transfer and local personalization in foundation model federated learning.

### Rejected Candidates
- [concept] Personalized Federated Sparse Adaptation Framework (`personalized-federated-sparse-adaptation`) - paper_local: Subcomponent or specialized instantiation of federated mixture-of-experts adaptation applied to time-series foundation models, which is too paper-local and architecture-specific for a permanent standalone note.

## Links

- [Abstract](https://arxiv.org/abs/2608.04695)
- [PDF](https://arxiv.org/pdf/2608.04695)

