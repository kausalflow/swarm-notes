---
created_at: '2026-03-27T09:10:03Z'
source_papers:
- '[[2603.25702-s2d2-fast-decoding-for-diffusion-llms-via-training-free-self]]'
title: Causal Drafting Mask Impact
---

**Background:** Block-diffusion models offer parallelism by operating on blocks, but their interaction with autoregressive verification must be carefully managed for optimal performance.

**Question / Future Work:** Further investigate the effect of the optional partially causal drafting/caching mask (Equation 4) on the overall hybrid decoding trajectory, specifically assessing whether a more strictly causal drafting mask provides better local AR-guidance at the cost of KV cache utilization or overall speed.