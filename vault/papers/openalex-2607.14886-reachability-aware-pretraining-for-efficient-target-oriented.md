---
# CSL-compatible fields
title: "Reachability-Aware Pretraining for Efficient Target-Oriented Path Exploration in Temporal Knowledge Graph Reasoning"
author:
  - literal: "Chien‐Liang Liu"
  - literal: "Tsao-Lun Chen"
issued:
  date-parts:
    - [2026, 7, 16]
url: "https://arxiv.org/abs/2607.14886"

# Custom fields
paper_id: "2607.14886"
paper_source: "openalex"
domain: "nlp"
tags:
  - "reinforcement-learning"
  - "knowledge-graph"
  - "pre-training"
  - "self-supervised-learning"
  - "reasoning"
  - "benchmark"
architectures:
  []
datasets:
  - "icews-dataset-series"
concept_slugs:
  - "reachability-aware-pretraining"
dataset_slugs:
  - "icews-dataset-series"
skill: "TimeSeriesSkill"
processed_at: "2026-07-19T07:24:55Z"
created_at: "2026-07-19T07:24:55Z"
---

# Reachability-Aware Pretraining for Efficient Target-Oriented Path Exploration in Temporal Knowledge Graph Reasoning

**Authors**: Chien‐Liang Liu, Tsao-Lun Chen
**Date**: 2026-07-16
**Paper ID**: [openalex:2607.14886](https://arxiv.org/abs/2607.14886)

## Summary

This paper addresses the challenge of sparse rewards and inefficient exploration in reinforcement learning-based multi-hop reasoning for temporal knowledge graphs. The authors propose RAPTOR, a self-supervised pretraining method that incorporates a reachability-aware inductive bias to estimate the likelihood of reaching target entities. This approach significantly streamlines the search space for RL agents, improving both training efficiency and predictive performance on standard temporal graph benchmarks.

## Key Contributions

- Introduces RAPTOR, a self-supervised pretraining method that reduces exploration inefficiency in RL-based TKG reasoning by estimating action reachability.
- Provides a strong model initialization that improves downstream RL fine-tuning speed and overall performance.
- Demonstrates consistent performance improvements over conventional RL-based baselines on the ICEWS14, ICEWS05-15, and ICEWS18 benchmarks.

## Open Questions & Future Work

- [[scalability-of-reachability-labeling-in-tkg-reasoning]]

## Key Concepts

- [[reachability-aware-pretraining]]: A self-supervised pretraining technique for RL agents that injects a reachability-aware inductive bias to streamline exploration in time-evolving action spaces.

## Archivist Review

I approved Reachability-Aware Pretraining as it represents a novel inductive bias for navigating time-evolving graphs, and I created a generalized dataset entry for the ICEWS series (as the specific ICEWS datasets are well-known variants). I rejected the generalizability open question as it was overly focused on simple model benchmarking, but kept the labeling scalability question as it addresses a fundamental technical bottleneck in dynamic graph learning.

### Approved Concepts
- Reachability-Aware Pretraining: It addresses the efficiency challenges inherent in RL-based multi-hop reasoning by guiding the agent through time-evolving graphs via a learned reachability metric.

### Approved Open Questions
- Scalability of Reachability Labeling: As graphs scale, the preprocessing burden threatens the practical utility of reachability-based training methods, necessitating more efficient labeling alternatives.

### Rejected Candidates
- [open_question] Generalizing Reachability-Aware Pretraining (`generalizability-of-reachability-pretraining`) - not_novel: The question essentially asks for more experiments on different models, which falls under boilerplate future work.

## Datasets

- [[icews-dataset-series]]

## Links

- [Abstract](https://arxiv.org/abs/2607.14886)
- [PDF](https://arxiv.org/pdf/2607.14886)

