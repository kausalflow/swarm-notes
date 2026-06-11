---
# CSL-compatible fields
title: "Real-time body pose non-verbal communication with a consistency-based reliability measure"
author:
  - literal: "Alina Marcu"
  - literal: "Dragoş Costea"
  - literal: "Cristina Lazar"
  - literal: "Marius Leordeanu"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09390"

# Custom fields
paper_id: "2606.09390"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "robotics"
  - "dataset"
  - "evaluation"
  - "autoregressive"
  - "graph-neural-network"
architectures:
  []
datasets:
  - "IPC-dataset"
concept_slugs:
  - "autoregressive-self-consistency-reliability-measure"
dataset_slugs:
  - "ipc-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:08:42Z"
created_at: "2026-06-11T09:08:42Z"
---

# Real-time body pose non-verbal communication with a consistency-based reliability measure

**Authors**: Alina Marcu, Dragoş Costea, Cristina Lazar, Marius Leordeanu
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09390](https://arxiv.org/abs/2606.09390)

## Summary

This paper addresses the recognition of non-verbal communicative intent from 2D body pose, particularly for real-time person-to-robot interaction in challenging environments like rescue missions. The authors introduce a new dataset of communicative intents and evaluate several skeleton-based models for their performance and latency on embedded hardware. A key contribution is the proposal of an autoregressive self-consistency mechanism that functions as an unsupervised, low-compute reliability signal for predictions. Theoretical analysis demonstrates that prediction confidence increases with consistency, providing a robust solution for edge-deployed robotic systems.

## Key Contributions

- Introduces a dataset of full-body poses annotated with ten distinct communicative intents, specifically curated for real-time person-to-robot communication.
- Evaluates various skeleton graph classifiers and motion-forecasting networks on resource-constrained embedded hardware (NVIDIA Orin Nano) to establish efficiency-accuracy trade-offs.
- Proposes an unsupervised reliability measure based on autoregressive self-consistency, accompanied by theoretical bounds on prediction correctness.

## Open Questions & Future Work

- [[resolving-depth-ambiguity-pose-intent]]

## Key Concepts

- [[autoregressive-self-consistency-reliability-measure]]: An unsupervised uncertainty estimation method that uses the stability of autoregressive predictions as a confidence proxy for classification tasks.

## Archivist Review

Approved the self-consistency reliability measure for its potential as a general lightweight uncertainty quantification technique in sequence modeling. Included the IPC dataset and the open question regarding depth ambiguity as they directly address the core methodological constraints of pose-based intent recognition in robotics. Rejected the long-range aerial deployment question as it relates more to evaluation scale than to an unresolved scientific or algorithmic bottleneck.

### Approved Concepts
- Autoregressive self-consistency reliability measure: Provides a novel, unsupervised method for estimating the reliability of communicative intent predictions from body pose, which is critical for deployment on resource-constrained robotics hardware.

### Approved Open Questions
- Resolving Depth Ambiguity in Intent Recognition: This is a fundamental limitation for real-world robotic interaction, where distinguishing approach/recede gestures is critical for safety and intent accuracy.

## Datasets

- [[ipc-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2606.09390)
- [PDF](https://arxiv.org/pdf/2606.09390)

