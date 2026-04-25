---
# CSL-compatible fields
title: "Unlocking the Forecasting Economy: A Suite of Datasets for the Full Lifecycle of Prediction Market: [Experiments & Analysis]"
author:
  - literal: "Huaiyu Jia"
  - literal: "Luofeng Zhou"
  - literal: "Wentao Zhang"
  - literal: "Lin William Cong"
  - literal: "Siguang Li"
  - literal: "Shuo Sun"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20421"

# Custom fields
paper_id: "2604.20421"
paper_source: "openalex"
domain: "finance"
tags:
  - "dataset"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "polymarket-prediction-market-dataset"
concept_slugs:
  []
dataset_slugs:
  - "polymarket-prediction-market-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:15:55Z"
created_at: "2026-04-25T06:15:55Z"
---

# Unlocking the Forecasting Economy: A Suite of Datasets for the Full Lifecycle of Prediction Market: [Experiments & Analysis]

**Authors**: Huaiyu Jia, Luofeng Zhou, Wentao Zhang, Lin William Cong, Siguang Li, Shuo Sun
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20421](https://arxiv.org/abs/2604.20421)

## Summary

This paper introduces a large-scale, unified dataset suite for decentralized prediction markets, specifically targeting the Polymarket platform. By integrating fragmented on-chain and off-chain data—including market creation, trading history, and oracle settlement—the authors enable longitudinal analysis of collective forecasting. The resulting system includes over 770,000 market records and nearly a billion trading events, providing a foundational resource for studying market dynamics and forecasting accuracy. The authors further validate the dataset through descriptive analysis and downstream applications in sports and macroeconomic prediction.

## Key Contributions

- Presents the first comprehensive, continuously maintained dataset suite covering the entire lifecycle of decentralized prediction markets from October 2020 to March 2026.
- Develops a unified relational data system that integrates heterogeneous on-chain and off-chain sources (market metadata, trading records, and oracle-resolution events).
- Demonstrates the utility of the integrated data via empirical case studies on NBA outcome calibration and CPI expectation reconstruction.

## Open Questions & Future Work

- [[oracle-risk-dynamics-prediction-markets]]

## Archivist Review

The paper provides a significant contribution by creating a unified, multi-layered dataset for decentralized prediction markets. The dataset is approved due to its scale and potential for longitudinal financial and behavioral research. The open question regarding oracle risk is approved as it addresses a core systemic challenge inherent to the decentralization of prediction markets.

### Approved Open Questions
- Oracle risk dynamics and behavior: Oracle resolution is a critical point of failure in decentralized prediction markets, making understanding the dynamics around it essential for market design.

### Rejected Candidates
- [dataset] Polymarket (`polymarket`) - other: Renamed to a more descriptive slug for the vault.

## Datasets

- [[polymarket-prediction-market-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2604.20421)
- [PDF](https://arxiv.org/pdf/2604.20421)

