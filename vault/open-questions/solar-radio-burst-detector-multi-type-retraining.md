---
created_at: '2026-03-29T06:09:07Z'
source_papers:
- '[[openalex-2603.25446-implementation-of-a-near-realtime-recording-and-reporting-sy]]'
title: Expand ML detector to new burst types
---

**Background:** The development of automated solar radio burst detection systems relies on training machine learning models using synthetic data that closely mimics real observations.

**Question / Future Work:** The system was trained exclusively on synthetic type III and type IIIb radio bursts, leading to an intrinsic brightness sensitivity that favors moderate and strong events. Future work should involve building a comprehensive, multi-type labeled dataset, including other significant classes like type II bursts and various noise-storm/background scenarios, and subsequently retraining or fine-tuning the detector on this larger, more representative dataset. This is crucial for a direct comparison between observed- and synthetic-training performance across all event types.

**Why It Matters:** Expanding the event catalog beyond Type III/IIIb bursts to include Type II bursts (signatures of CME-driven shocks) is necessary to make the system operationally useful for comprehensive space-weather monitoring, which relies on multiple burst types.

**Evidence:** Future work will expand the detector beyond the current type III/type IIIb training set. In particular, type II bursts—key signatures of CME-driven shocks—and other burst classes (e.g., type V) are not yet represented in the training data, so the present system should be viewed as optimized for type III-related electron-beam activity. We are building a larger multi-type labeled dataset (including type II, additional burst classes, and noise-storm/background scenarios). Once this labeling effort is completed, we will retrain/fine-tune the detector using these well-observed events to better reflect real burst morphology and to enable a direct comparison between observed- and synthetic-training performance.