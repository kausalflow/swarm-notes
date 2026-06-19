---
# CSL-compatible fields
title: "EventDrive: Event Cameras for Vision-Language Driving Intelligence"
author:
  - literal: "D H Lu"
  - literal: "R K Li"
  - literal: "Ao Liang"
  - literal: "Lingdong Kong"
  - literal: "Wei Yin"
  - literal: "Lai Xing Ng"
  - literal: "Benoit R. Cottereau"
  - literal: "Camille Simon-Chane"
  - literal: "Wei Tsang Ooi"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.18242"

# Custom fields
paper_id: "2606.18242"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "vlm"
  - "event-camera"
  - "autonomous-agent"
  - "planning"
  - "mixture-of-experts"
  - "moe"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-horizon-event-pyramid"
  - "temporal-horizon-mixture-of-experts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:26:04Z"
created_at: "2026-06-19T09:26:04Z"
---

# EventDrive: Event Cameras for Vision-Language Driving Intelligence

**Authors**: D H Lu, R K Li, Ao Liang, Lingdong Kong, Wei Yin, Lai Xing Ng, Benoit R. Cottereau, Camille Simon-Chane, Wei Tsang Ooi
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.18242](https://arxiv.org/abs/2606.18242)

## Summary

EventDrive addresses the limitations of frame-based vision-language models in autonomous driving by introducing an event-aware model suite. It features a large-scale benchmark covering four core driving dimensions and the EventDrive-VLM model, which integrates asynchronous event streams with RGB inputs. The model architecture uses a multi-horizon event pyramid and a temporal-horizon mixture-of-experts module to provide robust, high-fidelity perception and decision-making in adverse conditions.

## Key Contributions

- Introduces EventDrive, a benchmark suite for autonomous driving unifying events, RGB, and language across perception, understanding, prediction, and planning.
- Develops EventDrive-VLM, which leverages a multi-horizon event pyramid and temporal-horizon MoE to fuse asynchronous event data with frames.
- Demonstrates that incorporating event sensors significantly improves temporal precision, motion awareness, and robustness in challenging driving scenarios like glare and rapid movement.

## Open Questions & Future Work

- [[event-based-vlm-driving-stack-integration]]

## Key Concepts

- [[multi-horizon-event-pyramid]]: A hierarchical encoding scheme for integrating asynchronous event streams across multiple temporal scales in vision-language models.
- [[temporal-horizon-mixture-of-experts]]: A mixture-of-experts routing mechanism for adaptive fusion of asynchronous event streams and frame-based visual features across temporal horizons.

## Archivist Review

I approved the two core architectural contributions, as they offer reusable mechanisms for multiscale, multisensor fusion that extend well beyond the current driving-specific application. The open question was approved to track the systemic challenge of integrating high-frequency, asynchronous data into semantic vision-language architectures for full-stack autonomy. I rejected the request to approve the 'EventDrive' benchmark itself, as it is a single-paper suite, and prioritized concepts that represent generalizable modeling principles.

### Approved Concepts
- Multi-horizon event pyramid: It provides a scalable hierarchical approach for integrating high-frequency, asynchronous sensor data with standard vision-language backbones.
- Temporal-horizon mixture-of-experts: It allows for dynamic selection of temporal context and sensor fusion, which is vital for balancing high-frequency event fidelity with semantic consistency.

### Approved Open Questions
- Event-Based VLM Driving Stack Integration: Establishing this integration is necessary for moving beyond isolated perception tasks to holistic, safety-critical decision-making architectures.

## Links

- [Abstract](https://arxiv.org/abs/2606.18242)
- [PDF](https://arxiv.org/pdf/2606.18242)

