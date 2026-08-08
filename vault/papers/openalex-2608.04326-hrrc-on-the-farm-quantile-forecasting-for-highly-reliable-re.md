---
# CSL-compatible fields
title: "HRRC on the Farm: Quantile Forecasting for Highly-Reliable Remote Control via LEO Networks"
author:
  - literal: "André Gomes"
  - literal: "Jie Wang"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04326"

# Custom fields
paper_id: "2608.04326"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "robustness"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:34:50Z"
created_at: "2026-08-08T05:34:50Z"
---

# HRRC on the Farm: Quantile Forecasting for Highly-Reliable Remote Control via LEO Networks

**Authors**: André Gomes, Jie Wang
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04326](https://arxiv.org/abs/2608.04326)

## Summary

This paper investigates highly-reliable remote control for agricultural automation over LEO satellite networks by framing it as a quantile forecasting problem. The authors propose a high-quantile estimator to predict latency spikes and satisfy stringent reliability constraints. Evaluated on a real-world OneWeb dataset from a US agricultural hub, the estimator enables remote-controlled farm vehicles to achieve operating speeds up to 138.6% higher than conventional approaches.

## Key Contributions

- Casts highly-reliable remote control over LEO networks as a quantile forecasting problem to predict latency spikes
- Proposes a high-quantile estimator for latency prediction tailored to mission-critical agricultural automation
- Demonstrates on a real-world OneWeb dataset that the estimator enables remote-controlled vehicles to operate at speeds up to 138.6% higher while meeting reliability requirements

## Archivist Review

Applied strict selectivity: no novel reusable concepts or open questions met the bar for permanent vault storage. The paper studies an applied setting (LEO network remote control via quantile forecasting) using standard high-quantile estimation, which does not introduce a standalone methodological primitive.

### Rejected Candidates
- [open_question] Extreme-Value Theory and Prototyping (`extreme-value-theory-prototyping-for-leo-remote-control`) - weak_evidence: The proposed future work is a paper-local combination of future prototyping and standard extreme-value theory extensions without a reusable technical formulation.

## Links

- [Abstract](https://arxiv.org/abs/2608.04326)
- [PDF](https://arxiv.org/pdf/2608.04326)

