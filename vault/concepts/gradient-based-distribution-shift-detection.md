---
title: "Gradient-Based Distribution Shift Detection"
slug: "gradient-based-distribution-shift-detection"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2604.12425-forecasting-the-past-gradient-based-distribution-shift-detec]]"
processed_at: "2026-04-17T06:29:28Z"
created_at: "2026-04-17T06:29:28Z"
---

# Gradient-Based Distribution Shift Detection

> *Auto-generated stub. Edit this file to add more details.*

A method for identifying out-of-distribution trajectories by monitoring the gradient norms of a self-supervised auxiliary forecasting task.


## Why It Matters

Provides a post-hoc, non-intrusive method for detecting distributional shifts in trajectory prediction without modifying the base model.

## Evidence

> The L2 norm of the gradient of this forecasting loss with respect to the decoder's final layer defines a score to identify distribution shifts.

## Related Papers

- [[openalex-2604.12425-forecasting-the-past-gradient-based-distribution-shift-detec]]
