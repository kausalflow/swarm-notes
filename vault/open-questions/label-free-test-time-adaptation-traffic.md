---
created_at: '2026-07-31T07:44:18Z'
source_papers:
- '[[openalex-2607.25875-a2tta-anchored-and-agile-test-time-adaptation-for-evolving-t]]'
title: Fully Label-Free Test-Time Adaptation
---

**Background:** Traffic forecasting models deployed in real-world intelligent transportation systems face continuous distribution shifts caused by ongoing road network construction, evolving human mobility patterns, and sensor network expansion.

**Question / Future Work:** Investigate how to develop test-time adaptation and forecasting methods that can function completely label-free or under extreme label scarcity during deployment, as current approaches rely on observing labels after a forecasting delay and require a warm-up phase on a labeled training partition.

**Why It Matters:** Real-world deployment environments often lack ground truth labels immediately or entirely, making label-efficient or label-free test-time adaptation critically important for practical smart city infrastructure.

**Evidence:** A2TTA assumes that labels eventually arrive and uses a labeled training partition to warm up the calibrator for each yearly snapshot. The main setting therefore does not cover fully label-free deployment.