---
created_at: '2026-09-30T10:50:35Z'
source_papers:
- '[[openalex-2609.35634-dr-net-mamba-selective-state-space-modeling-for-long-range-e]]'
title: Unsupervised ECG Denoising Without Ground Truth
---

**Background:** Electrocardiogram (ECG) denoising requires clean clinical reference data, yet clinical datasets inherently lack true clean ground truth.

**Question / Future Work:** Investigate unsupervised or self-supervised denoising frameworks that eliminate the reliance on clean ground-truth reference signals during training, given that clinical ECG datasets inherently lack clean ground truth and current supervised models risk learning residual artifacts.

**Why It Matters:** Crucial for scaling physiological time-series denoising to real-world clinical datasets where clean signals are fundamentally unobservable.

**Evidence:** A persistent challenge across supervised methods is the scarcity of clean ground truth in clinical datasets, where residual artifacts survive preprocessing and become part of the reconstruction target