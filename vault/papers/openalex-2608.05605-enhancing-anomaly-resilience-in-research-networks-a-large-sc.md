---
# CSL-compatible fields
title: "Enhancing Anomaly Resilience in Research Networks: A Large-Scale Forecasting Benchmark for Dynamic Security Baselining"
author:
  - literal: "Mohammad Arafath Uddin Shariff"
  - literal: "Byrav Ramamurthy"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.05605"

# Custom fields
paper_id: "2608.05605"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "robustness"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:40:42Z"
created_at: "2026-08-09T05:40:42Z"
---

# Enhancing Anomaly Resilience in Research Networks: A Large-Scale Forecasting Benchmark for Dynamic Security Baselining

**Authors**: Mohammad Arafath Uddin Shariff, Byrav Ramamurthy
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.05605](https://arxiv.org/abs/2608.05605)

## Summary

This paper presents a comprehensive forecasting benchmark and anomaly-integration framework to establish dynamic security baselines for Research and Education Networks (RENs), addressing the challenge of distinguishing legitimate, bursty scientific traffic from volumetric attacks like DDoS. Using a large-scale 57-day Internet2 dataset spanning ten backbone routers, the authors systematically evaluate six model families across 960 configurations. Results show that long-sequence forecasting architectures, particularly TiDE, substantially reduce baseline prediction error and improve anomaly resilience.

## Key Contributions

- Evaluated six model families from SARIMA to state-of-the-art long-sequence architectures (TiDE, PatchTST) across 960 experimental configurations for dynamic security baselining in Research and Education Networks.
- Demonstrated that advanced architectures like TiDE reduce baseline prediction error by 30-42% compared to traditional methods, enhancing the separation between legitimate bursty scientific traffic ('elephant flows') and volumetric attacks.
- Introduced an anomaly-integration strategy that improves model robustness by 3.3% in noisy operational environments.

## Open Questions & Future Work

- [[long-term-seasonal-evaluations]]
- [[spatio-temporal-ren-baselining]]

## Archivist Review

The paper presents an extensive benchmark evaluating existing time-series models for security baselining in Research and Education Networks, so no novel standalone concepts qualify for vault notes. The dataset used is a proprietary Internet2 backbone dump, which is not a standard public benchmark in the vault's database registry. However, the explicit open questions regarding seasonal evaluation and spatio-temporal network baselines are reusable, high-value research directions and have been approved.

### Approved Open Questions
- Long-Term Seasonal and Academic Cycle Evaluation: Crucial for evaluating the temporal stability and concept drift resilience of security baseline models in critical infrastructure over extended operational periods.
- Spatio-Temporal Network Security Baselines: Important for improving global anomaly detection accuracy by leveraging multi-router spatial topologies rather than isolated single-node observations.

## Links

- [Abstract](https://arxiv.org/abs/2608.05605)
- [PDF](https://arxiv.org/pdf/2608.05605)

