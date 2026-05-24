---
created_at: '2026-05-24T07:46:05Z'
source_papers:
- '[[openalex-2605.22055-prototype-guided-classification-sub-task-decoupling-framewor]]'
title: Adaptive Prototype Allocation Strategies
---

**Background:** Time series classification models often lack automated mechanisms to determine the optimal number of prototypes required to represent the latent feature distribution of different classes.

**Question / Future Work:** The current framework relies on manually specified prototype counts at each granularity level, which may not be optimal for diverse datasets. Future research could explore adaptive prototype allocation strategies that dynamically determine the number of prototypes based on dataset complexity, inter-class variability, and intra-class feature distribution.

**Why It Matters:** This is a fundamental bottleneck in prototype-based models, as hyperparameter sensitivity to the number of prototypes complicates deployment across heterogeneous datasets where the number of required clusters is unknown.

**Evidence:** First, the number of prototypes at each granularity level is manually specified. Although the model shows stable performance across reasonable settings, developing adaptive prototype allocation strategies could further improve flexibility.