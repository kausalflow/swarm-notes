---
# CSL-compatible fields
title: "Leveraging Time-Series Foundation Models for Financial Crime Detection"
author:
  - literal: "Danae Natalie Savvidi"
  - literal: "H. Çağrı Bilgi"
  - literal: "Kubilay Atasu"
  - literal: "Arie Van Deursen A"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29667"

# Custom fields
paper_id: "2610.29667"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "graph-neural-network"
  - "gnn"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "temporal-context-edge-enrichment-tcee"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:11:47Z"
created_at: "2026-10-24T09:11:47Z"
---

# Leveraging Time-Series Foundation Models for Financial Crime Detection

**Authors**: Danae Natalie Savvidi, H. Çağrı Bilgi, Kubilay Atasu, Arie Van Deursen A
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29667](https://arxiv.org/abs/2610.29667)

## Summary

This paper introduces Temporal-Context Edge Enrichment (TCEE), a framework that leverages frozen time-series foundation models (TSFMs) to summarize account transaction histories and enrich transaction representations for financial crime detection. Across multiple AMLWorld datasets and an Ethereum phishing dataset, TCEE significantly outperforms existing baselines in both edge and node classification tasks, while also offering faster training times.

## Key Contributions

- Introduces Temporal-Context Edge Enrichment (TCEE), a framework that summarizes account transaction histories with a frozen time-series foundation model to enrich transaction representations.
- Improves PR-AUC over the strongest evaluated baseline on five AMLWorld datasets by a relative 10.8% on average while training 6.0x faster end-to-end.
- Demonstrates that feeding TSFM-generated account representations into a GNN on an Ethereum phishing dataset improves PR-AUC by 14.5% for node classification.

## Open Questions & Future Work

- [[generalization-to-real-bank-data]]

## Key Concepts

- [[temporal-context-edge-enrichment-tcee]]: A framework that summarizes account transaction histories using frozen time-series foundation models to enrich transaction representations for financial crime detection.

## Archivist Review

Approved the core methodological framework concept and the specific open question regarding transfer to real-world incomplete banking data, maintaining high selectivity and adhering strictly to vault standards.

### Approved Concepts
- Temporal-Context Edge Enrichment (TCEE): Core novel methodological framework introduced in the paper for financial crime detection.

### Approved Open Questions
- Real-World Financial Data Generalization: Assessing generalization to real-world financial data is critical for validating the practical utility of time-series foundation models in production anti-money laundering systems.

## Links

- [Abstract](https://arxiv.org/abs/2610.29667)
- [PDF](https://arxiv.org/pdf/2610.29667)

