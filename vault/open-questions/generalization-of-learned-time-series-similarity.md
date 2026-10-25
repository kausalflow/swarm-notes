---
created_at: '2026-10-25T09:29:11Z'
source_papers:
- '[[openalex-2610.31288-disc-domain-integrated-similarity-cost-for-time-series-datas]]'
title: Generalization of Learned Time-Series Similarity
---

**Background:** Time-series dataset similarity metrics are used to quantify source-target relationships and predict downstream transfer behavior across different models and tasks.

**Question / Future Work:** Investigate whether the performance gains and task-specific metric weightings learned by frameworks like DISC generalize robustly across a much broader and more diverse array of unseen dataset partitions, domains, and foundation model architectures beyond the evaluated split.

**Why It Matters:** Understanding whether learned dataset similarity costs overfit to specific dataset splits is crucial for ensuring reliable transferability estimation in general time-series foundation model pipelines.

**Evidence:** These results are based on one shared train-validation-test split, but the test score is averaged over 14 source-row evaluations and repeated across four downstream settings.