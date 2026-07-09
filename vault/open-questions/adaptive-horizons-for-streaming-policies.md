---
created_at: '2026-07-09T08:19:01Z'
source_papers:
- '[[openalex-2607.04739-spatial-attention-adapting-execution-horizons-for-diffusion]]'
title: Adaptive Horizons for Streaming Policies
---

**Background:** Generative policies that rely on discrete action chunking generally lack the ability to adapt execution horizons when interacting with continuous, streaming-based control architectures.

**Question / Future Work:** The current adaptive execution horizon framework is restricted to policies that produce discrete, chunked action sequences. Developing mechanisms to apply adaptive horizon control—or equivalent responsiveness modulation—to policies that generate actions in a truly continuous, streaming fashion remains an unresolved challenge.

**Why It Matters:** As robotics moves toward more fluid, streaming control policies, the inability to apply discrete-based adaptive horizon techniques creates a functional gap in ensuring real-time responsiveness and robustness for these newer architectures.

**Evidence:** A limitation, however, is that the framework requires a discrete action chunk. Therefore it does not extend to streaming-based policies, which generate actions continuously and expose no discrete chunk whose execution horizon can be adjusted.