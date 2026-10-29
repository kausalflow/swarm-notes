---
# CSL-compatible fields
title: "Thermal-Headroom Routing for Efficient Robot Perception in Extreme Heat"
author:
  - literal: "Sparsh Roy"
  - literal: "Kevin Zhou"
  - literal: "Arhaan Shah"
  - literal: "Shreyan Garg"
  - literal: "Vihaan Joshi-Apte"
  - literal: "Maxim Kudryashov"
  - literal: "Nanda Cheruvanthala"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35231"

# Custom fields
paper_id: "2610.35231"
paper_source: "openalex"
domain: "robotics"
tags:
  - "autonomous-agent"
  - "agent"
  - "efficiency"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:11:32Z"
created_at: "2026-10-29T11:11:32Z"
---

# Thermal-Headroom Routing for Efficient Robot Perception in Extreme Heat

**Authors**: Sparsh Roy, Kevin Zhou, Arhaan Shah, Shreyan Garg, Vihaan Joshi-Apte, Maxim Kudryashov, Nanda Cheruvanthala
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35231](https://arxiv.org/abs/2610.35231)

## Summary

Adaptive robot perception systems must manage trade-offs between accuracy, latency, and energy consumption, especially in extreme heat environments where processors thermally throttle. To address this, the authors propose Thermal-Headroom Routing (THR), a lightweight model-selection policy that utilizes a closed-form RC thermal model to forecast processor temperatures and filter out detector configurations likely to cross throttling thresholds. Extensive evaluations across multiple YOLO11 configurations and real-world perception traces show that THR effectively eliminates throttling, reduces deadline misses, and improves energy efficiency under severe ambient conditions.

## Key Contributions

- Proposes Thermal-Headroom Routing (THR), a lightweight model-selection policy that forecasts processor temperature using a closed-form RC thermal model to prevent thermal throttling in robot perception systems.
- Demonstrates that THR eliminates thermal throttling in simulation under extreme ambient temperatures (45-55C) and tight inference deadlines.
- Achieves 3.9-7.5 percentage point reductions in deadline misses and a 12-13% reduction in energy per on-time frame compared to latency-belief routers across seven perception traces and eight ambient temperatures.

## Limitations

Measurements on an Apple M5 support the single-node heating approximation but do not validate hardware throttling.

## Archivist Review

The paper presents Thermal-Headroom Routing (THR) for robot perception under extreme heat, utilizing a closed-form RC thermal model. However, since the work is highly application-specific to robotics and edge thermal management rather than general time-series forecasting or core machine learning methodology, no concepts or open questions met the stringent inclusion criteria for the vault.

### Rejected Candidates
- [open_question] Online-Learned Duty Budgets for Thermal Routing (`online-learned-duty-budgets-for-thermal-routing-in-edge-robotics`) - low_impact: The question focuses on a hardware-specific robotics application (thermal throttling on edge boards) rather than a reusable time-series forecasting or core ML bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.35231)
- [PDF](https://arxiv.org/pdf/2610.35231)

