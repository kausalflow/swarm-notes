---
# CSL-compatible fields
title: "SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation"
author:
  - literal: "Masoud Moghani"
  - literal: "Mahdi Azizian"
  - literal: "Animesh Garg"
  - literal: "Yuke Zhu"
  - literal: "Sean Huver"
  - literal: "Ajay Mandlekar"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25725"

# Custom fields
paper_id: "2603.25725"
paper_source: "arxiv"
domain: "robotics"
tags:
  - "dataset"
  - "simulation"
  - "robotics"
  - "object-detection"
architectures:
  []
datasets:
  []
skill: "GeneralMLSkill"
processed_at: "2026-03-27T06:07:10Z"
created_at: "2026-03-27T06:07:10Z"
---

# SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation

**Authors**: Masoud Moghani, Mahdi Azizian, Animesh Garg, Yuke Zhu, Sean Huver, Ajay Mandlekar
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25725](https://arxiv.org/abs/2603.25725)

## Summary

This paper introduces SoftMimicGen, an automated data generation pipeline to address the bottleneck of collecting large-scale real-world data for deformable object manipulation, a domain largely neglected by existing synthetic data methods focused on rigid bodies. The system comprises high-fidelity simulation environments supporting diverse deformable objects and complex manipulation behaviors across four different robot embodiments. The authors demonstrate that policies trained on this synthetic data achieve high performance across the task suite, validating the utility of large-scale, simulated deformable object data generation. This work significantly expands the applicability of the synthetic data paradigm to complex, non-rigid robotic tasks.

## Key Contributions

- Introduction of SoftMimicGen, an automated data generation pipeline to address the scarcity of large-scale datasets for deformable object manipulation.
- Creation of a suite of high-fidelity simulation environments covering diverse deformable objects (stuffed animal, rope, tissue, towel) and manipulation behaviors (threading, whipping, folding).
- Demonstration of data generation across four distinct robot embodiments: single-arm, bimanual, humanoid, and surgical robots.
- Validation of the generated data by training high-performing policies and systematically analyzing the data generation system's efficacy.

## Limitations

The paper focuses on the system design and initial validation; scalability limits under extreme complexity or fidelity tradeoffs are not fully explored.

## Open Questions & Future Work

- [[flexible-task-structures-for-mimicgen]]

## Key Concepts

- [SoftMimicGen Pipeline](../concepts/softmimicgen-pipeline.md): An automated data generation pipeline specifically designed for creating high-fidelity synthetic datasets for deformable object manipulation tasks in robotics.

## Limitations

The paper focuses on the system design and initial validation; scalability limits under extreme complexity or fidelity tradeoffs are not fully explored.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25725)
- [PDF](https://arxiv.org/pdf/2603.25725)

