---
created_at: '2026-09-20T09:30:30Z'
source_papers:
- '[[openalex-2609.19760-sabreagent-language-models-at-design-time-for-lost-sales-inv]]'
title: Runtime Versus Design-Time LLM Control
---

**Background:** Integrating language models into real-time decision-making loops such as inventory control can introduce high computational overhead and reasoning instability, motivating design-time alternatives where models propose static artifacts like priors and policy families evaluated via simulation before deployment.

**Question / Future Work:** Investigate the broader applicability and rigorous comparative evaluation of runtime-adjustment controls versus design-time-only language model integration across diverse operational settings, lead-time uncertainty profiles, and model families to better understand when runtime interventions genuinely improve complete analytical controllers.

**Why It Matters:** This open question is technically important because it directly addresses the boundary between offline/design-time LLM reasoning and online/runtime adjustments, providing crucial guidelines for deploying hybrid AI-OR systems in sequential decision-making.

**Evidence:** Matched comparisons across models and larger samples would clarify when these additional runtime adjustments improve the complete policy.