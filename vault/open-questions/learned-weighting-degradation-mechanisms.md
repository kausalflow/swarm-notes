---
created_at: '2026-10-04T10:49:22Z'
source_papers:
- '[[openalex-2610.01831-pooling-helps-learned-weighting-hurts-in-context-decomposing]]'
title: Mechanisms of Learned Weighting Degradation
---

**Background:** Group attention mechanisms in time series models combine a pooling pathway with a learned weighting pathway, but the exact reasons why learned weighting degrades in-context learning remain uncharacterized.

**Question / Future Work:** Investigate the underlying mechanisms and representations responsible for the degradation caused by learned Q/K weighting during in-context learning in group attention architectures. This includes studying whether phenomena like rank collapse or specific features of the learned weighting responses across depth explain the observed performance drop.

**Why It Matters:** Understanding why learned weighting degrades in-context group attention is crucial for designing robust time series foundation models that can handle both multivariate and in-context forecasting without manual intervention.

**Evidence:** Why the tidal networks are an exception where learned weighting pays, and why depth is what makes it costly, we cannot say. Both are questions about what the learned weighting responds to, which these edits cannot answer: they localize an effect to a pathway and a block without showing what that block computes. Depth-dependent accounts such as rank collapse are candidates they cannot adjudicate, and we leave them to future work.