---
created_at: '2026-06-13T08:16:44Z'
source_papers:
- '[[openalex-2606.12240-multi-rate-mixture-of-experts-for-accelerating-liquid-neural]]'
title: Decoupled Multi-Time-Scale Training Strategy
---

**Background:** In multi-rate mixture-of-experts architectures, experts are assigned distinct time constants to capture different temporal scales, typically optimized through a joint loss function. Joint optimization of experts with heterogeneous temporal scales can introduce interference and suboptimal convergence.

**Question / Future Work:** There is a need for more effective training strategies, such as hierarchical or alternating optimization, to decouple the training of experts operating at different time scales. Exploring how to optimize experts independently or in a staged manner to prevent interference between fast-changing and slow-evolving dynamics remains an unresolved challenge.

**Why It Matters:** Decoupling training is critical for improving the specialized performance of experts and ensuring the model architecture successfully separates dynamics as intended by the multi-rate design.

**Evidence:** While this simplifies implementation, it limits the ability of the model to fully exploit the separation of time scales. In particular, fast dynamics and slow dynamics may have different learning behaviors and convergence rates, and joint training can introduce interference between them. A promising direction for future work is to develop training strategies that decouple the optimization across time scales...