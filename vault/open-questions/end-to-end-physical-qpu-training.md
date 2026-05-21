---
created_at: '2026-05-21T08:27:12Z'
source_papers:
- '[[openalex-2605.18333-qlif-cast-quantum-leaky-integrate-and-fire-for-time-series-w]]'
title: End-to-end Physical QPU Training
---

**Background:** Quantum-classical hybrid neural networks often rely on simulation for training, as running backpropagation through quantum circuits on physical hardware remains technically challenging due to NISQ device limitations.

**Question / Future Work:** There is a need to develop training frameworks that enable end-to-end backpropagation through quantum circuits directly on physical QPUs, addressing issues of hardware-in-the-loop gradient estimation and environmental noise management.

**Why It Matters:** Current reliance on classical simulators limits the empirical validation of quantum neural network scalability and real-world performance benefits.

**Evidence:** We will focus on training the full model on physical QPUs.