---
# CSL-compatible fields
title: "Event-Aware Loss Design for Forecasting of Convective Precipitation and Lightning"
author:
  - literal: "ChangJae Lee"
  - literal: "Heecheol Yang"
  - literal: "Byeonggwon Kim"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2606.25937"

# Custom fields
paper_id: "2606.25937"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "generative-adversarial-network"
  - "gan"
  - "multimodal"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "lightning-informed-loss-weighting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-27T07:43:04Z"
created_at: "2026-06-27T07:43:04Z"
---

# Event-Aware Loss Design for Forecasting of Convective Precipitation and Lightning

**Authors**: ChangJae Lee, Heecheol Yang, Byeonggwon Kim
**Date**: 2026-06-24
**Paper ID**: [openalex:2606.25937](https://arxiv.org/abs/2606.25937)

## Summary

This paper addresses the under-prediction of high-intensity convective weather events in deep learning models by introducing an event-aware multi-task framework. The proposed model, based on a Patch-cGAN, jointly predicts precipitation amount, rainfall probability, and lightning, guided by a novel lightning-informed spatial loss-weighting strategy. Evaluations on 2025 Korean Peninsula summer data show that this approach significantly improves forecasting accuracy for extreme precipitation thresholds and lightning occurrence compared to standard NWP and AI benchmarks.

## Key Contributions

- Introduced an Event-Aware multi-task deep-learning framework (Patch-cGAN) that jointly predicts precipitation and lightning occurrence to better represent convective processes.
- Developed a lightning-informed loss-weighting strategy that effectively mitigates the under-prediction of extreme events by prioritizing convective regions.
- Demonstrated superior performance against conventional NWP and AI benchmarks in extreme precipitation forecasting (40 mm/6 h threshold) and lightning prediction on 2025 Korean Peninsula data.

## Key Concepts

- [[lightning-informed-loss-weighting]]: A spatial loss-weighting mechanism that uses auxiliary observation maps to prioritize the prediction of critical events in deep learning models.

## Archivist Review

The paper introduces a effective spatial loss-weighting mechanism to address rare-event forecasting in meteorology. I approved this concept under a more generalized name to encourage its reuse in other spatiotemporal forecasting domains. No specific datasets were noted as critical or broadly reusable outside of this experiment.

### Approved Concepts
- Lightning-Informed Loss Weighting: It addresses the critical challenge of rare-event under-prediction in high-impact weather forecasting by spatially biasing the model's focus during training.

### Rejected Candidates
- [concept] lightning-informed loss-weighting strategy (`lightning-informed-loss-weighting-strategy`) - other: The name was too specific to the paper's domain; renamed to a more canonical, reusable concept slug.

## Links

- [Abstract](https://arxiv.org/abs/2606.25937)
- [PDF](https://arxiv.org/pdf/2606.25937)

