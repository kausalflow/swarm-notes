---
# CSL-compatible fields
title: "Solow system driven by $α$-stable Lévy process"
author:
  - literal: "Yiren Wang"
  - literal: "Shenglan Yuan"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.20997"

# Custom fields
paper_id: "2607.20997"
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
processed_at: "2026-07-26T07:30:46Z"
created_at: "2026-07-26T07:30:46Z"
---

# Solow system driven by $α$-stable Lévy process

**Authors**: Yiren Wang, Shenglan Yuan
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.20997](https://arxiv.org/abs/2607.20997)

## Summary

This paper extends the Solow economic growth model by incorporating $\alpha$-stable Lévy process shocks and time-varying capital elasticity to capture macroeconomic heavy tails, jumps, and infinite variance. The authors derive closed-form conditional characteristic functions, establish a dual mean-reversion integral representation, and design an estimation strategy tailored to Lévy data properties. Empirical application to Argentina, Colombia, and the United States shows superior crisis tracking and parameter alignment compared to standard Gaussian Ornstein-Uhlenbeck benchmarks.

## Key Contributions

- Derives the stationary distribution and closed-form conditional characteristic function for a Solow-type growth model driven by $\alpha$-stable Lévy shocks with time-varying capital elasticity.
- Designs a robust estimation strategy based on objective functions that respect the probabilistic properties of Lévy-driven data without relying on finite variance.
- Demonstrates on Argentine, Colombian, and US data that the Lévy specification outperforms the Gaussian Ornstein-Uhlenbeck benchmark in crisis-period tracking while maintaining stable quarterly capital adjustment speeds ($\eta \approx 0.05$).

## Archivist Review

Both candidates are specific to economic growth modeling (Solow model extensions) rather than general machine learning or time-series forecasting methodology, so they are rejected in favor of maintaining high selectivity for the vault.

### Rejected Candidates
- [concept] Solow system driven by $\alpha$-stable Lévy process (`solow-system-driven-by-alpha-stable-levy-process`) - not_reusable: This is a specific macroeconomic application (Solow growth model with Lévy noise) rather than a general, highly reusable time-series forecasting method or neural architecture.
- [open_question] Open-Economy and Skewed Lévy Extensions (`skewed-levy-open-economy-solow-extensions`) - low_impact: The question focuses on specific extensions of an economic growth model rather than a broad, foundational time-series or machine learning research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.20997)
- [PDF](https://arxiv.org/pdf/2607.20997)

