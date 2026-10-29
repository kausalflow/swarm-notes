---
# CSL-compatible fields
title: "AgenticCity-Bench: Longitudinal Multimodal Observations of Urban Dynamics with Agentic Reasoning"
author:
  - literal: "Xiaofei Yu"
  - literal: "Kailai Sun"
  - literal: "Yanyu Mao"
  - literal: "Baoshen Guo"
  - literal: "Heye Huang"
  - literal: "Yongcai WANG"
  - literal: "Baotong Mi"
  - literal: "Alok Prakash"
  - literal: "Shenhao Wang"
  - literal: "Jinhua Zhao"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35293"

# Custom fields
paper_id: "2610.35293"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "agent"
  - "autonomous-agent"
  - "planning"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "agenticcity-bench"
concept_slugs:
  []
dataset_slugs:
  - "agenticcity-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:11:48Z"
created_at: "2026-10-29T11:11:48Z"
---

# AgenticCity-Bench: Longitudinal Multimodal Observations of Urban Dynamics with Agentic Reasoning

**Authors**: Xiaofei Yu, Kailai Sun, Yanyu Mao, Baoshen Guo, Heye Huang, Yongcai WANG, Baotong Mi, Alok Prakash, Shenhao Wang, Jinhua Zhao
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35293](https://arxiv.org/abs/2610.35293)

## Summary

This paper introduces AgenticCity-Bench, a longitudinal multimodal benchmark spanning 16 cities globally from 2000 to 2025 across 18 modalities of urban function, activity, and environmental state. The benchmark unifies heterogeneous data sources around a common spatial reference and calendar index to enable joint modeling of urban dynamics. Furthermore, it supports diverse agentic tasks including cross-modal translation, forecasting, planning, and resource analysis.

## Key Contributions

- Introduces AgenticCity-Bench, a longitudinal multimodal benchmark covering 16 cities across 12 countries from 2000 to 2025 with 18 urban function, activity, and environmental modalities.
- Organizes heterogeneous data sources around a common spatial reference and calendar index while preserving tile-level provenance and availability.
- Supports urban cross-modal translation, forecasting, planning, and resource analysis tasks through agentic city reasoning frameworks.

## Open Questions & Future Work

- [[bridging-understanding-action-gap-urban-agents]]

## Archivist Review

The paper introduces AgenticCity-Bench, a longitudinal multimodal benchmark for urban dynamics and agentic reasoning. We approve AgenticCity-Bench as a dataset and retain the open question regarding the perception-action gap in urban agent architectures, while rejecting the benchmark concept as a duplicate of the dataset entry.

### Approved Open Questions
- Bridging Understanding-Action Gap in Urban Agents: This is a core foundational limitation in current urban AI agents, directly dictating whether multimodal urban datasets can be successfully operationalized for real-world policymaking and scientific planning.

### Rejected Candidates
- [concept] AgenticCity-Bench (`agenticcity-bench`) - not_reusable: This candidate is fundamentally a dataset benchmark rather than a reusable algorithmic mechanism or theoretical concept, and is correctly captured under approved datasets.

## Datasets

- [[agenticcity-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2610.35293)
- [PDF](https://arxiv.org/pdf/2610.35293)

