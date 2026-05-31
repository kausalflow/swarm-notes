---
# CSL-compatible fields
title: "Precomputed 1D-CNNs for Atrial Fibrillation Detection on Tiny Smart Sensor Systems"
author:
  - literal: "Lukas Einhaus"
  - literal: "Natalie Maman"
  - literal: "Julian Hoever"
  - literal: "Andreas Erbslöh"
  - literal: "Gregor Schiele"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29994"

# Custom fields
paper_id: "2605.29994"
paper_source: "openalex"
domain: "speech"
tags:
  - "cnn"
  - "model-compression"
  - "time-series"
architectures:
  []
datasets:
  - "mit-bih"
concept_slugs:
  - "lut-based-precomputation"
dataset_slugs:
  - "mit-bih"
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:10:43Z"
created_at: "2026-05-31T08:10:43Z"
---

# Precomputed 1D-CNNs for Atrial Fibrillation Detection on Tiny Smart Sensor Systems

**Authors**: Lukas Einhaus, Natalie Maman, Julian Hoever, Andreas Erbslöh, Gregor Schiele
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29994](https://arxiv.org/abs/2605.29994)

## Summary

This paper presents an optimization technique for deploying 1D-CNNs on resource-constrained FPGAs by generalizing LUT-based precomputation to include various grouped convolution structures. The authors propose a novel convolutional block design and a corresponding hyperparameter search algorithm to maximize efficiency on tiny sensor systems. Experimental results on the MIT-BIH ECG dataset demonstrate high detection accuracy for atrial fibrillation while achieving extremely low hardware utilization without requiring DSPs or BRAM.

## Key Contributions

- Generalizes depthwise-separable convolution LUT-based precomputation to broader grouped convolutional structures for FPGA deployment.
- Introduces a novel convolutional block and an algorithm for hyperparameter optimization targeting constrained FPGA resources.
- Achieves an F1-Score of 95% on atrial fibrillation detection using the MIT-BIH dataset with a hardware footprint of only 2,844 LUTs on an AMD Spartan 7 S15.

## Open Questions & Future Work

- [[generalizability-of-lut-precomputation-to-diverse-datasets]]

## Key Concepts

- [[lut-based-precomputation]]: An FPGA-based optimization technique where neural network layer outputs are precomputed and stored in lookup tables to minimize hardware resource usage.

## Archivist Review

The paper provides a clear contribution regarding LUT-based precomputation for time-series models on edge hardware. I have approved the core concept and a general open question regarding its cross-dataset generalizability, while rejecting the request for synergistic optimization study as it lacks a clear path toward a unified theory or bottleneck identification. I have also added the MIT-BIH dataset as it is a standard medical time-series benchmark.

### Approved Concepts
- LUT-based precomputation: It enables ultra-low latency and resource-efficient implementation of neural networks on FPGAs by eliminating runtime computation.

### Approved Open Questions
- Generalizability of LUT-based Precomputation: This is critical to determine if the proposed grouped convolution method is a universal architectural pattern for tiny sensor systems or specific to ECG-based atrial fibrillation tasks.

### Rejected Candidates
- [open_question] Synergistic Optimization Integration (`synergistic-lut-optimization-integration`) - low_impact: Exploring the integration of multiple existing hardware-aware optimization techniques is too speculative and local to the specific hardware targets chosen by the authors.

## Datasets

- [[mit-bih]]

## Links

- [Abstract](https://arxiv.org/abs/2605.29994)
- [PDF](https://arxiv.org/pdf/2605.29994)

