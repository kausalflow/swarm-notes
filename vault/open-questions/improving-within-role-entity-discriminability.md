---
created_at: '2026-06-11T09:08:22Z'
source_papers:
- '[[openalex-2606.09327-a-universal-dense-football-event-representation-based-on-tab]]'
title: Improving Within-Role Entity Discriminability
---

**Background:** Dense representations of events are often generated through simple aggregation (e.g., season-level averaging), which may overlook nuanced differences in playing style within specific roles.

**Question / Future Work:** It remains to be determined whether contrastive learning or more granular pretraining objectives can enhance the discriminability of agent-level representations, specifically to improve the ability to distinguish between agents who share the same role.

**Why It Matters:** Improving the granularity of agent style representations is essential for practical analytical and scouting applications, where distinguishing between entities with similar roles is critical.

**Evidence:** the uniformly high cosine similarity scores (many at 1.0) are a direct consequence of season-level average pooling, which compresses within-position variance and yields highly concentrated player-level representations; future work will investigate whether within-position discriminability can be further improved through contrastive or fine-grained pretraining objectives.