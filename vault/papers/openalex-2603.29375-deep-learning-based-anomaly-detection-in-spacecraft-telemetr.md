---
# CSL-compatible fields
title: "Deep Learning-Based Anomaly Detection in Spacecraft Telemetry on Edge Devices"
author:
  - literal: "C. Goetze"
  - literal: "Tim Schlippe"
  - literal: "Daniel Lakey"
issued:
  date-parts:
    - [2026, 3, 31]
url: "https://arxiv.org/abs/2603.29375"

# Custom fields
paper_id: "2603.29375"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "neural-architecture-search"
  - "model-compression"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-03T06:07:19Z"
created_at: "2026-04-03T06:07:19Z"
---

# Deep Learning-Based Anomaly Detection in Spacecraft Telemetry on Edge Devices

**Authors**: C. Goetze, Tim Schlippe, Daniel Lakey
**Date**: 2026-03-31
**Paper ID**: [openalex:2603.29375](https://arxiv.org/abs/2603.29375)

## Summary

This paper investigates the feasibility of deploying deep learning-based anomaly detection on resource-constrained spacecraft edge devices. By comparing three detection paradigms, the authors identify forecasting and thresholding as the most effective approach for telemetry data, achieving high performance on the European Space Agency Anomaly Dataset. They further employ multi-objective neural architecture optimization to drastically compress these models, demonstrating that advanced anomaly detection is viable on CubeSat hardware with minimal memory and operational overhead.

## Key Contributions

- Evaluates and compares three distinct deep learning anomaly detection paradigms—forecasting & threshold, direct classification, and image classification—for spacecraft telemetry.
- Demonstrates that a forecasting-based anomaly detection approach achieves a superior 92.7% CEF0.5 score on the European Space Agency Anomaly Dataset.
- Applies multi-objective neural architecture optimization to reduce model footprint by 97.1% in RAM and 99.4% in operations, enabling deployment on resource-constrained CubeSat hardware.

## Open Questions & Future Work

- [[spacecraft-anomaly-detection-hybrid-optimization]]

## Archivist Review

The paper provides a focused empirical study on optimizing anomaly detection for edge devices but does not introduce sufficiently novel or reusable methodological concepts that aren't already captured by existing terminology like neural architecture search or model compression. The open question regarding hybrid ensemble optimization for constrained edge environments is approved as it addresses a significant bottleneck in deploying robust AI for high-stakes, resource-limited hardware.

### Approved Open Questions
- Hybrid Ensemble Anomaly Detection Optimization: As deep learning becomes more prevalent in space missions, developing robust, efficient, and multi-objective-aware anomaly detection systems is critical for mission safety, given the inability to upgrade hardware post-deployment.

### Rejected Candidates
- [concept] Anomaly Detection for Spacecraft Telemetry (`anomaly-detection-for-spacecraft-telemetry`) - generic: This is a domain application rather than a reusable methodological concept or architectural pattern.
- [dataset] European Space Agency Anomaly Dataset (`esa-anomaly-dataset`) - low_impact: While useful for this paper, it is a specialized domain dataset; per policy, I am being extremely conservative with dataset approvals and prioritizing those with wider general-purpose utility.

## Links

- [Abstract](https://arxiv.org/abs/2603.29375)
- [PDF](https://arxiv.org/pdf/2603.29375)

