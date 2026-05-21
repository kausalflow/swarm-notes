---
created_at: '2026-05-21T08:31:07Z'
source_papers:
- '[[openalex-2605.18188-utopya-a-multimodal-deep-learning-framework-for-physics-info]]'
title: Adaptive Physics-Informed Constraints
---

**Background:** Physics-informed regularisation, such as enforcing temporal smoothness and thermodynamic monotonicity, is commonly used to constrain neural networks in chemical process monitoring.

**Question / Future Work:** Current physics-informed constraints often assume steady-state equilibrium; however, developing state-dependent or phase-aware weighting would allow these constraints to be safely relaxed during transient phases like system startup where temporary thermodynamic deviations may be physically expected.

**Why It Matters:** This is a fundamental limitation in applying physics-informed machine learning to entire industrial process lifecycles rather than isolated steady-state windows.

**Evidence:** The current physics-informed monotonicity constraint, which enforces temperature decrease from reboiler to condenser, is strictly valid only at steady state.