---
source_papers:
- '[[2603.23490-dynamic-light-spanners-in-doubling-metrics]]'
title: Dynamic Light Spanner Runtime
---

**Background:** Research on dynamic spanners in doubling metrics has primarily focused on achieving sparsity (a small number of edges) with polylogarithmic update times. Controlling the lightness (the ratio of the spanner's total weight to the minimum spanning tree's weight) in a fully dynamic setting has remained a significant challenge.

**Question / Future Work:** Is it possible to design a fully dynamic algorithm that maintains a light-weight spanner for a point set undergoing insertions and deletions in a metric space with a constant doubling dimension, such that the update time is bounded by a polylogarithmic function of the aspect ratio ($\Phi$)?