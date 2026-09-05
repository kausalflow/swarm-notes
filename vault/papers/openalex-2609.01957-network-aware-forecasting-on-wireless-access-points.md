---
# CSL-compatible fields
title: "Network-Aware Forecasting on Wireless Access Points"
author:
  - literal: "Niloo Bahadori"
  - literal: "Swadhin Pradhan"
  - literal: "Peiman Amini"
issued:
  date-parts:
    - [2026, 9, 2]
url: "https://arxiv.org/abs/2609.01957"

# Custom fields
paper_id: "2609.01957"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "edge-computing"
  - "resource-management"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-05T08:41:57Z"
created_at: "2026-09-05T08:41:57Z"
---

# Network-Aware Forecasting on Wireless Access Points

**Authors**: Niloo Bahadori, Swadhin Pradhan, Peiman Amini
**Date**: 2026-09-02
**Paper ID**: [openalex:2609.01957](https://arxiv.org/abs/2609.01957)

## Summary

This paper investigates the resource contention challenges of deploying predictive machine learning models on enterprise wireless access points (APs) that must simultaneously handle high-load packet processing and wireless services. The authors formalize network-aware deployability through a two-gate process involving target AP execution qualification and profile validation under packet-service constraints. Empirical benchmarks demonstrate that standard edge hardware is an unreliable proxy, as model execution speeds and memory profiles vary drastically on real AP hardware. Furthermore, running forecasting workloads under network saturation introduces severe latency and throughput degradation, highlighting the necessity of network-aware model selection for edge AP deployments.

## Key Contributions

- Demonstrates that standard edge testbeds (like Raspberry Pi 5) fail to reliably capture target AP behavior, with models running 6.1--19.1x slower on actual AP hardware.
- Introduces the concept of network-aware deployability, incorporating model qualification and execution profile validation under packet-service and forecasting constraints.
- Quantifies resource contention trade-offs, showing that serving forecasting workloads under network saturation can significantly increase p99 round-trip time (RTT) and reduce network throughput.

## Archivist Review

Applied strict selectivity: rejected the single candidate open question because it focuses on hardware/software co-location interference on wireless access points rather than a general, enduring forecasting methodology or distribution problem.

### Rejected Candidates
- [open_question] Root-Cause Analysis of AP Inference Interference (`root-cause-analysis-ap-interference`) - paper_local: Too paper-local and specific to wireless access point resource contention rather than a general core time-series forecasting methodology question.

## Links

- [Abstract](https://arxiv.org/abs/2609.01957)
- [PDF](https://arxiv.org/pdf/2609.01957)

