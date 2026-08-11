---
created_at: '2026-08-11T05:45:53Z'
source_papers:
- '[[openalex-2509.05663-dqs-a-low-budget-query-strategy-for-enhancing-unsupervised-d]]'
title: Robust Active Learning under Mislabelling
---

**Background:** Active learning strategies for time series anomaly detection frequently assume that oracle labels are entirely error-free, ignoring realistic conditions where domain experts may experience fatigue or provide incorrect annotations.

**Question / Future Work:** Develop query strategies and evaluation methodologies for time series anomaly detection that maintain high performance under realistic conditions of human oracle mislabelling, as current approaches exclusively assume ideal, error-free labels.

**Why It Matters:** Addressing mislabelling robustness bridges the gap between simulated active learning benchmarks and noisy real-world industrial deployments.

**Evidence:** Additionally, literature in the field of active learning in time series anomaly detection has always assumed a perfect oracle, i.e. all labels provided are correct... Therefore, this work investigates the impact of different rates of mislabelling on the anomaly detection performance, which has not been undertaken previously in the literature.