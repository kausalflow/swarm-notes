---
# CSL-compatible fields
title: "Time Series Forecasting based on Solana Digital Asset Dataset"
author:
  - literal: "Yufeng Xiao"
  - literal: "Minxing Wang"
  - literal: "Pravel Braslavski"
  - literal: "Dmitry I. Ignatov"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.19521"

# Custom fields
paper_id: "2608.19521"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "solana-digital-asset-dataset"
concept_slugs:
  []
dataset_slugs:
  - "solana-digital-asset-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:18:49Z"
created_at: "2026-08-23T05:18:49Z"
---

# Time Series Forecasting based on Solana Digital Asset Dataset

**Authors**: Yufeng Xiao, Minxing Wang, Pravel Braslavski, Dmitry I. Ignatov
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.19521](https://arxiv.org/abs/2608.19521)

## Summary

This paper introduces the first comprehensive Solana digital asset time series dataset, combining token-level transactions and prices with ecosystem-level decentralized exchange (DEX) activity across 1,584 tokens. The authors analyze market-structure dynamics during rapid ecosystem growth—identifying synchronized activity peaks tied to major events such as the January 2025 'Trump' token phenomenon—and evaluate forecasting models including PatchTST, Chronos, and statistical baselines for three-day-ahead market capitalization prediction. Results show that models like PatchTST perform well, and that ecosystem-level covariates such as total DEX volume and SOL price significantly contribute to predictive performance.

## Key Contributions

- Introduces the first comprehensive Solana digital asset time series dataset containing 1,584 tokens and 27 variables combining token transactions, prices, and DEX activity.
- Characterizes the DEX-driven token market dynamics, identifying synchronized activity peaks linked to ecosystem events like the January 2025 'Trump' token phenomenon.
- Evaluates forecasting performance on three-day-ahead market-capitalization prediction, demonstrating that PatchTST and Chronos outperform traditional statistical baselines while highlighting the predictive power of ecosystem covariates like SOL price and DEX volume.

## Limitations

Limited to daily resolution over a single year of rapid ecosystem growth (March 2024 to March 2025).

## Open Questions & Future Work

- [[cross-chain-external-validity-and-temporal-generalization]]

## Archivist Review

The paper introduces a domain-specific digital asset dataset for Solana forecasting. The dataset itself is added to the approved datasets vault note, and the cross-chain external validity open question is approved. The concept candidate is rejected as the contribution is fundamentally dataset curation rather than a novel conceptual mechanism.

### Approved Open Questions
- Cross-Chain External Validity and Temporal Generalization: Determining whether specialized blockchain dataset structures and forecasting models generalize across different Layer-1 or Layer-2 network architectures is vital for building universally robust financial and on-chain predictive systems.

### Rejected Candidates
- [concept] Solana Digital Asset Dataset (`solana-digital-asset-dataset`) - not_reusable: This is primarily a dataset contribution rather than an algorithmic or methodological concept.

## Datasets

- [[solana-digital-asset-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2608.19521)
- [PDF](https://arxiv.org/pdf/2608.19521)

