---
created_at: '2026-10-10T10:53:13Z'
source_papers:
- '[[openalex-2610.10440-seq-flow-efficient-probabilistic-forecasting-with-self-rollo]]'
title: Recursive Source-Distribution Error Control
---

**Background:** Online probabilistic forecasting models recursively reuse previous predictions as initial states or source distributions for subsequent flow or diffusion updates, creating a train-test distribution mismatch over long deployment horizons.

**Question / Future Work:** Investigate the theoretical and empirical dynamics of error accumulation and propagation when recursively reusing model-generated forecasts as source distributions in flow-matching and diffusion frameworks, particularly over extremely long-horizon rollouts beyond the training horizon.

**Why It Matters:** Understanding how errors propagate through recursive source distributions is crucial for designing stable few-step sequential generative models that do not degrade during extended autonomous operation.

**Evidence:** Although trained on self-rollouts of at most four updates, Seq-Flow remains accurate over more than 400 consecutive updates.