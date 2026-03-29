---
# CSL-compatible fields
title: "Modeling and Forecasting Tail Risk Spillovers: A Component-Based CAViaR Approach"
author:
  - literal: "Demetrio Lacava"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25217"

# Custom fields
paper_id: "2603.25217"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "caviar-se-tail-risk-forecasting"
  - "recursive-partial-correlation-spillover-selection"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:07:13Z"
created_at: "2026-03-29T06:07:13Z"
---

# Modeling and Forecasting Tail Risk Spillovers: A Component-Based CAViaR Approach

**Authors**: Demetrio Lacava
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25217](https://arxiv.org/abs/2603.25217)

## Summary

This paper introduces CAViaR-SE, a novel extension of the Conditional Autoregressive Value at Risk (CAViaR) model designed for more accurate tail risk forecasting across multiple assets. The core innovation is decomposing the conditional Value at Risk into a component representing inherent risk and a spillover component derived from a combination of influential assets' tail risks. These influential assets are selected using a new recursive partial correlation algorithm that ensures parsimony while capturing multiple spillover drivers. Empirical tests on Dow Jones stocks demonstrate that the spillover component significantly shifts the conditional quantile dynamics, leading to statistically superior out-of-sample tail risk forecasts confirmed by Model Confidence Set analysis.

## Key Contributions

- Introduction of the Component-Based CAViaR with Spillover Effects (CAViaR-SE) model for improved tail risk forecasting.
- The model decomposes Conditional VaR into proper-risk and spillover components, where the latter is driven by influential asset tail risks.
- The use of a recursive partial correlation algorithm to select influential spillover sources with minimal parameterization.
- Empirical validation showing CAViaR-SE provides statistically superior, well-calibrated tail risk forecasts compared to standard CAViaR models on DJIA stocks.

## Limitations

The analysis is limited to Dow Jones Industrial Average stocks, and the general applicability to other asset classes or markets is not explicitly detailed.

## Open Questions & Future Work

- [[refining-spillover-asset-selection-criteria]]

## Key Concepts

- [[caviar-se-tail-risk-forecasting]]: An extension of the CAViaR model that decomposes conditional VaR into a proper-risk component and a spillover component based on influential assets' tail risks.
- [[recursive-partial-correlation-spillover-selection]]: A procedure used to identify a minimal set of influential assets whose tail risks drive the spillover component in the CAViaR-SE model.

## Archivist Review

Two core concepts were approved: the novel CAViaR-SE model itself, representing a new structural decomposition for tail risk, and the specific recursive partial correlation algorithm used for feature selection within that model. One open question was approved, focusing on refining the mechanism for selecting influential spillover assets, which is a key methodological point in this type of modeling. The general approach to risk modeling and quantile forecasting justifies the scarcity of approvals.

### Approved Concepts
- Component-Based CAViaR with Spillover Effects (CAViaR-SE): This is the novel, core econometric model proposed by the paper for tail risk forecasting.
- Recursive Partial Correlation Algorithm for Spillovers: This is the specific, novel method used to select the influential assets driving the spillover component, reducing model complexity.

### Approved Open Questions
- Alternative influential asset selection: The current selection method relies solely on recursive partial correlation; exploring alternative, theoretically justified selection criteria could improve the identification of true risk contagion channels.

### Rejected Candidates
- [open_question] Alternative influential asset selection (`refining-spillover-asset-selection-criteria`) - other: The provided evidence excerpt for this open question seems to reference a citation not present in the abstract, but the general question about refining the selection mechanism is a valid, non-boilerplate future direction for this class of econometric model. Approved based on the core idea.

## Links

- [Abstract](https://arxiv.org/abs/2603.25217)
- [PDF](https://arxiv.org/pdf/2603.25217)

