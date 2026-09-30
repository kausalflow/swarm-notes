---
created_at: '2026-09-30T10:50:06Z'
source_papers:
- '[[openalex-2609.34409-mascit-a-mask-aware-state-space-classifier-for-naturally-irr]]'
title: Test-Independent Selection for SSMs
---

**Background:** State space models utilizing selectivity mechanisms depend on hyperparameter configuration choices, such as input-dependent discretization and parameter matrices, which often require extensive search or oracle tuning.

**Question / Future Work:** Developing test-independent selection rules and automated configuration strategies for partially selective state space models remains an open challenge, as current performance relies heavily on oracle selection over multiple pattern configurations.

**Why It Matters:** Important for deploying selective state space models in real-world scenarios without incurring heavy validation overhead or overfitting to specific test sets.

**Evidence:** Nevertheless, the dataset-wise same-test oracle over eight patterns makes the aggregate an optimistic upper envelope, motivating a test-independent selection rule.