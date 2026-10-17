---
created_at: '2026-10-17T08:55:18Z'
source_papers:
- '[[openalex-2610.20597-co-evolving-acting-and-forecasting-for-language-agents]]'
title: Robust Success-Conditioned Action Forecasting
---

**Background:** Training language agents using reinforcement learning typically relies on sparse terminal rewards, leaving intermediate steps unguided unless expensive or noisy observation/value targets are constructed.

**Question / Future Work:** Developing robust multi-step action forecasting objectives and co-evolution mechanisms for language agents that avoid the distribution skew and over-representation of easy tasks (such as default refusals in customer service domains) observed under success-conditioned imitation.

**Why It Matters:** Addressing failure modes in success-conditioned imitation and action forecasting is crucial for extending language agent RL to domains with frequent trivial or refusal-based successful trajectories without degrading performance on active reasoning tasks.

**Evidence:** CoPE gains on Retail ... but drops on Airline ... because Airline's task and reward design makes this over-representation extreme. ... the forecaster, trained only on the rewarded copies, carries refusals over to tasks that require action.