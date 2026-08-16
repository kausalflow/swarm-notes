---
created_at: '2026-08-16T05:18:37Z'
source_papers:
- '[[openalex-2608.12841-aqua-recursively-self-improving-quantitative-trading-researc]]'
title: Coupling Factor Discovery and Model Development
---

**Background:** Quantitative investment research agents rely on isolated research loops for factor discovery and model development, but currently maintain these systems independently without shared learning or joint optimization.

**Question / Future Work:** Investigate how coupling the independently developed factor-discovery and model-development systems—such that discovered factors from the factor system directly feed the model training loop—can be achieved while rigorously maintaining leak-free separation and preventing downstream adaptive overfitting.

**Why It Matters:** Bridging symbolic factor discovery and neural time-series model development in a unified, leak-proof recursive self-improving pipeline represents a key frontier for autonomous financial research agents.

**Evidence:** Coupling the two systems is the natural next step: the factors discovered in Part I are direct inputs to the models trained in Part II. That coupling introduces a leakage channel neither part has on its own.