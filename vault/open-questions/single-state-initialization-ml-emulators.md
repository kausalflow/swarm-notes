---
created_at: '2026-08-09T05:41:13Z'
source_papers:
- '[[openalex-2608.06107-kastor-an-efficient-fine-tuning-strategy-for-generative-emul]]'
title: Single-State Initialization for Emulators
---

**Background:** Machine learning physics emulators rely on fixed-length context windows to initialize auto-regressive rollouts, requiring traditional numerical solvers to provide the initial history.

**Question / Future Work:** Investigate eliminating the dependency on a fixed-length historical context window to initialize surrogate rollouts by designing models that can start predictions from a single initial state and progressively increase context length.

**Why It Matters:** Removing the requirement for pre-computed history from numerical solvers is critical for end-to-end deployment of ML emulators in autonomous scientific discovery and real-time forecasting pipelines.

**Evidence:** standalone emulator should ideally start rollouts from a single state; and then progressively increase the context length. Following existing practices in the field, we rely on a fixed-length context window to start rollouts, implicitly relying on a physics solver to provide the initial context.