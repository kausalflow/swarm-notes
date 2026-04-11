---
created_at: '2026-04-11T05:53:51Z'
source_papers:
- '[[openalex-2604.07159-sbbts-a-unified-schrödinger-bass-framework-for-synthetic-fin]]'
title: Formal convergence of SBBTS
---

**Background:** The Schrödinger–Bass Bridge for Time Series (SBBTS) training algorithm relies on neural networks to estimate the score of the diffusion process. However, the theoretical convergence properties of this iterative training approach are currently unproven.

**Question / Future Work:** Formal convergence guarantees for the proposed SBBTS training algorithm remain an open question. While the algorithm demonstrates empirical convergence within a small number of iterations, a rigorous mathematical framework justifying its stability and optimality is currently lacking.

**Why It Matters:** Providing theoretical convergence guarantees is essential for the reliability and trustworthiness of generative models in high-stakes financial applications, where the stability of the learned drift and volatility is critical.

**Evidence:** On the theoretical side, although Algorithm 1 converges consistently within K = 5 iterations in our experiments, formal convergence guarantees remain an open question.