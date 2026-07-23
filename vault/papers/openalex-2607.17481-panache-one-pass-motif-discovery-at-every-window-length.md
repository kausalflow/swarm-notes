---
# CSL-compatible fields
title: "Panache: One-Pass Motif Discovery at Every Window Length"
author:
  - literal: "Tej Sanibh Ranade"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17481"

# Custom fields
paper_id: "2607.17481"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:27:59Z"
created_at: "2026-07-23T07:27:59Z"
---

# Panache: One-Pass Motif Discovery at Every Window Length

**Authors**: Tej Sanibh Ranade
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17481](https://arxiv.org/abs/2607.17481)

## Summary

The paper introduces Panache, a one-pass streaming algorithm for z-normalized pan matrix profile motif discovery that avoids repeated quadratic self-joins by maintaining non-DC spectra online via sliding-DFT recurrences. By combining spectral states with occupancy-controlled hashing and Parseval-based lower bounds, Panache achieves near-linear runtime across multiple window lengths. It outperforms state-of-the-art CPU and GPU baselines while recovering top-20 pan-motifs across diverse UCR configurations.

## Key Contributions

- Introduces Panache, the first one-pass streaming algorithm for z-normalized pan matrix profile motif discovery with near-linear runtime.
- Replaces repeated quadratic self-joins across multiple window lengths with a single scan using sliding-DFT recurrences and occupancy-controlled spectral hashing.
- Recovers all top-20 pan-motifs across 17 UCR configurations while significantly outperforming existing CPU and GPU baselines (e.g., finishing on Wafer with 5 million samples over 51 lengths in minutes instead of hours).

## Archivist Review

All candidates were carefully evaluated against strict vault inclusion criteria. The proposed concept 'panache' is a specific algorithmic system rather than a reusable theoretical modeling primitive, and the open question regarding memory scaling is standard for streaming systems. Therefore, no items were approved to maintain high vault standards.

### Rejected Candidates
- [concept] Panache (`panache`) - paper_local: Panache is a specific algorithmic implementation for motif discovery rather than a reusable conceptual time series modeling primitive.
- [open_question] Memory Scaling in Streaming Motif Discovery (`memory-scaling-streaming-motif-discovery`) - low_impact: Standard memory scaling bottleneck for streaming algorithms rather than a conceptual research question with broader vault reusability.

## Links

- [Abstract](https://arxiv.org/abs/2607.17481)
- [PDF](https://arxiv.org/pdf/2607.17481)

