---
# CSL-compatible fields
title: "QUIET: Quantifying Underutilized Influential Edges for Targeted Synchronization"
author:
  - literal: "Sovesh Mohapatra"
  - literal: "Christoffer G. Alexandersen"
  - literal: "Panagiotis Fotiadis"
  - literal: "Max B. Kelz"
  - literal: "John A. Detre"
  - literal: "Fabio Pasqualetti"
  - literal: "Dani S. Bassett"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.11091"

# Custom fields
paper_id: "2606.11091"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "network-control-theory"
  - "neuroscience"
architectures:
  []
datasets:
  - "human-connectome-project"
concept_slugs:
  - "quiet-framework"
dataset_slugs:
  - "human-connectome-project"
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:54:00Z"
created_at: "2026-06-12T08:54:00Z"
---

# QUIET: Quantifying Underutilized Influential Edges for Targeted Synchronization

**Authors**: Sovesh Mohapatra, Christoffer G. Alexandersen, Panagiotis Fotiadis, Max B. Kelz, John A. Detre, Fabio Pasqualetti, Dani S. Bassett
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.11091](https://arxiv.org/abs/2606.11091)

## Summary

The paper introduces QUIET (Quantifying Underutilized Influential Edges for Targeted Synchronization), an edge-centric framework for steering neural dynamics by integrating structural connectivity with functional time-series information. Unlike traditional node-centric models, QUIET targets 'quiet highways'—connections that are structurally potent yet functionally underutilized—to optimize the energy cost of achieving specific synchronization patterns. The authors validate the method against synthetic data and apply it to neural connectivity data, demonstrating its utility in explaining individual cognitive differences and network behavior during anesthesia.

## Key Contributions

- Developed QUIET, an edge-centric control framework that identifies structurally influential but functionally underutilized neural connections for energy-efficient synchronization.
- Demonstrated significant performance gains in synchronization tasks, outperforming random edge selection in 93% of synthetic configurations.
- Validated the framework on Human Connectome Project data, finding that control energy requirements for the salience network correlate with individual fluid intelligence.

## Open Questions & Future Work

- [[non-linear-brain-dynamics-control]]

## Key Concepts

- [[quiet-framework]]: An edge-centric control framework that identifies energy-efficient neural synchronization pathways by integrating structural controllability and functional mutual information.

## Archivist Review

The QUIET framework was approved as it proposes a distinct and reusable edge-centric control methodology for network synchronization, moving beyond traditional node-centric approaches. The Human Connectome Project was approved as a standard benchmark dataset for neural connectivity analysis. The open question regarding non-linear dynamics was retained due to its fundamental challenge to existing linear control theory frameworks in neuroscience. Other candidates were rejected to maintain strict vault selectivity.

### Approved Concepts
- QUIET Framework: It introduces a novel edge-centric approach for neural synchronization control, shifting focus from node-centric methods to structurally influential yet functionally underutilized pathways.

### Approved Open Questions
- Non-linear brain dynamics control: This addresses a fundamental limitation in the applicability of network control theory to the non-linear, multi-state nature of human brain dynamics.

## Datasets

- [[human-connectome-project]]

## Links

- [Abstract](https://arxiv.org/abs/2606.11091)
- [PDF](https://arxiv.org/pdf/2606.11091)

