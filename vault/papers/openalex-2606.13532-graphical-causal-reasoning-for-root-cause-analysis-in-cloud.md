---
# CSL-compatible fields
title: "Graphical Causal Reasoning for Root Cause Analysis in Cloud Networks"
author:
  - literal: "Fabien Chraim"
  - literal: "Dominik Janzing"
  - literal: "John Evans"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13532"

# Custom fields
paper_id: "2606.13532"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "anomaly-detection"
  - "causal-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  - "automation-ontology-for-root-cause-analysis"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:39:10Z"
created_at: "2026-06-14T08:39:10Z"
---

# Graphical Causal Reasoning for Root Cause Analysis in Cloud Networks

**Authors**: Fabien Chraim, Dominik Janzing, John Evans
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13532](https://arxiv.org/abs/2606.13532)

## Summary

This paper presents a causal graph-based approach to root cause analysis (RCA) in complex cloud networks. By employing a spatiotemporal grouping strategy and an automation ontology, the method effectively reduces the dimensionality of incident data. The system constructs causal graphs from binary time series using Granger causality and conditional independence tests, enabling interpretable root cause scoring through edge-specific probabilistic traversal. Evaluation on production incidents and real-world deployment demonstrates high accuracy and practicality for network operations.

## Key Contributions

- Introduces a novel RCA framework for cloud networks using graph-based causal discovery combined with a spatiotemporal grouping strategy and an automation ontology.
- Constructs causal graphs from binary time series data using bivariate Granger causality and conditional independence tests for interpretable dependency modeling.
- Demonstrates 85.7% root cause recall on a set of 35 labeled production incidents and successful deployment in over 800 real-world incidents.

## Open Questions & Future Work

- [[spatial-representation-granularity-in-rca]]

## Key Concepts

- [[automation-ontology-for-root-cause-analysis]]: A structural knowledge framework that organizes incident data to reduce dimensionality in cloud network root cause analysis.

## Archivist Review

The paper offers a practical framework for cloud network RCA. I approved the 'automation ontology' concept as a specialized, reusable approach to dimensionality reduction in monitoring systems, and the open question regarding spatial representation because it addresses a fundamental trade-off between complexity reduction and fault localization precision in graph-based RCA. Other candidates were rejected to maintain the vault's focus on high-impact, reusable mechanisms.

### Approved Concepts
- Automation Ontology for Root Cause Analysis: This concept addresses the critical challenge of high-dimensional data in root cause analysis for distributed systems by leveraging structured knowledge for dimensionality reduction.

### Approved Open Questions
- Spatial Representation Granularity: This addresses a fundamental limitation where excessive compression leads to the misclassification of faults in geographically or topologically proximate network locations.

### Rejected Candidates
- [concept] Automation Ontology (`automation-ontology`) - other: Renamed to 'automation-ontology-for-root-cause-analysis' to reflect its specific operational domain and intended purpose.
- [open_question] Refining Spatial Representation for RCA (`refining-spatial-representation-for-rca`) - other: Renamed to 'spatial-representation-granularity-in-rca' to better reflect the core research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2606.13532)
- [PDF](https://arxiv.org/pdf/2606.13532)

