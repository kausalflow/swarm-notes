---
# CSL-compatible fields
title: "TimeBlocks: Foundational and Continual Time-Series Blockbase -- Extended Version"
author:
  - literal: "David Campos"
  - literal: "Bin Yang"
  - literal: "Tung Kieu"
  - literal: "Lei Chen"
  - literal: "Chenjuan Guo"
  - literal: "Christian S. Jensen"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.02142"

# Custom fields
paper_id: "2606.02142"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "continual-learning"
  - "efficient-transformer"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "timeblocks"
  - "streamcore"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:42:57Z"
created_at: "2026-06-04T08:42:57Z"
---

# TimeBlocks: Foundational and Continual Time-Series Blockbase -- Extended Version

**Authors**: David Campos, Bin Yang, Tung Kieu, Lei Chen, Chenjuan Guo, Christian S. Jensen
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.02142](https://arxiv.org/abs/2606.02142)

## Summary

TimeBlocks is a modular, lightweight framework designed to enable foundational-like capabilities in time-series processing while remaining suitable for real-time stream applications. The system employs a routing strategy to dynamically assemble task-specific models from a pool of interchangeable building blocks. To handle non-stationary data streams, it integrates StreamCore, a method that preserves guaranteed stream approximations for efficient, continual model calibration. This approach provides a lightweight alternative to large-scale foundational models, enhancing deployability in resource-constrained environments.

## Key Contributions

- Introduces TimeBlocks, a modular architecture that constructs task-specific, lightweight models from a pre-defined pool of interchangeable blocks.
- Implements StreamCore, an approximation method that facilitates continual model calibration by maintaining representative subsets of non-stationary time-series streams.
- Demonstrates superior performance across multiple time-series tasks and datasets compared to existing monolithic foundational models.

## Key Concepts

- [[timeblocks]]: A modular framework for constructing lightweight time-series models by routing interchangeable blocks from a shared pool.
- [[streamcore]]: A data streaming method that maintains a representative subset of a stream for efficient, continual model calibration.

## Archivist Review

I have approved the core modular framework (TimeBlocks) and its accompanying stream-based calibration mechanism (StreamCore) because both represent distinct, reusable methodological contributions to lightweight time-series forecasting. I have not included any datasets or open questions, as none met the strict criteria for novelty and long-term research relevance. The framework is evaluated as a significant shift toward modular, real-time-capable time-series models.

### Approved Concepts
- TimeBlocks: Introduces a modular, block-based approach for constructing lightweight, task-specific time-series models from a shared pool.
- StreamCore: Enables efficient continual model calibration by distilling time-series data streams into representative, approximated subsets.

## Links

- [Abstract](https://arxiv.org/abs/2606.02142)
- [PDF](https://arxiv.org/pdf/2606.02142)

