---
created_at: '2026-05-23T07:26:28Z'
source_papers:
- '[[openalex-2605.20630-evaluating-temporal-semantic-caching-and-workflow-optimizati]]'
title: Parameter-Aware Caching for Agents
---

**Background:** In agentic plan-execute pipelines, semantic caching often relies on embedding similarity to reuse results across queries, which can lead to incorrect behavior for parameter-sensitive industrial queries where linguistic similarity does not guarantee answer validity.

**Question / Future Work:** Industrial agents often receive queries that share linguistic structures but differ significantly in their operational parameters, such as specific asset IDs, sensor names, or time windows. Current semantic caching methods frequently fail to distinguish these differences, resulting in false-positive cache hits. Developing a parameter-aware caching mechanism that extracts and utilizes structured parameters to ensure that cache lookups respect the underlying operational context remains an unresolved challenge.

**Why It Matters:** This is critical because it addresses a fundamental limitation of semantic caching in agentic systems, where result validity is state-dependent rather than just input-dependent. Solving this would move caching from a best-effort heuristic to a reliable component for safety-critical industrial applications.