---
# CSL-compatible fields
title: "MVP: A Motion-Predictive Speculative Vision Pipeline with Non-Blocking Drift Correction"
author:
  - literal: "Raul Taranco"
  - literal: "Antonio González"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27706"

# Custom fields
paper_id: "2609.27706"
paper_source: "openalex"
domain: "computer-vision"
tags:
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
processed_at: "2026-09-26T09:38:20Z"
created_at: "2026-09-26T09:38:20Z"
---

# MVP: A Motion-Predictive Speculative Vision Pipeline with Non-Blocking Drift Correction

**Authors**: Raul Taranco, Antonio González
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27706](https://arxiv.org/abs/2609.27706)

## Summary

Continuous vision systems suffer from high end-to-end latency due to serialized image capture and processing pipelines. To address this, the authors propose MVP, a motion-predictive speculative vision pipeline that performs perception extrapolation directly in the motion domain using a lightweight ISP hardware extension. By scheduling full backend inference as a background drift correction task off the critical path, MVP achieves up to 66.8% reduction in tail latency and 46% energy savings on object detection tasks.

## Key Contributions

- Proposes MVP, a motion-predictive speculative vision pipeline operating entirely in the motion domain rather than forecasting full images.
- Introduces a lightweight ISP hardware extension reusing existing motion-estimation logic for minimal area and energy overhead.
- Implements a non-blocking drift correction scheduling model running full backend inference periodically off the critical path.
- Demonstrates up to 66.8% reduction in tail latency and 46% energy savings on object detection tasks at a small accuracy cost.

## Limitations

Suffers a small accuracy cost due to motion extrapolation approximations compared to full frame inference.

## Archivist Review

All candidates were reviewed against the strict vault criteria. The proposed concept (MVP Pipeline) and open question (Embedded Deep Optical Flow Prediction) are highly hardware-specific and system-level engineering contributions rather than reusable forecasting methods or fundamental theoretical gaps, so they were rejected.

### Rejected Candidates
- [concept] MVP Pipeline (`mvp-pipeline`) - paper_local: Paper-internal system design and hardware-software integration for mobile vision SoCs rather than a fundamental forecasting or temporal representation method.
- [open_question] Embedded Deep Optical Flow Prediction (`embedded-deep-optical-flow-prediction`) - low_impact: A paper-specific engineering question about porting deep optical flow to specific embedded hardware constraints rather than a core theoretical forecasting bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.27706)
- [PDF](https://arxiv.org/pdf/2609.27706)

