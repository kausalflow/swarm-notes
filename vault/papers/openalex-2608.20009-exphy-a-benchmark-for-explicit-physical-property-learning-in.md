---
# CSL-compatible fields
title: "ExPhy: A Benchmark for Explicit Physical Property Learning in Multi-Object Trajectory Forecasting"
author:
  - literal: "Rui Wang"
  - literal: "Yeteng Wu"
  - literal: "Xianlin Zhang"
  - literal: "Mengshi Qi"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20009"

# Custom fields
paper_id: "2608.20009"
paper_source: "openalex"
domain: "robotics"
tags:
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:19:35Z"
created_at: "2026-08-23T05:19:35Z"
---

# ExPhy: A Benchmark for Explicit Physical Property Learning in Multi-Object Trajectory Forecasting

**Authors**: Rui Wang, Yeteng Wu, Xianlin Zhang, Mengshi Qi
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20009](https://arxiv.org/abs/2608.20009)

## Summary

ExPhy is a new benchmark for multi-object trajectory forecasting that evaluates models not only on future trajectory prediction but also on explicit recovery of object-level physical properties such as mass, friction, and restitution. The benchmark includes 24,000 simulated physical scenes partitioned into in-distribution and out-of-distribution splits over parameters and initial states. Additionally, the authors introduce PhyODE, a physics-guided model that estimates physical properties from observed trajectories to perform differentiable rollouts, achieving significant error reductions over baselines on long-horizon OOD settings.

## Key Contributions

- Introduces ExPhy, a benchmark containing 24,000 simulated physical scenes with explicit object-level labels for mass, friction, and restitution across ID, OOD-Parameter, and OOD-Initial splits.
- Proposes PhyODE, a physics-guided model featuring an explicit property interface that estimates physical parameters from observed trajectories for differentiable future rollout.
- Demonstrates that PhyODE reduces ADE by 33.1% and FDE by 31.0% on the long-horizon OOD-Initial setting compared to the strongest baseline.
- Reveals through property-level analyses that accurate trajectory forecasting does not necessarily imply accurate recovery of underlying physical properties.

## Limitations

Evaluated primarily on simulated physical scenes; real-world transfer remains to be fully explored beyond zero-shot evaluation on ComPhy.

## Open Questions & Future Work

- [[trajectory-vs-property-accuracy]]

## Archivist Review

Approved the open question regarding the decoupling of trajectory accuracy and physical property recovery as it addresses a fundamental limitation in physics-guided trajectory forecasting. Rejected the benchmark dataset and specific model instantiation in accordance with the scarcity and anti-paper-local policies.

### Approved Open Questions
- Trajectory vs Property Accuracy: Crucial for understanding whether physical reasoning models genuinely learn underlying physics or merely memorize trajectory patterns.

### Rejected Candidates
- [dataset] ExPhy (`exphy`) - paper_local: The ExPhy benchmark is introduced by the paper and is not yet a broad external dataset suitable for vault note inclusion.
- [concept] PhyODE (`phyode`) - subcomponent_of_broader_mechanism: PhyODE is a paper-specific model instance rather than a broadly reusable method or framework concept.

## Links

- [Abstract](https://arxiv.org/abs/2608.20009)
- [PDF](https://arxiv.org/pdf/2608.20009)

