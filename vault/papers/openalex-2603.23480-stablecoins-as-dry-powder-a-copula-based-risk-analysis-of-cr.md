---
# CSL-compatible fields
title: "Stablecoins as Dry Powder: A Copula-Based Risk Analysis of Cryptocurrency Markets"
author:
  - literal: "Elliot Jones"
  - literal: "Toshiko Matsui"
  - literal: "William Knottenbelt"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2603.23480"

# Custom fields
paper_id: "2603.23480"
paper_source: "openalex"
domain: "finance"
tags:
  - "finance"
  - "risk-analysis"
  - "forecasting"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "stablecoin-dry-powder-role"
  - "copula-based-risk-analysis"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T15:44:20Z"
created_at: "2026-03-27T15:44:20Z"
---

# Stablecoins as Dry Powder: A Copula-Based Risk Analysis of Cryptocurrency Markets

**Authors**: Elliot Jones, Toshiko Matsui, William Knottenbelt
**Date**: 2026-03-24
**Paper ID**: [openalex:2603.23480](https://arxiv.org/abs/2603.23480)

## Summary

This study investigates the systemic risk transmission from stablecoins to the broader cryptocurrency market using copula-based methodologies to quantify volatility and activity dependence. The authors show significant in-sample causality across multiple time horizons, confirming that stablecoin metrics, particularly volume and upside volatility, function as 'dry powder' influencing market risk. Incorporating these stablecoin factors into forecasting models demonstrably reduces Mean Squared Error (MSE) for cryptocurrency predictions. Furthermore, the inclusion of these factors leads to a measurable reduction in risk within a practical volatility targeting framework, establishing a clear economic utility for stablecoin analysis in risk management.

## Key Contributions

- Demonstrated in-sample causality between stablecoin metrics (volume, volatility) and cryptocurrency market activity across daily, weekly, and monthly time horizons.
- Quantified that incorporating stablecoin factors significantly reduces the Mean Squared Error (MSE) for cryptocurrency forecasting models.
- Established that stablecoin volume and upside volatility act as 'dry powder' indicators linked to broader market volatility.
- Showed an economic value by demonstrating reduced risk in a cryptocurrency volatility targeting model when stablecoin factors are included.

## Limitations

The analysis is limited to in-sample causality, and the specific definition/selection of 'stablecoin factors' (volume vs. specific stablecoin types) is not detailed enough for immediate replication.

## Open Questions & Future Work

- [[crypto-leads-stablecoin-causality-test]]
- [[intra-day-timeframe-analysis]]

## Key Concepts

- [[stablecoin-dry-powder-role]]: The concept that stablecoin volume and volatility act as a systemic risk transmitter and reactive 'dry powder' for the broader cryptocurrency market.
- [[copula-based-risk-analysis]]: Utilizing copula models to statistically quantify the dependence structure and risk transmission pathways between stablecoin activity and the volatility of the broader cryptocurrency market.

## Archivist Review

Two core concepts were approved: the 'Stablecoin Dry Powder Role' which reframes stablecoins as a systemic risk driver, and 'Copula-Based Risk Analysis' detailing the primary methodological approach. Two open questions were approved focusing on future causal investigation: one for reverse causality testing and one for replicating the analysis at a finer intra-day granularity to resolve empirical gaps. Other candidates were rejected as they were either boilerplate results or subcomponents of the approved mechanisms.

### Approved Concepts
- Stablecoin Dry Powder Role: The paper explicitly frames stablecoins not just as a stable medium, but as 'dry powder' whose volume and volatility influence the entire crypto market risk profile. This reframes a core DeFi component's systemic function.
- Copula-Based Risk Analysis: The paper's core methodological contribution is the application of copula models specifically for quantifying risk transmission between stablecoins and general cryptocurrency markets.

### Approved Open Questions
- Reverse Causality Testing: Investigating the reverse causality helps confirm or refute the hypothesis that cryptocurrencies act as a safe haven for stablecoins during stress, which is a key theoretical relationship in digital asset markets.
- Intra-day Timeframe Replication: Intra-day analysis could resolve the empirical divergence found between theoretical expectations (that downside shocks are instantaneous) and the findings based on daily data.

### Rejected Candidates
- [open_question] MSE Reduction in Crypto Forecasting (`crypto-forecasting-mse-reduction`) - generic: This is a standard result of including a good feature, not a novel reusable concept or question.
- [concept] Cryptocurrency Volatility Targeting Model (`volatility-targeting-model`) - subcomponent_of_broader_mechanism: Volatility targeting is a well-known financial strategy; the novelty is using stablecoin factors *within* it, which is covered by the Dry Powder concept.

## Links

- [Abstract](https://arxiv.org/abs/2603.23480)
- [PDF](https://arxiv.org/pdf/2603.23480)

