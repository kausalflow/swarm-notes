---
created_at: '2026-05-30T07:35:38Z'
source_papers:
- '[[openalex-2605.28153-skillful-high-resolution-weather-forecasting-independent-of]]'
title: Explicit 3D Atmospheric Modeling
---

**Background:** Regional weather forecasting models currently rely on high-resolution gridded surface variables for output, while representing upper-air atmospheric states only implicitly within latent space.

**Question / Future Work:** It is currently unresolved how to best extend regional, observation-driven machine learning models to explicitly model the three-dimensional structure of the atmosphere. Future work is required to determine the optimal architecture for vertical representation and to identify which additional observational data sources effectively constrain this vertical structure.

**Why It Matters:** Explicitly modeling 3D atmospheric dynamics is essential for improving forecast skill beyond the immediate near-surface layer and for achieving performance that competes with full-physics 3D NWP models.

**Evidence:** While ObsCast already produces forecasts for multiple variables of greatest practical interest, its explicit outputs are presently limited to near-surface quantities, with upper-air information only implicitly encoded in the latent state. Extending the system to explicitly model the three-dimensional atmosphere is a natural next step and appears feasible in light of the present results. It in turn motivates integrating additional observational sources to constrain the vertical structure.