---
created_at: '2026-06-20T08:18:39Z'
source_papers:
- '[[openalex-2606.18812-reinforcement-learning-foundation-models-should-already-be-a]]'
title: Continuous State Action Spaces in RL
---

**Background:** Reinforcement learning agents often operate in large discrete or continuous state and action spaces, which present significant challenges for tabular-based sufficient statistics.

**Question / Future Work:** Extending tabular sufficient statistic models to continuous domains requires moving beyond masked softmax policies to continuous action parametrizations and handling high-dimensional feature-indexed transitions.

**Why It Matters:** Continuous control is necessary for applying these models to real-world tasks such as robotics, making this an essential unresolved problem for general-purpose RL foundation models.