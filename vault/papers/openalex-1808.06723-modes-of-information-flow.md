---
# CSL-compatible fields
title: "Modes of Information Flow"
author:
  - literal: "Ryan G. James"
  - literal: "Blanca Daniella Mansante Ayala"
  - literal: "Bahti Zakirov"
  - literal: "James P. Crutchfield"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/1808.06723"

# Custom fields
paper_id: "1808.06723"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "information-extraction"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:40:35Z"
created_at: "2026-10-23T09:40:35Z"
---

# Modes of Information Flow

**Authors**: Ryan G. James, Blanca Daniella Mansante Ayala, Bahti Zakirov, James P. Crutchfield
**Date**: 2026-10-21
**Paper ID**: [openalex:1808.06723](https://arxiv.org/abs/1808.06723)

## Summary

This paper investigates the organization of complex systems by decomposing information flow between time series into three distinct modalities: intrinsic, shared, and synergistic flow. The authors demonstrate that standard metrics like time-delayed mutual information and transfer entropy conflate pairs of these modalities. To decouple and quantify each mode individually, they propose a cryptographic flow ansatz using intrinsic mutual information, successfully applying the framework to chaotic dynamical systems and financial markets.

## Key Contributions

- Demonstrates three distinct modalities of information flow between time series: intrinsic, shared, and synergistic information flow.
- Shows that traditional information-theoretic methods like time-delayed mutual information and transfer entropy conflate pairs of these information flow modalities.
- Introduces the cryptographic flow ansatz and intrinsic mutual information upper bound to quantify each mode individually across coupled chaotic dynamical systems, leader-follower dynamics, and financial markets.

## Open Questions & Future Work

- [[continuous-intrinsic-mutual-information]]

## Archivist Review

Approved one open question regarding continuous intrinsic mutual information because it highlights a clear computational and methodological bottleneck in information-theoretic time-series analysis. Rejected concept candidates as they represent paper-local framing and methodology.

### Approved Open Questions
- Continuous Intrinsic Mutual Information: Essential for extending multimodal information flow analysis beyond discrete time series to continuous physical and biological dynamical systems.

### Rejected Candidates
- [concept] Cryptographic Flow Ansatz (`cryptographic-flow-ansatz`) - paper_local: This is a specific theoretical ansatz and naming choice for this paper's framework rather than a broad, reusable machine learning method or architecture.
- [concept] Modes of Information Flow (`modes-of-information-flow`) - paper_local: This is the title of the paper and represents a high-level conceptual framing rather than a specific operationalizable concept.

## Links

- [Abstract](https://arxiv.org/abs/1808.06723)
- [PDF](https://arxiv.org/pdf/1808.06723)

