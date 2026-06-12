---
created_at: '2026-06-12T08:54:30Z'
source_papers:
- '[[openalex-2606.10656-envision4d-envisioning-visual-futures-via-feed-forward-4d-ga]]'
title: Long-horizon Unseen Hallucination
---

**Background:** Reconstruction-based models for dynamic scene extrapolation often struggle to generate regions that are entirely absent from historical input frames.

**Question / Future Work:** A fundamental limitation in reconstruction-based world models is their difficulty in synthesizing entirely new or unseen content over long horizons, necessitating the integration of strong generative priors for robust extrapolation in dynamic driving environments.

**Why It Matters:** This represents a core barrier to achieving safe and reliable long-term scene prediction in autonomous driving, where new objects or occlusions frequently enter the field of view.

**Evidence:** the model struggles to hallucinate entirely unseen regions, meaning it cannot forecast as far into the future as generative models.