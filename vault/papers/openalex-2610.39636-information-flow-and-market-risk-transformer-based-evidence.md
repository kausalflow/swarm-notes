---
# CSL-compatible fields
title: "Information Flow and Market Risk: Transformer-Based Evidence on Sentiment and Volatility Dynamics"
author:
  - literal: "Szymon Lis"
  - literal: "Robert Ślepaczuk"
  - literal: "Paweł Sakowski"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.39636"

# Custom fields
paper_id: "2610.39636"
paper_source: "openalex"
domain: "finance"
tags:
  - "transformer"
  - "bert"
  - "llm"
  - "time-series"
  - "forecasting"
  - "sentiment-analysis"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-01T11:33:57Z"
created_at: "2026-11-01T11:33:57Z"
---

# Information Flow and Market Risk: Transformer-Based Evidence on Sentiment and Volatility Dynamics

**Authors**: Szymon Lis, Robert Ślepaczuk, Paweł Sakowski
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.39636](https://arxiv.org/abs/2610.39636)

## Summary

This study investigates whether transformer-based news sentiment extracted via ModernFinBERT improves equity volatility forecasts for eleven US stocks beyond conventional predictors like VIX and AAII sentiment. Through rigorous walk-forward testing at 1, 5, and 22-day horizons, the authors find that a naive persistence benchmark and HAR-VIX dominate, with text-based sentiment providing statistically insignificant improvements in only a tiny fraction of comparisons. The findings caution against assuming a general forecasting advantage from transformer-derived text predictors and emphasize the necessity of robust evaluation frameworks.

## Key Contributions

- Investigated whether transformer-based financial news sentiment (extracted via ModernFinBERT) improves equity volatility forecasts across 11 US stocks.
- Compared volatility persistence models, HAR-VIX, AAII investor sentiment, and news sentiment specifications under walk-forward testing at 1, 5, and 22-day horizons.
- Demonstrated through rigorous statistical testing and blinded audits of 2,700 news texts that transformer-based news sentiment fails to provide a general, statistically significant incremental forecasting advantage over naive persistence and HAR-VIX benchmarks.

## Limitations

The study evaluates only eleven US stocks and relies on ModernFinBERT for sentiment extraction, meaning findings may vary with broader universes or alternative LLM-based sentiment extractors.

## Archivist Review

The paper provides a rigorous negative empirical evaluation of transformer-based news sentiment for equity volatility forecasting, showing that text sentiment fails to outperform naive persistence or HAR-VIX baselines. Since no novel architectural mechanism or open research question of vault-grade generality was introduced, all candidates were rejected.

### Rejected Candidates
- [concept] ModernFinBERT (`modernfinbert`) - not_reusable: ModernFinBERT is a specific off-the-shelf model name rather than a reusable architectural or methodological mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2610.39636)
- [PDF](https://arxiv.org/pdf/2610.39636)

