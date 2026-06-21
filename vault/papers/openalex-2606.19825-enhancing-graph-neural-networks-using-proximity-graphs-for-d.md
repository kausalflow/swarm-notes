---
# CSL-compatible fields
title: "Enhancing Graph Neural Networks Using Proximity Graphs for Dust Source Emission Forecasting"
author:
  - literal: "Maryam Sanisales"
  - literal: "Zahed Rahmati"
  - literal: "Ali Darvishi Boloorani"
  - literal: "Ali Vefghi"
issued:
  date-parts:
    - [2026, 6, 18]
url: "https://arxiv.org/abs/2606.19825"

# Custom fields
paper_id: "2606.19825"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "gnn"
  - "time-series"
  - "forecasting"
  - "lstm"
architectures:
  - "graph-neural-network"
datasets:
  []
concept_slugs:
  - "proximity-graph-enhanced-gnns"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-21T08:53:49Z"
created_at: "2026-06-21T08:53:49Z"
---

# Enhancing Graph Neural Networks Using Proximity Graphs for Dust Source Emission Forecasting

**Authors**: Maryam Sanisales, Zahed Rahmati, Ali Darvishi Boloorani, Ali Vefghi
**Date**: 2026-06-18
**Paper ID**: [openalex:2606.19825](https://arxiv.org/abs/2606.19825)

## Summary

This paper proposes an approach to enhance dust source emission forecasting by using proximity graphs as the underlying structure for Graph Neural Networks. By employing structures like Delaunay triangulation and k-nearest neighbors to inform message passing, the method more effectively captures complex spatiotemporal dependencies than standard random graph approaches or traditional sequence models like LSTMs. Experimental results confirm that these proximity-enhanced models achieve superior predictive performance in environmental dust emission scenarios.

## Key Contributions

- Proposes the use of various proximity graphs—Delaunay, Gabriel, k-NN, and Yao—as the structural basis for GNN-based message passing.
- Demonstrates that proximity graph-based GNNs outperform random-graph GNNs and traditional LSTM models in dust source emission forecasting tasks.
- Establishes that incorporating geographical proximity into the GNN input structure better captures the spatial-temporal dependencies of environmental dust emission dynamics.

## Open Questions & Future Work

- [[optimal-graph-construction-for-environmental-gnns]]

## Key Concepts

- [[proximity-graph-enhanced-gnns]]: A framework for improving GNN spatiotemporal modeling by utilizing proximity-based graphs instead of random or fixed structures for message passing.

## Archivist Review

The concepts and questions selected are central to the paper's novel approach of using proximity-based graph topologies to structure message passing in GNNs for environmental forecasting. The approval prioritizes the generalizable methodology of graph construction over specific experimental results or datasets. No other candidates were proposed.

### Approved Concepts
- Proximity Graph-Enhanced GNNs: The paper introduces the systematic integration of proximity graphs (Delaunay, Gabriel, k-NN, Yao) as the topological structure for GNN message passing in environmental forecasting.

### Approved Open Questions
- Optimal Graph Construction Methods: The performance of GNNs is highly sensitive to the graph structure. As environmental datasets expand to include more complex variables, understanding how to construct graphs that accurately reflect underlying physical phenomena rather than relying on heuristic proximity measures is critical for improving predictive reliability.

## Links

- [Abstract](https://arxiv.org/abs/2606.19825)
- [PDF](https://arxiv.org/pdf/2606.19825)

