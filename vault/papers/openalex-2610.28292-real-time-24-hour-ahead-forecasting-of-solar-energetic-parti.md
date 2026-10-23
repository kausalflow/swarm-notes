---
# CSL-compatible fields
title: "Real-Time 24-hour Ahead Forecasting of Solar Energetic Particle Events with SEPNET-PRISM-R"
author:
  - literal: "Yian Yu"
  - literal: "Yang Chen"
  - literal: "Lulu Zhao"
  - literal: "Kathryn Whitman"
  - literal: "Ward Manchester"
  - literal: "T. I. Gombosi"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.28292"

# Custom fields
paper_id: "2610.28292"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "interpretability"
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
processed_at: "2026-10-23T09:40:29Z"
created_at: "2026-10-23T09:40:29Z"
---

# Real-Time 24-hour Ahead Forecasting of Solar Energetic Particle Events with SEPNET-PRISM-R

**Authors**: Yian Yu, Yang Chen, Lulu Zhao, Kathryn Whitman, Ward Manchester, T. I. Gombosi
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.28292](https://arxiv.org/abs/2610.28292)

## Summary

The paper introduces SEPNET-PRISM-R, a real-time system designed for 24-hour ahead probabilistic forecasting of solar energetic particle (SEP) events. By integrating multimodal solar data—such as active region patches, flare features, coronal mass ejection characteristics, and historical proton flux—the framework concurrently predicts SEP occurrences, peak proton flux, soft X-ray flux, and CME velocity. Enhanced by a postprocessing module for cross-validated decision making and interpretable feature importance, the system substantially suppresses false alarm rates while maintaining robust event detection.

## Key Contributions

- Introduces SEPNET-PRISM-R, a near-real-time forecasting system for hourly, 24-hour ahead probabilistic solar energetic particle (SEP) predictions.
- Integrates multimodal solar data including active region patches, flare features, CME characteristics, and historical proton flux to concurrently forecast SEP occurrences, peak proton flux, soft X-ray flux, and CME velocity.
- Incorporates a postprocessing module providing cross-validated decision making, interpretable feature importance quantification, predictive probabilities, and historical analogs to suppress false alarm rates.

## Archivist Review

Strictly adhered to the high threshold for vault curation. The single proposed open question is highly domain-specific to space weather physics (CME/SEP events) and lacks general machine learning or time-series methodological transferability. Therefore, no concepts, datasets, or open questions were approved.

### Rejected Candidates
- [open_question] CME-Driven SEP Event Forecasting (`cme-driven-sep-forecasting-improvement`) - low_impact: The open question focuses primarily on domain-specific space weather modeling (coronal mass ejections and solar energetic particles) rather than generalizable time-series or machine learning methodology.

## Links

- [Abstract](https://arxiv.org/abs/2610.28292)
- [PDF](https://arxiv.org/pdf/2610.28292)

