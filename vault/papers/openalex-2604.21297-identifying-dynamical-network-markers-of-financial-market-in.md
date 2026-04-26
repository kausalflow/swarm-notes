---
# CSL-compatible fields
title: "Identifying dynamical network markers of financial market instability"
author:
  - literal: "Mariko I. Ito"
  - literal: "Hiroyuki Hasada"
  - literal: "Yudai Honma"
  - literal: "Takaaki Ohnishi"
  - literal: "Tsutomu Watanabe"
  - literal: "Kazuyuki Aihara"
issued:
  date-parts:
    - [2026, 4, 23]
url: "https://arxiv.org/abs/2604.21297"

# Custom fields
paper_id: "2604.21297"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "anomaly-detection"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dynamical-network-marker-theory"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-26T06:54:39Z"
created_at: "2026-04-26T06:54:39Z"
---

# Identifying dynamical network markers of financial market instability

**Authors**: Mariko I. Ito, Hiroyuki Hasada, Yudai Honma, Takaaki Ohnishi, Tsutomu Watanabe, Kazuyuki Aihara
**Date**: 2026-04-23
**Paper ID**: [openalex:2604.21297](https://arxiv.org/abs/2604.21297)

## Summary

This study applies Dynamical Network Marker (DNM) theory to detect early warning signals of financial market instability using high-dimensional order placement and execution data from the Tokyo Stock Exchange. By modeling individual market participants as interacting elements, the authors characterize precursors to critical transitions, specifically large price movements. Experimental results indicate that the proposed DNM-based framework can successfully identify these signals on a daily timescale. The findings offer a pathway toward developing robust, real-time early warning systems for market volatility.

## Key Contributions

- Adapts Dynamical Network Marker (DNM) theory to high-dimensional multivariate time series of market participant trading activities.
- Demonstrates that DNM-based indicators can provide early warning signals for large price movements in Tokyo Stock Exchange order data on a daily timescale.
- Establishes a framework for treating individual market participants as interacting elements in a complex system for instability detection.

## Open Questions & Future Work

- [[robust-dnm-forecasting-aggregation-exogenous-shocks]]

## Key Concepts

- [[dynamical-network-marker-theory]]: A theoretical framework that identifies indicators of critical slowing down in high-dimensional systems to forecast regime shifts.

## Archivist Review

The paper demonstrates a clear application of Dynamical Network Marker (DNM) theory to high-dimensional time series. I approved the theory as a reusable concept and defined a focused open question regarding the challenges of applying closed-system dynamical models to open, exogenous financial environments. No datasets were approved as the Tokyo Stock Exchange order data is proprietary and not a shared/public benchmark dataset.

### Approved Concepts
- Dynamical Network Marker (DNM) Theory: DNM theory acts as the core methodological framework for detecting precursors to critical transitions in high-dimensional financial systems.

### Approved Open Questions
- Robust DNM-Based Financial Forecasting: Establishing a robust, actionable, and scalable early-warning indicator is the primary bottleneck for transitioning DNM theory from a descriptive analytical tool to a functional component of financial risk management.

## Links

- [Abstract](https://arxiv.org/abs/2604.21297)
- [PDF](https://arxiv.org/pdf/2604.21297)

