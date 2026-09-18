---
# CSL-compatible fields
title: "Research on the Price Prediction Algorithms of Major Cryptocurrencies and a Basic Transaction Framework"
author:
  - literal: "Shengjian Chen"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18149"

# Custom fields
paper_id: "2609.18149"
paper_source: "openalex"
domain: "finance"
tags:
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
processed_at: "2026-09-18T09:18:21Z"
created_at: "2026-09-18T09:18:21Z"
---

# Research on the Price Prediction Algorithms of Major Cryptocurrencies and a Basic Transaction Framework

**Authors**: Shengjian Chen
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18149](https://arxiv.org/abs/2609.18149)

## Summary

This paper analyzes the long-term price trends and weekly K-line similarities of Bitcoin and Ethereum, introducing data denoising and smoothing techniques to derive cyclical price patterns and optimal trading timing. The author introduces momentum opening and closing prices to better capture continuous 24/7 market dynamics and proposes a novel arbitrage strategy treating the cryptocurrency ecosystem as a relatively independent financial market. Additionally, the work highlights central bank digital currencies (CBDC) adoption as a crucial macro signal for exiting cryptocurrency holdings.

## Key Contributions

- Identified long-term consistent price trends and weekly K-line similarities between Bitcoin and Ethereum through time series analysis.
- Proposed momentum opening/closing prices to replace traditional nominal opening/closing prices for 24/7 financial markets.
- Designed an arbitrage strategy based on the observation that the cryptocurrency market acts as a relatively independent financial market.

## Archivist Review

The paper discusses basic time series denoising and introduces a local 'momentum closing price' concept and arbitrage strategy for major cryptocurrencies. Neither proposed open question rises to the level of a major, reusable research bottleneck across machine learning time-series literature. Therefore, all candidates are rejected to maintain vault rigor.

### Rejected Candidates
- [open_question] Refined Momentum Closing Price Definition (`refined-momentum-closing-price-definition`) - low_impact: Refining a local price indicator formula is too narrow and incremental for a standalone vault question.
- [open_question] Universality of Weighted Momentum Functions (`universality-of-weighted-momentum-functions`) - paper_local: Testing whether a specific momentum weighting function generalizes to altcoins is paper-local evaluation future work.

## Links

- [Abstract](https://arxiv.org/abs/2609.18149)
- [PDF](https://arxiv.org/pdf/2609.18149)

