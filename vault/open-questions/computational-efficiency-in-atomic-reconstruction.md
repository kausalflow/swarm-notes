---
created_at: '2026-04-11T05:56:50Z'
source_papers:
- '[[openalex-2604.07271-physics-informed-3d-atomic-reconstruction-and-dynamics-of-fr]]'
title: Accelerating 3D atomic reconstruction
---

**Background:** Reconstructing 3D atomic coordinates from single-projection low-dose transmission electron microscopy (TEM) images is an inherently ill-posed problem, as it requires resolving multiple degrees of freedom from limited signal-to-noise data without direct phase information.

**Question / Future Work:** The iterative nature of current physics-informed reconstruction frameworks (e.g., combining simulated annealing and MD relaxation) creates significant computational bottlenecks for high-throughput analysis, highlighting the need for efficient machine-learning surrogate models that can approximate the reconstruction process while maintaining physical fidelity.

**Why It Matters:** Overcoming the computational bottleneck is critical for scaling high-resolution 3D dynamic characterization to larger datasets and real-time experimental environments.