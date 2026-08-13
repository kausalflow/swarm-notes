---
# CSL-compatible fields
title: "Towards Collaborative Joint Perception and Prediction: Framework, Baseline Evaluation, and Deployment Perspectives"
author:
  - literal: "Lei Wan"
  - literal: "Hannan Ejaz Keen"
  - literal: "Alexey Vinel"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09541"

# Custom fields
paper_id: "2608.09541"
paper_source: "openalex"
domain: "robotics"
tags:
  - "autonomous-agent"
  - "prediction"
  - "multimodal"
  - "object-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:09:40Z"
created_at: "2026-08-13T06:09:40Z"
---

# Towards Collaborative Joint Perception and Prediction: Framework, Baseline Evaluation, and Deployment Perspectives

**Authors**: Lei Wan, Hannan Ejaz Keen, Alexey Vinel
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09541](https://arxiv.org/abs/2608.09541)

## Summary

This work explores Collaborative Joint Perception and Prediction (Co-P&amp;P) for Connected Autonomous Vehicles, a paradigm unifying collaborative perception and motion prediction via V2X communication. The authors present a conceptual framework, evaluate different fusion strategies—finding prediction-level fusion inferior to detection- and tracking-level fusion—and establish a minimal end-to-end prototype using the RENO neural codec and FutureDet. Experimental results demonstrate that collaboration improves forecasting accuracy while neural compression maintains these benefits with a 34x reduction in communication bandwidth.

## Key Contributions

- Proposes a conceptual framework for Collaborative Joint Perception and Prediction (Co-P&amp;P) that unifies collaborative perception with motion prediction to mitigate perception error accumulation and visual occlusions.
- Compares different fusion strategies (detection-level, tracking-level, and prediction-level), showing that prediction-level fusion results in degraded system performance.
- Implements a minimal end-to-end Co-P&amp;P prototype coupling point-cloud sharing via the RENO neural codec with joint detection-forecasting via FutureDet, demonstrating enhanced forecasting accuracy at roughly 34x lower communication bandwidth.

## Links

- [Abstract](https://arxiv.org/abs/2608.09541)
- [PDF](https://arxiv.org/pdf/2608.09541)

