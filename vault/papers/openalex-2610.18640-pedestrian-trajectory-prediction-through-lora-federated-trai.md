---
# CSL-compatible fields
title: "Pedestrian Trajectory Prediction through LoRA Federated Training"
author:
  - literal: "Simone Travagliati"
  - literal: "Maria Luisa Merani"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.18640"

# Custom fields
paper_id: "2610.18640"
paper_source: "openalex"
domain: "robotics"
tags:
  - "federated-learning"
  - "lora"
  - "parameter-efficient-fine-tuning"
  - "autonomous-agent"
  - "distributed-training"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:25:11Z"
created_at: "2026-10-16T09:25:11Z"
---

# Pedestrian Trajectory Prediction through LoRA Federated Training

**Authors**: Simone Travagliati, Maria Luisa Merani
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.18640](https://arxiv.org/abs/2610.18640)

## Summary

This paper proposes a distributed architecture for pedestrian trajectory forecasting in Intelligent Transport Systems, leveraging cellular-connected vehicles and an edge server to perform federated fine-tuning of foundation models. To address high communication costs, the authors combine Low-Rank Adaptation (LoRA) with increased local training epochs per communication round, significantly reducing radio resource usage. A novel figure of merit is also introduced to quantify Vehicle-to-Infrastructure communication overhead. Results show high prediction accuracy alongside substantial reductions in communication expenses compared to standard federated methods.

## Key Contributions

- Proposes a distributed architecture combining cellular infrastructure-connected vehicles and an edge server for federated fine-tuning of foundation models for pedestrian trajectory forecasting.
- Applies Low-Rank Adaptation (LoRA) and increased local training rounds per communication round to significantly reduce radio resource utilization and communication overhead.
- Introduces a novel figure of merit to quantify the consumption of radio resources dedicated to Vehicle-to-Infrastructure communications in federated training.
- Demonstrates excellent prediction accuracy while drastically lowering communication costs compared to baseline federated training methods in vehicular environments.

## Archivist Review

No novel standalone concepts or critical datasets warranting standalone wiki pages were identified beyond established techniques like LoRA and federated learning.

## Links

- [Abstract](https://arxiv.org/abs/2610.18640)
- [PDF](https://arxiv.org/pdf/2610.18640)

