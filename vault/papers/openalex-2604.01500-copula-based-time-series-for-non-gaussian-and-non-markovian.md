---
# CSL-compatible fields
title: "Copula-Based Time Series for Non-Gaussian and Non-Markovian Stationary Processes"
author:
  - literal: "Sven Pappert"
  - literal: "Harry Joe"
issued:
  date-parts:
    - [2026, 4, 2]
url: "https://arxiv.org/abs/2604.01500"

# Custom fields
paper_id: "2604.01500"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "copula-based-time-series-modeling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-05T06:08:31Z"
created_at: "2026-04-05T06:08:31Z"
---

# Copula-Based Time Series for Non-Gaussian and Non-Markovian Stationary Processes

**Authors**: Sven Pappert, Harry Joe
**Date**: 2026-04-02
**Paper ID**: [openalex:2604.01500](https://arxiv.org/abs/2604.01500)

## Summary

This paper presents a generalization of copula-based models for univariate, stationary time series, designed to capture complex temporal dependencies beyond the Markovian assumption. By integrating Markov sequences of order p and q-dependent processes, the proposed approach extends flexibility for non-Gaussian data. The authors analytically relate these models to established Gaussian frameworks, such as ARMA and GARCH(1,1), and evaluate their performance on real-world probabilistic forecasting tasks including inflation and wind energy.

## Key Contributions

- Formalizes a generalization of copula-based time series models that incorporates Markov sequences of order p and q-dependent sequences.
- Establishes analytical connections between the proposed copula-based models and classical Gaussian-ARMA and Gaussian-GARCH(1,1) frameworks.
- Demonstrates empirical performance in probabilistic forecasting tasks using US inflation and German wind energy production datasets.

## Key Concepts

- [[copula-based-time-series-modeling]]: A framework for modeling univariate time series dependence by capturing finite-dimensional joint distributions via copulas.

## Archivist Review

I approved the core framework of copula-based time series modeling because it provides a principled statistical alternative to neural methods for handling non-Gaussian temporal dependencies. I rejected the initial concept candidate in favor of a slightly more descriptive title to ensure it remains distinct in the vault. No datasets or open questions were approved as the paper focuses on theoretical formalization rather than introducing novel, standalone datasets or identifying specific, actionable research gaps.

### Approved Concepts
- Copula-Based Time Series Modeling: Provides a flexible, non-parametric framework for modeling complex dependencies in non-Gaussian, non-Markovian stationary processes.

### Rejected Candidates
- [concept] Copula-Based Time Series (`copula-based-time-series`) - duplicate_existing: The title was slightly ambiguous; renamed to 'Copula-Based Time Series Modeling' for clarity and to avoid collision with generic terminology.

## Links

- [Abstract](https://arxiv.org/abs/2604.01500)
- [PDF](https://arxiv.org/pdf/2604.01500)

