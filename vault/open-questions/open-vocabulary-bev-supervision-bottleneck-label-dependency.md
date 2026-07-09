---
created_at: '2026-07-09T08:19:25Z'
source_papers:
- '[[openalex-2607.04812-tgrip-a-text-guided-approach-to-vehicle-instance-prediction]]'
title: Open-Vocabulary BEV Supervision Bottleneck
---

**Background:** Bird’s-Eye View (BEV) instance prediction relies on geometric ground truth (occupancy, optical flow) which often lacks the explicit semantic awareness needed for navigating complex, high-ambiguity scenarios. Integrating open-vocabulary semantic priors from Vision-Language Models into temporal BEV representations remains a fundamental challenge for robust, end-to-end motion prediction.

**Question / Future Work:** The development of open-vocabulary supervision strategies that bypass the need for explicit 3D bounding box annotations for semantic map generation is required. Exploring ways to derive semantic embeddings directly from raw, unannotated image regions rather than pre-labeling will enhance the ability to scale to long-tail scenarios.

**Why It Matters:** Removing dependency on manually labeled 3D boxes is essential for scaling autonomous driving perception to long-tail, real-world scenarios where unanticipated objects or rare categories frequently occur.