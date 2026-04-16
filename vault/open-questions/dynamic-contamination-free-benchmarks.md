---
created_at: '2026-04-16T06:28:04Z'
source_papers:
- '[[openalex-2604.11529-tempusbench-an-evaluation-framework-for-time-series-forecast]]'
title: Dynamic Contamination-Free Benchmarks
---

**Background:** Time-series forecasting evaluation currently suffers from contamination, where test datasets are included in the pre-training corpora of foundation models, leading to inflated performance metrics. Additionally, existing benchmarks often rely on static datasets rather than evolving to reflect real-world data dynamics.

**Question / Future Work:** The development of dynamic, contamination-free benchmarks is a critical future direction, involving creating synthetic data generators or real-world pipelines that continuously refresh to prevent data memorization.

**Why It Matters:** Without contamination-free and dynamic evaluation sets, it is impossible to distinguish genuine methodological progress from memorization, which is the primary bottleneck for advancing time-series foundation models.

**Evidence:** We expect the datasets used to define our benchmarks will eventually be included in the pretaining corpora of TSFMs, as has been the case with many NLP benchmarks. To this end, we are developing dynamic benchmarks where test data is continuously refreshed.