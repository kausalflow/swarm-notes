---
# CSL-compatible fields
title: "FAST: A Holistic Framework for Optimizing Memory-I/O, Computation, and Sampling in Temporal GNN Training"
author:
  - literal: "Yushu Cai"
  - literal: "Qingrui Zhu"
  - literal: "Lei Liu"
  - literal: "Kai Sheng"
  - literal: "Hao Chen"
  - literal: "X He"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.05095"

# Custom fields
paper_id: "2607.05095"
paper_source: "openalex"
domain: "graph-learning"
tags:
  - "graph-neural-network"
  - "gnn"
  - "model-compression"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fast-framework"
  - "slimcache"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:19:19Z"
created_at: "2026-07-09T08:19:19Z"
---

# FAST: A Holistic Framework for Optimizing Memory-I/O, Computation, and Sampling in Temporal GNN Training

**Authors**: Yushu Cai, Qingrui Zhu, Lei Liu, Kai Sheng, Hao Chen, X He
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.05095](https://arxiv.org/abs/2607.05095)

## Summary

FAST is a framework designed to accelerate the end-to-end training of Temporal Graph Neural Networks (TGNNs) by jointly optimizing memory I/O, sparse computation, and temporal sampling. It introduces SlimCache to minimize host-to-device data transfers through compression and caching strategies, while simultaneously enhancing thread efficiency for temporal graph operations and improving CPU cache locality during neighbor sampling. Experiments demonstrate that this holistic approach achieves significant speedups on large-scale dynamic graphs without loss of model accuracy.

## Key Contributions

- Proposes FAST, a holistic framework for TGNN training that addresses I/O, computation, and sampling bottlenecks concurrently.
- Introduces SlimCache for reducing host-device data movement through within-batch compression and cross-batch caching.
- Achieves an average 2.1x speedup on large-scale dynamic graphs compared to state-of-the-art training systems.

## Open Questions & Future Work

- [[dtdg-optimization-bottlenecks-tgnn]]

## Key Concepts

- [[fast-framework]]: A system-level framework for training Temporal Graph Neural Networks that jointly optimizes neighbor sampling, memory I/O, and GPU computation.
- [[slimcache]]: A memory optimization technique for dynamic graph training that uses batch compression and caching to minimize host-to-device data transfers.

## Archivist Review

The approved concepts describe a high-level system-level framework and a specific, reusable memory management mechanism for dynamic graph training. The open question is approved for identifying a substantial, system-level efficiency gap between two major graph paradigms. Other candidates were rejected as they represent implementation-specific sub-components or were not sufficiently distinct.

### Approved Concepts
- FAST Framework: Addresses the training bottleneck in TGNNs through holistic system-level optimization of traditionally decoupled tasks.
- SlimCache: Specifically targets the host-to-device memory bottleneck in memory-constrained dynamic graph training.

### Approved Open Questions
- DTDGs Training Optimization Bottlenecks: DTDGs are a fundamental representation for many time-series and graph tasks; closing the performance gap in training them is essential for broad-spectrum dynamic graph learning.

## Links

- [Abstract](https://arxiv.org/abs/2607.05095)
- [PDF](https://arxiv.org/pdf/2607.05095)

