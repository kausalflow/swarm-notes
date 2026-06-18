---
created_at: '2026-06-18T09:08:11Z'
source_papers:
- '[[openalex-2606.16486-can-optimal-dispatch-models-recreate-reality-a-retrospective]]'
title: Optimizing storage under rolling horizons
---

**Background:** Optimal dispatch models typically use a cyclic constraint to ensure electricity system storage (e.g., hydropower reservoirs) returns to initial states at the end of an optimization window. This constraint can lead to unrealistic dispatch behavior when optimization horizons are shortened or during extreme system stress.

**Question / Future Work:** Future work should investigate alternative strategies for managing storage in limited-foresight dispatch models, such as using marginal storage values (shadow prices of water) to represent the opportunity cost of stored energy, rather than relying on strict cyclic state-of-charge constraints. This is critical for improving the accuracy of seasonal storage modeling in rolling-horizon frameworks during periods of market stress.

**Why It Matters:** The cyclic constraint is a fundamental limitation in rolling-horizon dispatch models used to simulate real-world system behavior under uncertainty, making it a key bottleneck for long-term dispatch modeling accuracy.