---
created_at: '2026-10-04T10:49:05Z'
source_papers:
- '[[openalex-2610.00976-variational-streaming-flow-probabilistic-forecasting-in-phys]]'
title: Hybrid and Jump-Aware Latent Dynamics
---

**Background:** Physical-time flow forecasting models like Variational Streaming Flow rely on smooth local motion derived from adjacent states to learn physical-time velocities, which can fail under abrupt impacts, discontinuities, or strong observation noise.

**Question / Future Work:** Future work should explore hybrid or jump-aware latent dynamics, controlled or rough differential equations, and higher-order or adaptive Runge–Kutta solvers to handle abrupt impacts, discontinuities, or strong observation noise that degrade local velocity resolution in physical-time forecasting.

**Why It Matters:** Addressing discretization errors and non-smooth physical transitions is critical for expanding continuous physical-time generative forecasting to robotics and complex real-world environments with discontinuities.

**Evidence:** VSF relies on adjacent states providing a meaningful local direction of motion for learning the physical-time velocity. This assumption is most reliable when the dynamics vary smoothly in physical time. Abrupt impacts, discontinuities, or strong observation noise can make the local velocity poorly resolved. VSF also uses explicit forward Euler integration, which can accumulate discretization error for coarse step sizes or rapidly varying learned fields (Hairer et al., 1993); solver choice can also affect the effective dynamics learned by neural ODEs (Zhu et al., 2022). Future work could therefore explore hybrid or jump-aware latent dynamics (Jia and Benson, 2019), controlled or rough differential equations (Kidger et al., 2020; Morrill et al., 2021), and higher-order or adaptive Runge–Kutta solvers (Queiruga et al., 2020).