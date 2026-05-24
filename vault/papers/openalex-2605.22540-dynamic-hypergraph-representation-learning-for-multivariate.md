---
# CSL-compatible fields
title: "Dynamic Hypergraph Representation Learning for Multivariate Time Series without Prior Knowledge"
author:
  - literal: "Marco Gregnanin"
  - literal: "Johannes De Smedt"
  - literal: "Giorgio Gnecco"
  - literal: "Maurizio Parton"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22540"

# Custom fields
paper_id: "2605.22540"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dhacn-dynamic-hypergraph-attention-convolution-network"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:45:58Z"
created_at: "2026-05-24T07:45:58Z"
---

# Dynamic Hypergraph Representation Learning for Multivariate Time Series without Prior Knowledge

**Authors**: Marco Gregnanin, Johannes De Smedt, Giorgio Gnecco, Maurizio Parton
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22540](https://arxiv.org/abs/2605.22540)

## Summary

This paper addresses the difficulty of deriving structure from unstructured multivariate time series by proposing a method to construct dynamic hypergraphs without prior knowledge. The approach utilizes an attention-based community detection technique to identify relationships, which are subsequently transformed into hypergraph representations using a clique-based construction. These representations are then processed by a Dynamic Hypergraph Attention Convolution Network (DHACN) to improve forecasting performance by effectively modeling high-order dependencies.

## Key Contributions

- Introduces a fully automated approach for constructing dynamic hypergraph representations from multivariate time series without requiring prior domain knowledge.
- Develops a clique-based hypergraph construction method driven by community detection via an attention mechanism to capture high-order relationships.
- Proposes the Dynamic Hypergraph Attention Convolution Network (DHACN) to leverage constructed hypergraph structures for multivariate time series prediction.

## Open Questions & Future Work

- [[hypergraph-time-series-informativeness]]

## Key Concepts

- [[dhacn-dynamic-hypergraph-attention-convolution-network]]: A deep learning architecture designed to perform multivariate time series predictions using dynamic hypergraph representations derived from community-based attention.

## Archivist Review

The approved concept captures a novel architectural approach to dynamic hypergraph modeling for time series, while the open question addresses the foundational need to quantify the informativeness of high-order structures vs. pairwise ones in multivariate forecasting. Other candidates were deemed either overly specific to this implementation or covered by broader categories already in the vault.

### Approved Concepts
- Dynamic Hypergraph Attention Convolution Network (DHACN): The model serves as the core architecture for processing the constructed dynamic hypergraphs to perform multivariate time series forecasting.

### Approved Open Questions
- Dynamics of Higher-Order Dependencies: Understanding the conditions under which hypergraph-based approaches provide predictive advantages over simpler, graph-based or purely temporal models is essential for broader adoption in time series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2605.22540)
- [PDF](https://arxiv.org/pdf/2605.22540)

