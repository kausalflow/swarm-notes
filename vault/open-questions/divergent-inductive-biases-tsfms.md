---
created_at: '2026-07-05T07:51:57Z'
source_papers:
- '[[openalex-2607.01918-zeus-towards-tuning-free-foundation-model-for-time-series-an]]'
title: Reconciling Divergent Inductive Biases
---

**Background:** Foundation models are increasingly expected to perform zero-shot inference across diverse time series analysis tasks, yet different tasks like forecasting, imputation, and classification require fundamentally different inductive biases.

**Question / Future Work:** It remains an open challenge to design a unified pretraining framework that can simultaneously optimize for and reconcile these divergent inductive biases (extrapolation, interpolation, and global abstraction) without needing task-specific fine-tuning or specialized modules.

**Why It Matters:** This challenge addresses the core of what makes a model a 'foundation' model; without solving the reconciliation of these biases, models remain specialized or require costly adaptation.

**Evidence:** Although recent works attempt a unified modeling paradigm, they often neglect the fundamentally different inductive biases required by each objective: forecasting relies on extrapolation, imputation and anomaly detection necessitate interpolation, and classification requires global abstraction.