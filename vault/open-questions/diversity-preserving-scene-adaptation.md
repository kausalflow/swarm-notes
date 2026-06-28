---
created_at: '2026-06-28T08:16:48Z'
source_papers:
- '[[openalex-2606.26661-lamp-lane-aligned-motion-primitives-for-feasible-trajectory]]'
title: Diversity-Preserving Scene Adaptation
---

**Background:** Motion forecasting models often encounter a trade-off between generating diverse, multimodal predictions and ensuring that all individual hypotheses remain feasible according to lane topology and traffic rules.

**Question / Future Work:** Future work is required to develop scene-adaptive decoding mechanisms that improve the structural feasibility of multimodal trajectory predictions without compromising their behavioral diversity. Investigating methods to maintain high-diversity coverage while strictly enforcing topological constraints remains an open challenge for motion forecasting systems.

**Why It Matters:** Achieving both diversity and feasibility is critical for autonomous driving; systems that either produce infeasible trajectories or lack the necessary behavioral variety fail to support safe, robust downstream planning.

**Evidence:** Due to this feasibility–diversity trade-off, we exclude LoRA from the final LAMP model, leaving diversity-preserving scene adaptation as future work.