---
# CSL-compatible fields
title: "Volatility in Prediction Markets: A Structural Approach"
author:
  - literal: "Weiye Xi"
  - literal: "Ciamac C. Moallemi"
  - literal: "Mallesh Pai"
  - literal: "Shouqiao Want"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08199"

# Custom fields
paper_id: "2607.08199"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "kalshi"
concept_slugs:
  - "wright-fisher-deadline-resolution-component"
  - "glosten-milgrom-order-flow-component"
dataset_slugs:
  - "kalshi"
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:24:59Z"
created_at: "2026-07-12T07:24:59Z"
---

# Volatility in Prediction Markets: A Structural Approach

**Authors**: Weiye Xi, Ciamac C. Moallemi, Mallesh Pai, Shouqiao Want
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08199](https://arxiv.org/abs/2607.08199)

## Summary

This paper proposes a structural volatility model for binary prediction markets, which diverge significantly from standard asset market return-based dynamics. The model decomposes volatility into a Wright-Fisher component, reflecting deadline-driven uncertainty resolution, and a Glosten-Milgrom component, capturing volatility from informed trading reflected in market microstructure. Evaluated on Kalshi contracts, the framework outperforms classical GARCH models and provides an interpretable mechanism for understanding volatility across different event types. Results suggest that structural volatility drivers transfer well across varied market categories, providing robust forecasts for derivatives pricing and risk management.

## Key Contributions

- Introduces a structural volatility modeling framework for binary prediction markets by decomposing dynamics into deadline-resolution and order-flow effects.
- Demonstrates that structural specifications significantly outperform traditional ARCH/GARCH baseline models in predicting volatility for prediction market contracts.
- Shows that the proposed structural variables exhibit high transferability across diverse market categories, such as economics and sports.

## Open Questions & Future Work

- [[prediction-market-channel-correlation]]
- [[prediction-market-jump-modeling]]

## Key Concepts

- [[wright-fisher-deadline-resolution-component]]: A structural component that models volatility as a function of the shrinking binary uncertainty as a contract approaches its resolution deadline.
- [[glosten-milgrom-order-flow-component]]: A structural component that captures volatility contributions derived from informed trading activities observable through market order flow.

## Archivist Review

The paper introduces a structured approach to volatility modeling in prediction markets by decomposing dynamics into deadline-resolution and order-flow effects. These concepts represent a shift from return-based GARCH models to structure-aware mechanisms, and the open questions highlight the fundamental limitations in modeling the interaction and jump-like dynamics of these markets. Kalshi is approved as a key dataset that serves as the basis for these structural findings.

### Approved Concepts
- Wright-Fisher deadline-resolution component: Provides a mechanistic foundation for volatility in markets with binary outcomes and finite time horizons, distinguishing it from standard ARCH/GARCH processes.
- Glosten-Milgrom order-flow component: Integrates market microstructure dynamics—specifically informed trading impact—into the volatility forecasting framework.

### Approved Open Questions
- Correlating Market Information Channels: Understanding the dependency between public information and order flow is crucial for accurate volatility modeling and derivatives pricing in prediction markets, as assuming independence may lead to biased conditional variance forecasts.
- Modeling Jumps and Events: This is technically important for enhancing the accuracy of risk management and market-making strategies in event-heavy prediction markets where price movements are not purely driven by smooth, information-arrival processes.

## Datasets

- [[kalshi]]

## Links

- [Abstract](https://arxiv.org/abs/2607.08199)
- [PDF](https://arxiv.org/pdf/2607.08199)

