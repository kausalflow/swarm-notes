---
# CSL-compatible fields
title: "Learning When to Listen: Gated Affect Fusion for Human Motion Prediction"
author:
  - literal: "J W Huang"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00296"

# Custom fields
paper_id: "2607.00296"
paper_source: "openalex"
domain: "computer-vision,nlp"
tags:
  - "transformer,multimodal,attention-mechanism,time-series,forecasting,motion-prediction,gating-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gated-cross-modal-fusion"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:36:53Z"
created_at: "2026-07-04T07:36:53Z"
---

# Learning When to Listen: Gated Affect Fusion for Human Motion Prediction

**Authors**: J W Huang
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00296](https://arxiv.org/abs/2607.00296)

## Summary

This paper investigates the role of facial affect as a complementary cue for human motion forecasting in noisy, unconstrained environments. The author demonstrates that simple multimodal fusion often introduces noise, leading to decreased performance compared to pose-only baselines. To address this, the proposed Gated Affect Transformer (GAT) uses a gating mechanism to selectively incorporate affective information. Empirical evaluations reveal that facial affect provides performance gains only within short-to-medium temporal horizons, emphasizing the necessity of horizon-aware multimodal integration.

## Key Contributions

- Identifies that naive early multimodal concatenation of facial affect with body pose degrades human motion prediction performance in-the-wild.
- Introduces the Gated Affect Transformer (GAT), which improves forecasting accuracy by dynamically regulating the affective information stream.
- Establishes that facial affect cues are only beneficial for short-to-medium forecasting horizons (e.g., up to 30 frames), while long-term motion is dominated by kinematic continuity.

## Open Questions & Future Work

- [[scaling-behavioral-cues-long-term-forecasting]]

## Key Concepts

- [[gated-cross-modal-fusion]]: A mechanism for dynamically controlling the integration of secondary or noisy input streams in multimodal time-series forecasting to prevent performance degradation.

## Archivist Review

I approved the broader concept of 'Gated Cross-Modal Fusion' because the paper's core contribution is the recognition that naive fusion fails and requires a gated mechanism to manage noise. I rejected the 'Gated Affect Transformer' as it is a specific instantiation of this mechanism. The open question was approved for capturing the critical limitation of using auxiliary behavioral cues in long-horizon forecasting.

### Approved Concepts
- Gated Cross-Modal Fusion: The paper highlights a critical issue in multimodal time-series modeling where auxiliary, noisy signals degrade performance if concatenated naively, necessitating a learnable regulation mechanism.

### Approved Open Questions
- Scaling Behavioral Cues for Forecasting: This question defines the boundary between immediate reactive motion (affect-driven) and long-term behavioral planning, which is a core bottleneck in human-centric forecasting.

### Rejected Candidates
- [concept] Gated Affect Transformer (GAT) (`gated-affect-transformer-gat`) - subcomponent_of_broader_mechanism: The proposed architecture is a specific implementation of a broader 'gated cross-modal fusion' concept, which I have approved instead.

## Links

- [Abstract](https://arxiv.org/abs/2607.00296)
- [PDF](https://arxiv.org/pdf/2607.00296)

