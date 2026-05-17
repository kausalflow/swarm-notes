---
created_at: '2026-05-17T07:32:32Z'
source_papers:
- '[[openalex-2605.14840-in-context-learning-for-data-driven-censored-inventory-contr]]'
title: Identifiability in censored inventory control
---

**Background:** Censored feedback in repeated inventory control problems creates identifiability and coverage issues, where certain regions of the latent demand space may never be observed under conservative policies.

**Question / Future Work:** It remains an open problem to define minimal, necessary, and sufficient conditions under which offline predictive quality in censored environments translates into online decision-making performance guarantees. Quantifying the impact of identifiability barriers on regret in the absence of persistence or strong coverage conditions requires further investigation.

**Why It Matters:** Understanding the gap between offline predictive fit and online regret is fundamental for the reliability of data-driven operational decision-making where data is intrinsically missing.

**Evidence:** Censoring creates fundamental identifiability and coverage issues: the learner may never see certain regions of the latent space under conservative policies, so offline predictive quality may fail to translate to online decision quality.