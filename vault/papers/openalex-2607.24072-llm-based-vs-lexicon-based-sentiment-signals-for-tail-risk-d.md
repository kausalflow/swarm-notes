---
# CSL-compatible fields
title: "LLM-Based vs. Lexicon-Based Sentiment Signals for Tail-Risk Detection in Meme Stocks"
author:
  - literal: "Paul Kilian"
  - literal: "Markus Kleffmann"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24072"

# Custom fields
paper_id: "2607.24072"
paper_source: "openalex"
domain: "finance"
tags:
  - "sentiment-analysis"
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:27:18Z"
created_at: "2026-07-30T07:27:18Z"
---

# LLM-Based vs. Lexicon-Based Sentiment Signals for Tail-Risk Detection in Meme Stocks

**Authors**: Paul Kilian, Markus Kleffmann
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24072](https://arxiv.org/abs/2607.24072)

## Summary

This paper empirically compares lexicon-based (VADER) and Large Language Model (LLM)-based sentiment analysis for extracting signals from Reddit social media discourse regarding meme stocks. The LLM approach produces multidimensional representations of emotional polarity, bullishness, sarcasm likelihood, and topical relevance, whereas the baseline uses standard lexicons. Evaluating both through lead/lag correlation, OLS regression, directional classification, and a quantile-based early-warning framework reveals that while LLMs offer richer linguistic structure, their predictive relationship with extreme tail-risk market returns remains heterogeneous and unstable across assets.

## Key Contributions

- Compares lexicon-based (VADER) and LLM-based sentiment analysis for social media discourse on Reddit (r/WallStreetBets) regarding meme stocks (GME, AMC, NOK).
- Finds that LLM-based indicators generate richer multidimensional representations (emotional polarity, bullishness, sarcasm likelihood, topical relevance) with stronger asset-specific statistical structure than lexicon baselines.
- Demonstrates through lead/lag correlation, OLS regression, ROC-AUC, and quantile-based early-warning frameworks that increased linguistic expressiveness does not necessarily translate into stable forecasting performance across assets in retail-driven volatility regimes.

## Limitations

Relationship between sentiment signals and extreme market movements remains heterogeneous across assets, indicating unstable forecasting performance in retail-driven volatility regimes.

## Archivist Review

The paper provides an empirical comparison between lexicon-based and LLM-based sentiment signals for tail-risk detection in meme stocks. None of the proposed open questions represent fundamental, cross-cutting theoretical bottlenecks that generalize across time series analysis; they are specific to financial sentiment pipelines and deployment considerations. Therefore, all candidates were rejected to maintain strict vault standards.

### Rejected Candidates
- [open_question] Cross-Asset Robustness of LLM Sentiment (`cross-asset-robustness-llm-sentiment`) - low_impact: This question addresses application-specific generalization in financial text mining rather than a fundamental methodological bottleneck across time series forecasting.
- [open_question] Methodological Standardization of LLM Indicators (`methodological-standardization-llm-financial-indicators`) - not_novel: Standardizing prompt designs and model backbones is routine implementation hygiene rather than a canonical theoretical gap.
- [open_question] Real-Time Tail-Risk Monitoring with LLMs (`real-time-tail-risk-monitoring-llms`) - low_impact: Operational latency and model-version control are general deployment engineering topics rather than foundational modeling limitations.

## Links

- [Abstract](https://arxiv.org/abs/2607.24072)
- [PDF](https://arxiv.org/pdf/2607.24072)

