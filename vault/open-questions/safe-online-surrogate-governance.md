---
created_at: '2026-06-05T08:39:31Z'
source_papers:
- '[[openalex-2606.03321-validation-gated-multi-agent-governance-for-online-adaptatio]]'
title: Safe Online Surrogate Governance
---

**Background:** AI surrogates deployed for real-time forecasting in thermal-hydraulic facilities are typically trained and frozen offline, leaving them vulnerable to performance degradation when the facility enters operating regimes not represented in the training data. While continual learning techniques allow for online model adaptation, they introduce risks of overfitting and instability in safety-critical engineering environments.

**Question / Future Work:** There is an unresolved need to balance the stability of deterministic, gate-controlled deployment with the flexibility of agent-guided adaptation to ensure that surrogates remain reliable under shifting operating conditions. Research is required to structure governance layers, evaluate the promotion of model challengers within strict safety bounds, and establish the statistical generalizability of these adaptation frameworks across diverse, unseen transient scenarios.

**Why It Matters:** This represents a foundational bottleneck for the deployment of AI digital twins in high-stakes, safety-critical industrial applications where autonomous model evolution must be auditable and restricted.