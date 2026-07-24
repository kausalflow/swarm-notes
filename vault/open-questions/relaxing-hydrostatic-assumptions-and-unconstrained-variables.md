---
created_at: '2026-07-24T07:25:48Z'
source_papers:
- '[[openalex-2607.18877-physics-informed-super-resolution-of-atmospheric-data]]'
title: Relaxing Hydrostatic Assumptions and Unconstrained Variables
---

**Background:** Atmospheric data super-resolution models rely on hydrostatic primitive equations that depend on simplifying assumptions like hydrostatic balance, which fail in fine-resolution or strongly convective settings and cannot model unconstrained quantities such as precipitation.

**Question / Future Work:** Future work needs to relax simplifying assumptions like hydrostatic balance to accommodate fine-resolution or strongly convective settings, and develop more general physical representations for variables whose governing equations are incomplete or difficult to formulate explicitly (such as precipitation).

**Why It Matters:** Addressing limitations in governing equations and extending physics-informed constraints to unconstrained variables like precipitation is vital for extending climate models to finer scales and broader meteorological phenomena.

**Evidence:** A key limitation of this work lies in the governing equations used to constrain the model. The hydrostatic primitive equations rely on simplifying assumptions, such as hydrostatic balance, which becomes less accurate at fine resolutions or in strongly convective settings. Moreover, the constrained variable is limited by the coverage of variables defined in the governing equations. Unconstrained quantities such as precipitation will potentially yield limited improvements. Future work may relax these assumptions according to the characteristics of real-world data, and could develop more general physical representations for variables whose governing equations are incomplete or difficult to formulate explicitly.