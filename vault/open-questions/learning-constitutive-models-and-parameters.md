---
created_at: '2026-09-03T09:17:29Z'
source_papers:
- '[[openalex-2608.30926-a-neural-network-architecture-and-training-algorithm-to-pred]]'
title: Learning constitutive models and parameters
---

**Background:** Viscoelastic fluid simulations and experiments often face challenges in identifying the appropriate constitutive models and parameters, alongside obtaining simultaneous multi-field measurements.

**Question / Future Work:** Extend the assimilation-based neural network framework to simultaneously learn and determine unknown polymer constitutive models and underlying parameters as part of the inverse solution process for experimental datasets.

**Why It Matters:** Enables data-driven discovery of constitutive equations and physical parameters directly from partial flow observations without requiring offline training libraries.

**Evidence:** Another key unknown in an experiment is the polymer model and its underlying parameters. Our method has an advantage in that no offline data generation occurs, and in principle the model parameters can also be ‘learned’ as network outputs. Consideration of this kind of approach... is something we are actively exploring.