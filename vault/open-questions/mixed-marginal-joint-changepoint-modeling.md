---
created_at: '2026-04-25T06:14:55Z'
source_papers:
- '[[openalex-2604.20072-vertex-misalignment-and-changepoint-localization-in-network]]'
title: Modeling mixed changepoint information
---

**Background:** The detectability of changepoints in network time series depends on whether the change resides in the marginal or joint distributions of latent vertex positions. Real-world networks often exhibit complex behavior that does not align perfectly with either edge case.

**Question / Future Work:** Develop latent position process models that capture scenarios where changepoint information is simultaneously present in both marginal and joint distributions, enabling recovery of signals even when vertex correspondence is partially lost or misspecified.

**Why It Matters:** This is critical for bridging the gap between theoretical models and real-world empirical network data where vertex correspondence is rarely known perfectly.

**Evidence:** neither of the current models can reproduce the phenomena observed in the simulated swarm data example in Section 5.4, where the signal is lost after shuffling but is partially recovered after graph matching.