---
# CSL-compatible fields
title: "EagleVision: A Multi-Task Benchmark for Cross-Domain Perception in High-Speed Autonomous Racing"
author:
  - literal: "Zakhar Yagudin"
  - literal: "Murad Mebrahtu"
  - literal: "Ren Jin"
  - literal: "Jiaqi Huang"
  - literal: "Yujia Yue"
  - literal: "Dzmitry Tsetserukou"
  - literal: "Jorge Dias"
  - literal: "Majid Khonji"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11400"

# Custom fields
paper_id: "2604.11400"
paper_source: "openalex"
domain: "robotics"
tags:
  - "benchmark"
  - "dataset"
  - "object-detection"
  - "autonomous-agent"
  - "trajectory-prediction"
architectures:
  []
datasets:
  - "Indy Autonomous Challenge dataset"
  - "A2RL Real competition dataset"
concept_slugs:
  []
dataset_slugs:
  - "indy-autonomous-challenge-dataset"
  - "a2rl-real-competition-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:29:37Z"
created_at: "2026-04-16T06:29:37Z"
---

# EagleVision: A Multi-Task Benchmark for Cross-Domain Perception in High-Speed Autonomous Racing

**Authors**: Zakhar Yagudin, Murad Mebrahtu, Ren Jin, Jiaqi Huang, Yujia Yue, Dzmitry Tsetserukou, Jorge Dias, Majid Khonji
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11400](https://arxiv.org/abs/2604.11400)

## Summary

EagleVision addresses the scarcity of high-dynamic perception benchmarks by providing a unified LiDAR-based dataset and evaluation protocol for autonomous racing. The authors synthesize data from the Indy Autonomous Challenge, A2RL competition, and simulations to analyze cross-domain generalization in 3D detection and trajectory prediction. Results show that integrating real racing data into pretraining pipelines significantly enhances model performance compared to simulator-only approaches, providing a rigorous testbed for high-speed perception.

## Key Contributions

- Introduces EagleVision, a LiDAR-based benchmark for 3D detection and trajectory prediction, featuring 28,000+ frames across simulation and real racing environments.
- Establishes a dataset-centric transfer framework for evaluating cross-domain generalization between urban-driving, simulator, and high-speed racing domains.
- Demonstrates that motion-distribution coverage in racing datasets leads to improved trajectory prediction performance (FDE 0.947) compared to in-domain training.

## Open Questions & Future Work

- [[high-speed-racing-perception-generalization]]

## Archivist Review

I have approved two specific racing datasets as they are the core contribution and standardized artifacts of the benchmark. I rejected the concept candidate because it describes a dataset/benchmark resource, not a conceptual methodology. I reformulated the open question to focus on the technical research challenge of perception generalization in extreme dynamics rather than just listing gaps.

### Approved Open Questions
- High-Speed Racing Perception Generalization: Understanding these bottlenecks is critical for advancing full-stack autonomy in extreme high-speed scenarios where conventional perception systems currently fail.

### Rejected Candidates
- [concept] EagleVision Benchmark (`eaglevision-benchmark`) - not_reusable: The benchmark is a specific resource/dataset collection rather than a reusable methodological concept or architectural pattern.

## Datasets

- [[indy-autonomous-challenge-dataset]]
- [[a2rl-real-competition-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2604.11400)
- [PDF](https://arxiv.org/pdf/2604.11400)

