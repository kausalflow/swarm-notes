---
# CSL-compatible fields
title: "A Later Test Set Is Not a New Domain: Pretraining Familiarity Survives a Contamination-Free Hold-Out"
author:
  - literal: "Mahdi Naser Moghadasi"
  - literal: "Faezeh Ghaderi"
issued:
  date-parts:
    - [2026, 9, 9]
url: "https://arxiv.org/abs/2609.10357"

# Custom fields
paper_id: "2609.10357"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "pretrained-models"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-12T08:55:38Z"
created_at: "2026-09-12T08:55:38Z"
---

# A Later Test Set Is Not a New Domain: Pretraining Familiarity Survives a Contamination-Free Hold-Out

**Authors**: Mahdi Naser Moghadasi, Faezeh Ghaderi
**Date**: 2026-09-09
**Paper ID**: [openalex:2609.10357](https://arxiv.org/abs/2609.10357)

## Summary

The paper evaluates thirteen time-series forecasters (classical, per-dataset trained, and pretrained) on a contamination-free temporal hold-out dataset where all observations postdate the release of the models. The findings reveal that pretrained models still dominate, but their advantage is governed by corpus familiarity rather than inherent series difficulty or seasonal strength, demonstrating that temporal hold-outs prevent window memorization but preserve domain familiarity.

## Key Contributions

- Constructed a contamination-free temporal hold-out benchmark consisting of observations published after the release dates of thirteen evaluated forecasters across seven groups from five domains.
- Demonstrated that pretrained time-series models win 5 of 7 benchmark groups under the temporal hold-out protocol, while losing to classical baselines on specific series like daily exchange rates.
- Showed that performance advantages are driven by corpus familiarity (e.g., TimesFM excelling on Wikipedia pageviews matching its pretraining data) rather than intrinsic series properties such as seasonal strength or spectral entropy.
- Established that temporal hold-outs eliminate exact window memorization but retain domain familiarity, indicating that future time-series benchmarks require explicit domain hold-outs relative to disclosed training corpora.

## Open Questions & Future Work

- [[corpus-stratified-time-series-benchmarks]]

## Archivist Review

The paper investigates the impact of temporal hold-outs on time-series foundation model evaluation, demonstrating that pretraining familiarity survives contamination-free splits and that performance is driven by corpus familiarity rather than temporal novelty. One open question addressing corpus-stratified benchmarking was approved as it targets a major gap in evaluating time-series foundation models. No concepts were approved as the paper focuses on an evaluation audit rather than a novel standalone forecasting architecture or method.

### Approved Open Questions
- Corpus-Stratified Time-Series Benchmarks: Crucial for isolating true generalization capabilities from pretraining corpus familiarity and dataset leakage in zero-shot time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2609.10357)
- [PDF](https://arxiv.org/pdf/2609.10357)

