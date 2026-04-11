---
created_at: '2026-04-11T05:55:25Z'
source_papers:
- '[[openalex-2604.07027-learning-to-query-history-nonstationary-classification-via-l]]'
title: Training stability in discrete retrieval
---

**Background:** Training retrieval-augmented systems with discrete components often requires stochastic gradient estimators that exhibit high variance, potentially leading to instability during the joint optimization of the retriever and the downstream classifier.

**Question / Future Work:** Further research is required to stabilize the joint training of retrieval mechanisms and classifiers, specifically investigating variance-reduction techniques, regularization, and alternative gradient estimators to mitigate cold-start issues and training sensitivity.

**Why It Matters:** Understanding how to stabilize these joint training dynamics is essential for the effective scaling of retrieval-augmented systems.

**Evidence:** Our system requires careful tuning to manage the high variance of the score-based gradient estimator and to prevent the classifier from ignoring historical context early in training.