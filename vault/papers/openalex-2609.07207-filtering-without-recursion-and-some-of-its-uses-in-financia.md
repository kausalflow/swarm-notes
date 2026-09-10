---
# CSL-compatible fields
title: "Filtering without recursion and some of its uses in financial economics"
author:
  - literal: "Simon Donker van Heel"
  - literal: "Neil Shephard"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.07207"

# Custom fields
paper_id: "2609.07207"
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
processed_at: "2026-09-10T09:17:49Z"
created_at: "2026-09-10T09:17:49Z"
---

# Filtering without recursion and some of its uses in financial economics

**Authors**: Simon Donker van Heel, Neil Shephard
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.07207](https://arxiv.org/abs/2609.07207)

## Summary

This paper develops a time series filter defined at each time point as the minimizer of a discounted convex combination of observed and expected losses, eliminating the need for recursion. The filter can be estimated via simulation to arbitrary accuracy with O(1) computational complexity per time point and executed in parallel across all time steps. Applied to over 1.5 million high-frequency financial trades with infinite variance noise, the method robustly computes a preaveraged price process that yields a flat volatility signature plot down to the one-second level, overcoming the bias of standard linear methods.

## Key Contributions

- Develops a time series filter defined at each time point as the minimizer of a discounted convex combination of observed and expected losses.
- Shows that the proposed filter can be estimated via simulation to arbitrary accuracy in O(1) flops per time point and executed in parallel across all time steps.
- Applies the method to robustly compute a preaveraged price process for over 1.5 million intraday trades with infinite noise variance, successfully eliminating microstructure noise bias down to the 1-second level.

## Archivist Review

No novel conceptual methodology meriting a standalone vault entry was proposed; standard time series filtering without recursion is the core focus. No critical named datasets were mentioned.

## Links

- [Abstract](https://arxiv.org/abs/2609.07207)
- [PDF](https://arxiv.org/pdf/2609.07207)

