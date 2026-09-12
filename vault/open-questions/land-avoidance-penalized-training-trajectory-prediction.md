---
created_at: '2026-09-12T08:56:00Z'
source_papers:
- '[[openalex-2609.09840-temptpi-informer-based-trajectory-prediction-for-maritime-ve]]'
title: Land Avoidance and Penalized Training
---

**Background:** Maritime vessel trajectory forecasting models frequently encounter edge cases where predicted paths violate physical land boundaries.

**Question / Future Work:** Investigate advanced penalized training methods, loss functions, or specialized land avoidance techniques to prevent deep learning trajectory prediction models from generating physically implausible paths that cross landmasses.

**Why It Matters:** Ensuring that predicted maritime paths respect physical geography is critical for collision avoidance and operational safety, yet standard regression losses often fail to enforce these constraints without destabilizing training.

**Evidence:** The results have partially shown trajectories being predicted to enter land boundaries. In a novel experiment, we introduced a land punishment during training, but found that it destabilized the training and reduced overall performance, thus it was left out of this paper. Future research could investigate options for penalized training or other land avoidance techniques in more detail.