---
created_at: '2026-10-18T09:13:00Z'
source_papers:
- '[[openalex-2610.22215-futurelift-lifting-trajectory-proposals-into-bidirectional-f]]'
title: Future-Graph Lifting for Planning
---

**Background:** Motion forecasting refiners typically rely on forward-only causal sweeps or compressed trajectory embeddings that limit temporal context propagation.

**Question / Future Work:** Investigate how future-graph lifting and bidirectional temporal reasoning can be extended to handle less structured scene contexts, dynamic map-light environments, and downstream closed-loop planning tasks.

**Why It Matters:** Extending motion forecasting refiners to closed-loop planning and unstructured environments addresses the current limitation of open-loop metrics and static HD maps.

**Evidence:** Future work should extend future-graph lifting to less structured scene context and evaluate whether the refined forecasts translate into safer planning decisions under closed-loop interaction.