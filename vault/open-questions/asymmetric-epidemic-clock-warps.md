---
created_at: '2026-08-20T05:21:30Z'
source_papers:
- '[[openalex-2608.16537-bayesian-epidemic-alignment-for-causal-evaluation-of-seasona]]'
title: Asymmetric Epidemic Clock Warps
---

**Background:** Current curve registration techniques for functional data often separate phase variation from amplitude variation via two-stage procedures, which discard alignment uncertainty before downstream causal evaluation.

**Question / Future Work:** Extend the Bayesian epidemic alignment framework to handle asymmetric temporal deformations (where growth and decline rates change differently across seasons) beyond symmetric affine clock warps, while properly preserving and propagating the joint uncertainty into causal effect estimates.

**Why It Matters:** Handling asymmetric epidemic deformation is critical for capturing realistic non-linear seasonal shifts in infectious disease outbreaks without discarding uncertainty in functional curve registration.

**Evidence:** The main structural limitation is that affine warping cannot represent asymmetric deformation, in which growth and decline change differently; monotone spline warps would relax this at the cost of a harder identification problem.