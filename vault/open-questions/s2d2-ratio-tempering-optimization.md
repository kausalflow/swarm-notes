---
created_at: '2026-03-27T09:10:03Z'
source_papers:
- '[[2603.25702-s2d2-fast-decoding-for-diffusion-llms-via-training-free-self]]'
title: Optimizing Ratio Tempering Factors
---

**Background:** Speculative decoding for diffusion models integrates autoregressive verification with parallel denoising steps, creating a hybrid generation trajectory.

**Question / Future Work:** Analyze the theoretical implications and practical performance of altering the rejection-sampling acceptance probability by using ratio tempering factors ($\gamma \neq 1$) to intentionally bias the acceptance/rejection decision, potentially optimizing the accuracy/speed trade-off beyond the standard exact ratio ($\gamma=1$).