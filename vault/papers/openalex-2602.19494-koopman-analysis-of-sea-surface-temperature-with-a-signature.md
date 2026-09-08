---
# CSL-compatible fields
title: "Koopman analysis of sea surface temperature with a signature kernel"
author:
  - literal: "Nozomi Sugiura"
  - literal: "Satoshi Osafune"
  - literal: "Shinya Kouketsu"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2602.19494"

# Custom fields
paper_id: "2602.19494"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "kernel-mean-embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-08T09:16:28Z"
created_at: "2026-09-08T09:16:28Z"
---

# Koopman analysis of sea surface temperature with a signature kernel

**Authors**: Nozomi Sugiura, Satoshi Osafune, Shinya Kouketsu
**Date**: 2026-09-07
**Paper ID**: [openalex:2602.19494](https://arxiv.org/abs/2602.19494)

## Summary

This paper develops a trajectory-based Koopman method for sea surface temperature (SST) forecasting and spectral analysis by lifting annual SST segments with a signature kernel and learning the one-year shift operator. By leveraging signature kernels to compare paths via iterated-integral features, the framework encodes finite-time history to capture memory effects in SST-only evolution. Implemented via kernel extended dynamic mode decomposition (kEDMD) on signature-kernel Gram matrices, the approach improves out-of-sample multiyear forecast skill over climatology baselines and uncovers coherent spectral modes.

## Key Contributions

- Develops a trajectory-based Koopman method for sea surface temperature (SST) using a signature kernel to lift annual SST segments and learn the one-year shift operator.
- Encodes finite-time history through trajectory segments rather than instantaneous fields to capture memory effects in SST-only evolution.
- Improves out-of-sample multiyear forecast skill relative to a climatology baseline while revealing coherent spectral modes via kernel extended dynamic mode decomposition (kEDMD) on signature-kernel Gram matrices.

## Archivist Review

Applied strict review policies. No new reusable concepts or open questions met the high bar for permanent vault storage.

### Rejected Candidates
- [open_question] Physical Interpretation of Koopman Modes (`physical-interpretation-koopman-modes`) - paper_local: Paper-local open question asking to physically interpret sea surface temperature modes for a specific regional dataset.

## Links

- [Abstract](https://arxiv.org/abs/2602.19494)
- [PDF](https://arxiv.org/pdf/2602.19494)

