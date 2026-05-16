---
created_at: '2026-05-16T07:09:41Z'
source_papers:
- '[[openalex-2605.13816-uncertainty-driven-anomaly-detection-for-psychotic-relapse-u]]'
title: Early fusion for relapse detection
---

**Background:** Digital phenotyping involves combining diverse data streams such as cardiac, motion, and sleep signals to monitor mental health states. Current approaches often rely on late fusion techniques that combine model outputs at the decision level.

**Question / Future Work:** Investigating early fusion architectures that jointly model cardiac and sleep patterns within a unified neural network to capture cross-modal interactions that might be missed by late-stage integration. This approach aims to determine if shared latent representations better capture the longitudinal dependencies and physiological precursors required for reliable relapse detection.

**Why It Matters:** Early fusion may allow for learning higher-order cross-modal dependencies that are invisible when modalities are processed independently and fused only at the final decision stage.