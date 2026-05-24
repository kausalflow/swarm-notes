---
title: "Composite Feature Representation for Bias Mitigation"
slug: "composite-feature-representation-bias-mitigation"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2605.22233-a-robust-deep-learning-framework-for-prominence-detection-th]]"
processed_at: "2026-05-24T07:48:14Z"
created_at: "2026-05-24T07:48:14Z"
---

# Composite Feature Representation for Bias Mitigation

> *Auto-generated stub. Edit this file to add more details.*

A preprocessing strategy that constructs multi-channel inputs from derived physical image representations to decouple model performance from instrument-specific colormaps and sensor artifacts.


## Why It Matters

The paper demonstrates that simple object detectors are prone to spurious correlations with raw sensor colormaps; constructing composite channels (full-disk, enhanced, disk-removed) forces the model to learn physically grounded geometric features rather than imaging artifacts.

## Evidence

> We develop a further two models comprising three-channel images constructed through an original dataset preprocessing pipeline... The composite model (i) achieves a mAP@50 of 0.749 and a recall of 78% on the test set, outperforming previous bounding box methods.

## Related Papers

- [[openalex-2605.22233-a-robust-deep-learning-framework-for-prominence-detection-th]]
