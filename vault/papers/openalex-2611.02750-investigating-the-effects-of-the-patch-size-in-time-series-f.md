---
# CSL-compatible fields
title: "Investigating the effects of the patch size in Time Series Foundation Models"
author:
  - literal: "Jad Yehya"
  - literal: "Andrei-Tiberiu Pantea"
  - literal: "Aymeric Dieuleveut"
  - literal: "Matthieu Kowalski"
  - literal: "Thomas Moreau"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.02750"

# Custom fields
paper_id: "2611.02750"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "long-context"
  - "evaluation"
architectures:
  - "encoder-only"
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:51:18Z"
created_at: "2026-11-05T12:51:18Z"
---

# Investigating the effects of the patch size in Time Series Foundation Models

**Authors**: Jad Yehya, Andrei-Tiberiu Pantea, Aymeric Dieuleveut, Matthieu Kowalski, Thomas Moreau
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.02750](https://arxiv.org/abs/2611.02750)

## Summary

This paper investigates the role of patch size in patch-based time-series foundation models, comparing encoder-only and decoder-only architectures across 97 GIFT-Eval tasks. The results show that encoder-only models prefer smaller patches and benefit from longer context lengths up to 2048, whereas decoder-only models exhibit U-shaped performance curves where optimal patch sizes scale with the forecasting horizon. Pareto analyses further highlight complementary deployment regimes, with decoder-only models offering greater efficiency and encoder-only models achieving superior accuracy.

## Key Contributions

- Investigates the effect of patch size in patch-based time-series foundation models through controlled comparisons of encoder-only and decoder-only architectures trained on identical data and budgets.
- Demonstrates across 97 GIFT-Eval tasks that encoder-only models consistently benefit from smaller patches, while decoder-only models exhibit U-shaped performance trends peaking at intermediate patch sizes.
- Reveals that the preferred decoder patch size scales directly with the forecasting horizon, whereas encoder-only performance improves with context lengths up to 2048.
- Provides Pareto analyses showing decoder-only models excel in computational efficiency while encoder-only models achieve peak accuracy.

## Limitations

Future work could explore scaling limits and broader architectural interactions across larger pre-training corpora.

## Open Questions & Future Work

- [[independent-patch-sizes-and-architectural-components-in-tsfms]]

## Archivist Review

Strictly adhered to scarcity limits by approving zero concepts (as patching and encoder/decoder architectures are general existing design dimensions) and exactly one targeted open question exploring the decoupling of input and output patch sizes and architectural components in time series foundation models.

### Approved Open Questions
- Disentangling Patch Size and Architecture: Understanding the disentangled impact of input versus output patch sizes and specific architectural components is crucial for establishing universal design principles for time series foundation models rather than architecture-specific heuristics.

## Links

- [Abstract](https://arxiv.org/abs/2611.02750)
- [PDF](https://arxiv.org/pdf/2611.02750)

