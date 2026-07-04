---
created_at: '2026-07-04T07:37:39Z'
source_papers:
- '[[openalex-2607.00581-decision-focused-sparse-tangent-portfolio-optimization]]'
title: Practical Constraints in DFL
---

**Background:** Portfolio optimization in institutional settings is governed by regulatory and mandate-specific constraints such as leverage limits, long-only requirements, and transaction cost penalties.

**Question / Future Work:** Integrating complex, non-trivial financial constraints into differentiable convex programming layers without sacrificing gradient flow or computational feasibility remains a significant technical challenge for the widespread adoption of decision-focused learning in finance.

**Why It Matters:** These constraints fundamentally alter the optimal frontier; without them, the utility of DFL-based optimization models in real-world finance is limited.

**Evidence:** Incorporating more practical constraints, such as long-only positions, leverage limits, turnover penalties, or margin constraints, remains an important direction for future work.