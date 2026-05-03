---
created_at: '2026-05-03T07:14:35Z'
source_papers:
- '[[openalex-2604.27443-abc-any-subset-autoregression-via-non-markovian-diffusion-br]]'
title: Scaling Continuous-time Generative Models
---

**Background:** Stochastic differential equation-based generative models for time series often suffer from computational overhead and physical inconsistency when handling high-dimensional, irregularly sampled, or non-causal conditioning data.

**Question / Future Work:** Developing efficient, scalable architectures (such as state-space models) for history compression and exploring hybrid sampling schemes (e.g., hierarchical or chunked generation) remain critical to overcoming the current bottlenecks in continuous-time generative modeling.

**Why It Matters:** These directions address specific bottlenecks in computational efficiency and scalability, providing a clear trajectory for future architectural development in continuous-time generative models.

**Evidence:** For a mathematically faithful implementation, we made the transformer network attend to the entire history, but there are efficient architectures (e.g., SSMs) that selectively compress the history. Future work could also consider... generating chunks of states at a time.