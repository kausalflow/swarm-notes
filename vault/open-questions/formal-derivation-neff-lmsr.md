---
created_at: '2026-06-28T08:16:42Z'
source_papers:
- '[[openalex-2606.26583-preference-optimization-drives-monoculture-in-llm-prediction]]'
title: Formalizing N_eff in LMSR
---

**Background:** Prediction markets use scoring rules like the Logarithmic Market Scoring Rule (LMSR) to aggregate information, and N_eff is often used as a heuristic measure of agent diversity.

**Question / Future Work:** Current metrics for the effective number of independent forecasters rely on binary error-vector correlations, which lack a rigorous derivation connecting them directly to the posterior-price variance dynamics of LMSR-based markets. Establishing this link is necessary to quantify how agent correlation realistically impacts price discovery.

**Why It Matters:** Formalizing this relationship would move N_eff from a heuristic proxy to a grounded metric for evaluating the performance and robustness of agentic prediction systems.