---
created_at: '2026-09-24T09:39:20Z'
source_papers:
- '[[openalex-2609.24294-toward-gpu-resident-climate-models-a-feasibility-study-on-lo]]'
title: Downstream Forecast Accuracy with Lossy Communication
---

**Background:** Lossy scientific data compression trades off storage and communication bandwidth against reconstruction error in numerical simulations.

**Question / Future Work:** Investigate the long-term cumulative effects of online lossy communication buffer compression on multi-day weather forecast integrations and forecast accuracy across diverse meteorological conditions.

**Why It Matters:** Ensuring that aggressive communication compression does not lead to unphysical numerical drift or degraded forecast skill over production integration windows is vital for operational deployment.

**Evidence:** The effect of this error on the final spherical harmonic coefficients and, downstream, on forecast accuracy over multi-day integrations requires a full end-to-end experiment...