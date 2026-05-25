---
# CSL-compatible fields
title: "Stock market telepathy: Graph neural networks predicting the secret conversations between MINT and G7 countries"
author:
  - literal: "Nurbanu Bursa"
issued:
  date-parts:
    - [2026, 5, 22]
url: "https://arxiv.org/abs/2506.01945"

# Custom fields
paper_id: "2506.01945"
paper_source: "openalex"
domain: "finance"
tags:
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-25T08:50:01Z"
created_at: "2026-05-25T08:50:01Z"
---

# Stock market telepathy: Graph neural networks predicting the secret conversations between MINT and G7 countries

**Authors**: Nurbanu Bursa
**Date**: 2026-05-22
**Paper ID**: [openalex:2506.01945](https://arxiv.org/abs/2506.01945)

## Summary

This paper investigates the economic interdependence between G7 and MINT countries by modeling their stock market indices as a complex network. The study utilizes the Multivariate Time series Graph Neural Network (MTGNN) to capture spatio-temporal dynamics that traditional models often fail to identify. Empirical results demonstrate that MTGNN provides superior predictive accuracy for stock index forecasting and reveals critical hub nations within these economic blocks.

## Key Contributions

- Demonstrates that the MTGNN (Multivariate Time series Graph Neural Network) framework effectively captures spatio-temporal dependencies in global stock market indices for MINT and G7 economies.
- Identifies US and Canada as the primary influential G7 stock indices and Indonesia and Türkiye as the most influential MINT countries through GNN-based relationship analysis.
- Validates that MTGNN consistently outperforms traditional statistical methods in multi-step stock market price forecasting over the 2012-2024 period.

## Open Questions & Future Work

- [[gnn-predictive-versus-causal-graphs]]

## Archivist Review

I approved the open question regarding the distinction between predictive and causal graphs in GNN-based time series forecasting, as this is a fundamental conceptual limitation in the field. I rejected the concept candidate 'MTGNN' as it is a pre-existing architectural framework, not a novel contribution requiring a new vault note. No datasets were approved as they were not explicitly named or described in a reusable format.

### Approved Open Questions
- Predictive vs Causal Graphs in GNNs: Crucial for validating the reliability of deep learning models in high-stakes environments like economic policy and portfolio management, as predictive performance alone does not ensure the robustness required for structural decision-making.

### Rejected Candidates
- [concept] Multivariate Time series Graph Neural Network (MTGNN) (`mtgnn`) - not_novel: This is a known, existing architectural framework and not a novel contribution of this specific study.

## Links

- [Abstract](https://arxiv.org/abs/2506.01945)
- [PDF](https://arxiv.org/pdf/2506.01945)

