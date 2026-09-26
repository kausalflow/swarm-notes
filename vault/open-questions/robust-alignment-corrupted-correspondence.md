---
created_at: '2026-09-26T09:36:46Z'
source_papers:
- '[[openalex-2609.27473-learning-where-to-look-a-shared-relative-alignment-module-fo]]'
title: Robust Conditioning Under Corrupted Correspondence
---

**Background:** Time-series models using learned relative alignment modules often suffer from performance degradation and prior drift when the underlying correspondence between condition and target sequences is corrupted by artifacts such as motion noise.

**Question / Future Work:** Develop conditioning mechanisms and robustness strategies for alignment modules that can reliably detect and compensate for corrupted correspondences or severe motion artifacts in wrist-worn physiological signals without relying on auxiliary sensor inputs.

**Why It Matters:** Addressing motion-induced corruption is critical for deploying wearable vital-sign reconstruction models reliably in unconstrained, real-world free-living environments.

**Evidence:** In future work, we plan to make the conditioning robust when the correspondence itself is corrupted, for example under motion in wrist-worn PPG.