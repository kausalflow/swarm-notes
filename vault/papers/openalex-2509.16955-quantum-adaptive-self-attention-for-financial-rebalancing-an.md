---
# CSL-compatible fields
title: "Quantum Adaptive Self-Attention for Financial Rebalancing: An Empirical Study on Automated Market Makers in Decentralized Finance"
author:
  - literal: "Chi-Sheng Chen"
  - literal: "Aidan Hung-Wen Tsai"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2509.16955"

# Custom fields
paper_id: "2509.16955"
paper_source: "openalex"
domain: "finance"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
  - "time-series"
  - "hybrid-quantum-classical-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quantum-adaptive-self-attention-qasa"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:00:42Z"
created_at: "2026-04-24T07:00:42Z"
---

# Quantum Adaptive Self-Attention for Financial Rebalancing: An Empirical Study on Automated Market Makers in Decentralized Finance

**Authors**: Chi-Sheng Chen, Aidan Hung-Wen Tsai
**Date**: 2026-04-21
**Paper ID**: [openalex:2509.16955](https://arxiv.org/abs/2509.16955)

## Summary

This paper proposes Quantum Adaptive Self-Attention (QASA), a novel hybrid quantum–classical attention mechanism that replaces standard linear projections with variational quantum circuits (VQCs) to process financial time-series. By formulating automated market maker (AMM) rebalancing as a binary detection task, the authors show that QASA offers a more favorable performance-stability trade-off than pure classical or pure quantum models. Empirical results on BTCUSDC data demonstrate that QASA-Sequence outperforms traditional transformer and ensemble baselines in both return and Sharpe ratio.

## Key Contributions

- Introduced Quantum Adaptive Self-Attention (QASA), a hybrid quantum-classical attention module utilizing VQCs for query-key-value construction.
- Formulated automated market maker (AMM) rebalancing as a binary detection task for time-series decision-making.
- Demonstrated that QASA-Sequence achieves superior risk-adjusted performance (13.99% return, Sharpe 1.76) compared to classical ensembles and pure quantum baselines on BTCUSDC data.

## Open Questions & Future Work

- [[robustness-of-quantum-attention-to-regime-shifts]]

## Key Concepts

- [[quantum-adaptive-self-attention-qasa]]: A hybrid quantum–classical self-attention module that replaces linear projections with variational quantum circuits to process queries, keys, and values.

## Archivist Review

The paper introduces a novel drop-in hybrid quantum-classical attention module, QASA, which is deemed a reusable architectural component for time-series models. The open question regarding the robustness of these quantum encodings to financial regime shifts is substantial and important for the future of hybrid quantum-classical forecasting. Other candidates were rejected for being overly specific to the paper's financial application rather than fundamental algorithmic contributions.

### Approved Concepts
- Quantum Adaptive Self-Attention (QASA): QASA introduces a specialized hybrid integration of Variational Quantum Circuits (VQCs) into the core self-attention mechanism, providing a modular architectural component for high-dimensional time-series features.

### Approved Open Questions
- Quantum Attention Regime Robustness: Assessing long-term stability is critical for deploying automated rebalancing agents in real-world DeFi liquidity provision, where failure to adapt to new regimes can lead to significant financial loss.

### Rejected Candidates
- [concept] AMM Rebalancing as Binary Detection (`amm-rebalancing-as-binary-detection`) - paper_local: Formulating a specific task as a binary classification problem is a standard application-specific modelling choice rather than a reusable architectural concept.

## Links

- [Abstract](https://arxiv.org/abs/2509.16955)
- [PDF](https://arxiv.org/pdf/2509.16955)

