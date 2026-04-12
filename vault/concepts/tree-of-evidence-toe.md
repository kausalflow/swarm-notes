---
title: "Tree-of-Evidence (ToE)"
slug: "tree-of-evidence-toe"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2604.07692-tree-of-evidence-efficient-system-2-search-for-faithful-mult]]"
processed_at: "2026-04-12T06:20:58Z"
created_at: "2026-04-12T06:20:58Z"
---

# Tree-of-Evidence (ToE)

> *Auto-generated stub. Edit this file to add more details.*

An inference-time search algorithm that identifies minimal, discrete evidence sets from heterogeneous data streams to explain LMM predictions.


## Why It Matters

It frames interpretability as a discrete optimization search problem rather than relying on standard soft attention-based saliency methods, providing a more faithful audit of LMM decision-making.

## Evidence

> ToE employs lightweight Evidence Bottlenecks that score coarse groups or units of data... and performs a beam search to identify the compact evidence set required to reproduce the model's prediction.

## Related Papers

- [[openalex-2604.07692-tree-of-evidence-efficient-system-2-search-for-faithful-mult]]
