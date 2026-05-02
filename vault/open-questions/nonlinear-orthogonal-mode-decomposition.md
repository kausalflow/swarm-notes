---
created_at: '2026-05-02T06:57:10Z'
source_papers:
- '[[openalex-2604.26240-reduced-order-modeling-of-a-viscoelastic-turbulent-jet-with]]'
title: Nonlinear orthogonal mode decomposition
---

**Background:** Proper Orthogonal Decomposition (POD) provides a physically interpretable, linear low-dimensional basis for turbulent flows, but it often requires a large number of modes to capture the fine-scale dynamics of turbulent fields. Nonlinear model reduction techniques, such as autoencoders, offer potentially better compression rates but lack the orthogonality and clear energy ranking inherent in POD.

**Question / Future Work:** There is a need to develop hybrid reduced-order models that combine the physical interpretability and orthogonality of POD with the high compression efficiency and nonlinear representation capabilities of advanced machine learning architectures (e.g., nonlinear autoencoders) for complex turbulent flows. Future work should focus on defining frameworks that allow for a nonlinear, near-orthogonal basis that maintains clear energy ranking and physical interpretability.

**Why It Matters:** Bridging this gap is crucial for building ROMs that are both computationally efficient (requiring fewer modes) and physically interpretable, which is essential for scaling ROMs to highly complex, high-Reynolds or high-Weissenberg number turbulence.