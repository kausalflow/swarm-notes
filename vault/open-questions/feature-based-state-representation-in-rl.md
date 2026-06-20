---
created_at: '2026-06-20T08:18:39Z'
source_papers:
- '[[openalex-2606.18812-reinforcement-learning-foundation-models-should-already-be-a]]'
title: Feature-based State Representations in RL
---

**Background:** State representations in reinforcement learning often rely on integer indices which are permutation-equivariant but lack intrinsic geometric meaning, preventing the model from generalizing knowledge across physically similar but distinct states.

**Question / Future Work:** Developing mechanisms to incorporate informative feature vectors for states and actions, rather than relying on raw indices, is required to enable models to leverage spatial or semantic relationships for improved generalization across state spaces.

**Why It Matters:** This is a fundamental bottleneck for scaling foundation models to environments where state-space size and complexity prevent simple enumeration or rely on geometric relationships.

**Evidence:** One extension is to replace the bare index with a feature vector... per state (and per action), which gives the input a notion of distance between states.