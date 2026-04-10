---
created_at: '2026-04-10T06:27:12Z'
source_papers:
- '[[openalex-2604.05709-network-reconstruction-in-consensus-algorithms-with-hidden-a]]'
title: Asymmetric Leader-Follower Network Reconstruction
---

**Background:** Reconstructing full network dynamics from partial time-series measurements in leader-follower consensus systems often relies on assuming symmetric coupling between leaders and followers. Relaxing this assumption introduces mathematical degeneracies that current reconstruction methods cannot uniquely resolve.

**Question / Future Work:** The current autoregressive expansion method relies on the assumption that leaders are symmetrically coupled to followers to identify network parameters. Future work is required to develop techniques capable of reconstructing the full dynamical matrix when this symmetry assumption is violated, addressing the non-uniqueness of the resulting matrix inversion.

**Why It Matters:** Generalizing the reconstruction to non-symmetric couplings is critical for the applicability of these inference methods to real-world networks where leader-follower relationships are inherently directed and asymmetric.