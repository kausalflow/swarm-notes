---
created_at: '2026-08-13T06:08:57Z'
source_papers:
- '[[openalex-2608.09193-cpda-class-conditional-path-distribution-alignment-for-unsup]]'
title: Class-Conditional Path Alignment on Small Datasets
---

**Background:** Unsupervised time-series domain adaptation relies on aligning source and target distributions, but existing methods predominantly focus on marginal features and vector statistics rather than class-conditional temporal paths.

**Question / Future Work:** Investigate how class-conditional path distribution alignment methods can be effectively scaled and optimized for extremely small datasets, highly imbalanced class distributions, or large class spaces where target pseudo-labels are inherently noisy or unstable.

**Why It Matters:** Understanding the failure modes and failure boundaries of pseudo-label-weighted class-conditional alignments is crucial for extending domain adaptation reliability to small, noisy, or highly complex time-series classification benchmarks.

**Evidence:** In contrast, CPDA is less effective on Finger Movements, Gestures Mid Air, and the OnHW handwriting tasks... This dataset is small and close to chance-level performance for many methods, so target pseudo-labels may be too unreliable for class-conditional alignment.