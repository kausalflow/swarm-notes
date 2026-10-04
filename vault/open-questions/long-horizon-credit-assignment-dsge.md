---
created_at: '2026-10-04T10:49:17Z'
source_papers:
- '[[openalex-2610.01128-grounding-large-language-models-in-dsge-simulators-for-polic]]'
title: Long-Horizon Credit Assignment in Economic Simulators
---

**Background:** Large language models deployed in multi-turn environments face challenges in attributing delayed rewards to earlier decisions without a learned value function.

**Question / Future Work:** Develop and evaluate improved credit-assignment mechanisms, such as RUDDER-style return decomposition or specialized multi-turn advantage estimators, to address long-horizon delays in economic simulator grounding where policy effects appear several quarters after an action is taken.

**Why It Matters:** Long-horizon credit assignment is a fundamental bottleneck in applying reinforcement learning to language agents in dynamic environments with delayed feedback, making robust algorithmic comparisons and improvements crucial.

**Evidence:** This setting creates a long-horizon credit-assignment problem. Policy effects may appear several quarters after an action is taken. PPO has a learned value function that can propagate delayed reward to earlier tokens through generalized advantage estimation. GRPO has no learned value function and instead assigns a group-relative advantage from complete rollout returns.