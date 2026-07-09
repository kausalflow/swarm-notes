---
# CSL-compatible fields
title: "Video-based detection of cessation of breathing in pre-term infants using machine learning"
author:
  - literal: "Dineo Serame"
  - literal: "Lionel Tarassenko"
  - literal: "Mauricio Villarroel"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.05230"

# Custom fields
paper_id: "2607.05230"
paper_source: "openalex"
domain: "medicine"
tags:
  - "cnn"
  - "multimodal"
  - "anomaly-detection"
architectures:
  - "convolutional-neural-network"
datasets:
  []
concept_slugs:
  - "cessation-of-breathing-cobe-detection"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:19:32Z"
created_at: "2026-07-09T08:19:32Z"
---

# Video-based detection of cessation of breathing in pre-term infants using machine learning

**Authors**: Dineo Serame, Lionel Tarassenko, Mauricio Villarroel
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.05230](https://arxiv.org/abs/2607.05230)

## Summary

This paper investigates the feasibility of detecting cessation of breathing (COBE) in preterm infants using non-contact video monitoring to address limitations of traditional contact-based sensors. The authors extract respiratory signals from torso motion in video and train ResNet-based models for COBE detection. Their results show that video-only models are effective, and hybrid integration with standard clinical signals like impedance pneumography significantly boosts detection performance, underscoring the clinical utility of video as a complementary monitoring modality.

## Key Contributions

- Proposes a non-contact, video-based approach for monitoring cessation of breathing (COBE) in preterm infants, achieving a balanced accuracy of 76.9% using camera-only data.
- Demonstrates that hybrid models integrating video-derived signals with standard impedance pneumography (IP) significantly improve COBE detection, reaching a balanced accuracy of 90.6%.
- Validates that video-derived respiratory signals provide clinically complementary information to traditional contact-based sensors in the NICU.

## Open Questions & Future Work

- [[robust-neonatal-video-monitoring]]

## Key Concepts

- [[cessation-of-breathing-cobe-detection]]: A non-contact method for detecting respiratory pauses in preterm infants using video-derived signals and hybrid physiological data.

## Archivist Review

The paper is a straightforward application of video-based respiratory signal extraction. I have approved the task definition as a concept because it represents a distinct, reusable methodology for integrating non-contact sensors with clinical physiological time series. The open question regarding robustness was approved because it addresses a fundamental, well-defined gap in moving non-contact medical monitoring into real-world clinical settings, moving beyond simple performance reporting to systemic reliability concerns.

### Approved Concepts
- Cessation of Breathing (COBE) Detection: The paper introduces a specialized, clinically relevant task for non-contact neonatal monitoring that provides a template for integrating non-contact sensor data with standard physiological signals.

### Approved Open Questions
- Robustness of Neonatal Video Monitoring: Identifying solutions for these environmental bottlenecks is essential for transitioning non-contact medical monitoring from controlled research settings to reliable bedside clinical care.

## Links

- [Abstract](https://arxiv.org/abs/2607.05230)
- [PDF](https://arxiv.org/pdf/2607.05230)

