---
# CSL-compatible fields
title: "When the Martingale Never Stops Firing: Anytime-Valid Gating on Real Forecast Streams"
author:
  - literal: "Weijia Han"
  - literal: "Lisha Qu"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2608.30502"

# Custom fields
paper_id: "2608.30502"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
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
processed_at: "2026-09-03T09:17:02Z"
created_at: "2026-09-03T09:17:02Z"
---

# When the Martingale Never Stops Firing: Anytime-Valid Gating on Real Forecast Streams

**Authors**: Weijia Han, Lisha Qu
**Date**: 2026-08-31
**Paper ID**: [openalex:2608.30502](https://arxiv.org/abs/2608.30502)

## Summary

This paper investigates the deployment of anytime-valid conformal test martingales as statistical monitors for online correction loops in time-series forecasting. While these methods guarantee false-alarm control under exchangeability, empirical evaluations across five real forecasting streams reveal that temporal dependency and feedback loops cause 100% false-alarm rates. To address this failure, the authors recommend null-calibration controls and demonstrate that simple Huber-style gating of filter updates provides robust spike mitigation without relying on strict theoretical validity claims.

## Key Contributions

- Demonstrated that conformal test martingales with anytime-valid guarantees fail catastrophically on real-world dependent forecasting streams, firing in 135 out of 135 clean-stream runs at alpha = 0.05 due to exchangeability violations.
- Evaluated online updates of a Kalman adapter correcting frozen time-series foundation models across five forecasting streams, showing that repeated false alarms keep the drift response active and amplify transients.
- Proposed Huber-style gating of the filter's own updates as a robust, validity-free alternative that cuts isolated-spike degradation by an order of magnitude without dataset-specific tuning.

## Limitations

The anytime-valid conformal test martingale guarantee breaks down under temporal dependency and feedback loops between the monitor and the learner, necessitating null-calibration controls and mechanism traces for deployment.

## Open Questions & Future Work

- [[anytime-valid-inference-non-exchangeable-streams]]

## Archivist Review

Strict adherence to vault sparsity and review policy. No new concepts met the rigorous threshold for permanent notes, as Huber-style gating is standard robust statistics and the martingale failure is an empirical evaluation finding rather than a new architectural component. The single open question on anytime-valid inference under non-exchangeability was retained as it captures an important theoretical bottleneck.

### Approved Open Questions
- Anytime-Valid Inference on Non-Exchangeable Streams: Crucial for bridging the gap between theoretical guarantees of e-value methods/martingales and their practical failures in online machine learning pipelines where data dependence and feedback loops are ubiquitous.

### Rejected Candidates
- [concept] Huber-Style Gating (`huber-style-gating`) - not_novel: Huber-style robust gating is a standard robust statistics mechanism rather than a novel standalone ML concept central to forecasting theory.
- [concept] Conformal Test Martingales Online Failure (`conformal-test-martingales-online-failure`) - low_impact: Describes an evaluation finding and limitation of an existing technique rather than a reusable architectural concept or method.

## Links

- [Abstract](https://arxiv.org/abs/2608.30502)
- [PDF](https://arxiv.org/pdf/2608.30502)

