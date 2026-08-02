---
created_at: '2026-08-02T07:26:52Z'
source_papers:
- '[[openalex-2607.27604-revisiting-the-adversarial-robustness-of-graph-based-traffic]]'
title: Provably Non-Regressive Forecasting Defenses
---

**Background:** Graph-based traffic forecasting models are susceptible to adversarial attacks, but existing defenses like adversarial training are often attack-specific and can be bypassed by adaptive attackers.

**Question / Future Work:** Developing robust defenses for graph-based traffic forecasting that provably prevent regression under adaptive adversarial attacks remains an open challenge.

**Why It Matters:** Ensures that defenses maintain worst-case robustness guarantees without degrading performance on minor benchmark settings.

**Evidence:** Although initialized to match its AT baseline and kept there by a keep-best selection, a fully adaptive attacker through the added adapter can still exploit it on a minority of settings (one of fifteen regresses slightly); a construction that provably never regresses remains open.