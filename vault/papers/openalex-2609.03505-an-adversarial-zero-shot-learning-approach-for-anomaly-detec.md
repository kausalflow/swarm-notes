---
# CSL-compatible fields
title: "An Adversarial Zero-Shot Learning Approach for Anomaly Detection in Multivariate IoT Traffic Data"
author:
  - literal: "Mahshid Rezakhani"
  - literal: "Tolunay Seyfi"
  - literal: "Fatemeh Afghah"
issued:
  date-parts:
    - [2026, 9, 3]
url: "https://arxiv.org/abs/2609.03505"

# Custom fields
paper_id: "2609.03505"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "variational-autoencoder"
  - "vae"
  - "contrastive-learning"
  - "zero-shot-learning"
  - "multimodal"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-06T09:01:38Z"
created_at: "2026-09-06T09:01:38Z"
---

# An Adversarial Zero-Shot Learning Approach for Anomaly Detection in Multivariate IoT Traffic Data

**Authors**: Mahshid Rezakhani, Tolunay Seyfi, Fatemeh Afghah
**Date**: 2026-09-03
**Paper ID**: [openalex:2609.03505](https://arxiv.org/abs/2609.03505)

## Summary

This paper proposes an adversarial zero-shot learning framework for multivariate time-series anomaly detection in IoT networks, combining a sequence-based VAE with contrastive loss. The method employs encoder-decoder adaptor layers and a destination-based segmentation strategy to achieve zero-shot domain adaptation and align feature distributions across diverse environments without requiring labeled data. Extensive evaluation across six distinct IoT datasets and 44 transfer scenarios demonstrates robust cross-domain generalization.

## Key Contributions

- Proposes an adversarial sequence-based VAE framework with contrastive loss for multivariate time-series anomaly detection.
- Introduces encoder and decoder adaptor layers for zero-shot domain adaptation and feature distribution alignment without raw feature transfer.
- Applies a destination-based segmentation strategy to capture real-world communication structures in IoT traffic.
- Evaluated across 6 distinct IoT datasets and 44 transfer scenarios, demonstrating strong zero-shot generalization and competitive performance against baseline methods.

## Limitations

Evaluated primarily under zero-shot transfer scenarios in privacy-constrained IoT conditions; performance bounds under extremely noisy or dynamically evolving attack vectors remain to be explored.

## Open Questions & Future Work

- [[uncertainty-aware-zero-shot-iot-anomaly-detection]]

## Archivist Review

Reviewed the paper on adversarial zero-shot IoT anomaly detection. No concepts met the high bar for permanent standalone vault notes as they combine standard VAE and domain adaptation methods. The single open question was evaluated and rejected to maintain strict scarcity standards.

### Approved Open Questions
- Uncertainty-Aware Zero-Shot IoT Anomaly Detection: Addresses the fundamental reliability bottleneck of zero-shot anomaly detection under severe cross-domain distribution shifts in critical infrastructure.

### Rejected Candidates
- [open_question] Uncertainty-Aware Zero-Shot IoT Anomaly Detection (`uncertainty-aware-zero-shot-iot-anomaly-detection`) - low_impact: The open question is well-formulated and important, but we are keeping our open question selections extremely scarce.

## Links

- [Abstract](https://arxiv.org/abs/2609.03505)
- [PDF](https://arxiv.org/pdf/2609.03505)

