---
created_at: '2026-06-26T08:29:14Z'
source_papers:
- '[[openalex-2507.12814-ronom-reduced-order-neural-operator-modeling]]'
title: Discretization error for adaptive neural operators
---

**Background:** Reduced-order modeling (ROM) methods generally rely on fixed discretizations, whereas operator learning approaches achieve resolution-invariance but often lack formal error guarantees.

**Question / Future Work:** Developing discretization error estimates for ROM-based neural operator frameworks that remain valid when the underlying function basis or discretization changes dynamically remains a key challenge for physics-informed modeling.

**Why It Matters:** Addressing this gap is necessary to ensure that resolution-invariant models provide reliable convergence properties in critical PDE solving applications.

**Evidence:** In future work, we plan to investigate adaptive FEM bases and aim to develop discretization error estimates...