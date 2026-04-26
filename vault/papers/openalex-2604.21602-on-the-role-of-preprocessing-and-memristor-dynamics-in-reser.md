---
# CSL-compatible fields
title: "On the Role of Preprocessing and Memristor Dynamics in Reservoir Computing for Image Classification"
author:
  - literal: "Rishona Daniels"
  - literal: "Duna Wattad"
  - literal: "Ronny Ronen"
  - literal: "David A. Saad"
  - literal: "Shahar Kvatinsky"
issued:
  date-parts:
    - [2026, 4, 23]
url: "https://arxiv.org/abs/2604.21602"

# Custom fields
paper_id: "2604.21602"
paper_source: "openalex"
domain: "speech"
tags:
  - "recurrent-neural-network"
  - "image-classification"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "parallel-delayed-feedback-network"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-26T06:55:12Z"
created_at: "2026-04-26T06:55:12Z"
---

# On the Role of Preprocessing and Memristor Dynamics in Reservoir Computing for Image Classification

**Authors**: Rishona Daniels, Duna Wattad, Ronny Ronen, David A. Saad, Shahar Kvatinsky
**Date**: 2026-04-23
**Paper ID**: [openalex:2604.21602](https://arxiv.org/abs/2604.21602)

## Summary

This paper investigates the performance of parallel delayed feedback networks (PDFN) implemented with volatile memristors for image classification. It provides a systematic analysis of how hardware-level characteristics like device decay rates and variability influence the spatiotemporal processing capability of the reservoir. The authors also propose optimized preprocessing techniques to improve data representation, demonstrating high-performance, robust classification on the MNIST dataset even under significant hardware noise.

## Key Contributions

- Analyzes the impact of volatile memristor characteristics—decay rate, quantization, and variability—on the performance of reservoir computing systems.
- Introduces strategies for data preprocessing to enhance input representation within memristive reservoirs.
- Achieves 95.89% classification accuracy on MNIST using a parallel delayed feedback network, maintaining 94.2% accuracy under 20% device variability.

## Open Questions & Future Work

- [[systematic-preprocessing-design-methodology]]
- [[robustness-to-memristor-variability]]

## Key Concepts

- [[parallel-delayed-feedback-network]]: A reservoir computing architecture that utilizes parallel delayed feedback loops to leverage the intrinsic dynamics of physical memristive devices.

## Archivist Review

Approved the Parallel Delayed Feedback Network as it represents a core structural architectural contribution to physical reservoir computing. The open questions regarding preprocessing methodology and memristor variability are substantial, cross-cutting challenges that move beyond the specifics of this paper toward broader hardware-software co-design goals in neuromorphic systems. MNIST was rejected as it is a common benchmark and not a novel, specialized dataset requiring its own vault entry.

### Approved Concepts
- Parallel Delayed Feedback Network: The PDFN architecture is the fundamental structural framework investigated for mapping temporal dynamics into memristive hardware, providing a clear mechanism for neuromorphic reservoir computing.

### Approved Open Questions
- Systematic Preprocessing Design Methodology: Establishing a formal design framework for input-to-temporal transformation would enable more efficient deployment of physical reservoir computing systems across diverse, non-temporal input tasks.
- Robustness to Memristor Variability: Reliability under hardware noise is the primary barrier to the commercial adoption of memristor-based neuromorphic computing.

## Links

- [Abstract](https://arxiv.org/abs/2604.21602)
- [PDF](https://arxiv.org/pdf/2604.21602)

