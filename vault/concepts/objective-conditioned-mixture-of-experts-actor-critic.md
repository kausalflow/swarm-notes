---
title: "Objective-Conditioned Mixture-of-Experts Actor-Critic"
slug: "objective-conditioned-mixture-of-experts-actor-critic"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2606.30997-a-three-phase-foundation-model-for-tax-aware-personalized-po]]"
processed_at: "2026-07-03T07:55:42Z"
created_at: "2026-07-03T07:55:42Z"
---

# Objective-Conditioned Mixture-of-Experts Actor-Critic

> *Auto-generated stub. Edit this file to add more details.*

A policy optimization architecture that uses a router to distribute tasks among specialized expert heads based on user objectives and market context.


## Why It Matters

It enables a single RL policy to handle conflicting investment goals by dynamically routing tasks to specialized experts, eliminating gradient conflict.

## Evidence

> Phase 2 fine-tunes a MoE (Mixture of Experts) portfolio actor critic with PPO under an objective-conditioned reward that simultaneously serves six distinct investment goals... a learned intent router blends experts based on the active objective and current market regime.

## Related Papers

- [[openalex-2606.30997-a-three-phase-foundation-model-for-tax-aware-personalized-po]]
