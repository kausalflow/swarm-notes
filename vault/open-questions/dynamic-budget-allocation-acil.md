---
created_at: '2026-07-23T07:26:39Z'
source_papers:
- '[[openalex-2607.17632-typicore-a-hybrid-active-query-strategy-for-class-incrementa]]'
title: Dynamic Budget Allocation in ACIL
---

**Background:** Active Class-Incremental Learning (ACIL) applies active learning strategies to select informative samples for sequential model updating under labeling budgets, but existing approaches typically assume uniform budget distributions across tasks.

**Question / Future Work:** Investigate dynamic budget allocation strategies that allocate more labeling resources to tasks experiencing high distribution shifts relative to prior knowledge, avoiding uniform budget allocation across tasks.

**Why It Matters:** Dynamic budget allocation can optimize label efficiency and model adaptation in non-stationary environments where task complexity and distribution shifts vary unpredictably.

**Evidence:** rather than distributing the annotation budget uniformly across tasks, methods could estimate the degree of distribution shift between incoming and previously seen data, and allocate more labeling resources to tasks that deviate most significantly from prior knowledge