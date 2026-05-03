---
# CSL-compatible fields
title: "ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space"
author:
  - literal: "Gabe Guo"
  - literal: "Thanawat Sornwanee"
  - literal: "Lutong Hao"
  - literal: "Elon Litman"
  - literal: "Stefano Ermon"
  - literal: "Jose Blanchet"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27443"

# Custom fields
paper_id: "2604.27443"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "diffusion-model"
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "autoregressive"
architectures:
  []
datasets:
  []
concept_slugs:
  - "any-subset-autoregressive-models-abc"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:14:35Z"
created_at: "2026-05-03T07:14:35Z"
---

# ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space

**Authors**: Gabe Guo, Thanawat Sornwanee, Lutong Hao, Elon Litman, Stefano Ermon, Jose Blanchet
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27443](https://arxiv.org/abs/2604.27443)

## Summary

ABC is a generative framework for continuous-time, continuous-space stochastic processes that models dynamics as non-Markovian diffusion bridges to address limitations in standard diffusion approaches. By conditioning on arbitrary subsets of states and scaling noise injection with physical time, the model captures complex dynamics more effectively than methods relying on noise-to-data evolution. The model is trained via a path- and time-dependent extension of denoising score matching, demonstrating significant performance gains in video generation and weather forecasting benchmarks.

## Key Contributions

- Introduces ABC, a framework using non-Markovian diffusion bridges to model continuous-time, continuous-space processes with physical time-aware noise scaling.
- Enables flexible path-dependent conditioning on arbitrary subsets of states, including future observations and irregularly sampled data.
- Outperforms state-of-the-art diffusion models in video generation and weather forecasting by avoiding the instability of uninformative noise-to-data generation.

## Open Questions & Future Work

- [[scaling-and-efficiency-in-continuous-time-generative-modeling]]

## Key Concepts

- [[any-subset-autoregressive-models-abc]]: A generative framework that models continuous stochastic processes as non-Markovian diffusion bridges to enable arbitrary subset conditioning.

## Archivist Review

Approved the ABC concept for its novel combination of non-Markovian bridges with arbitrary-subset conditioning. The open question was rewritten to focus on the technical bottleneck of scaling and history compression in continuous-time models, rather than listing generic future work. No datasets were approved as none were central to the contribution.

### Approved Concepts
- Any-Subset Autoregressive Models (ABC): The framework enables conditioning on arbitrary subsets of states in continuous-time processes, addressing a major limitation of standard diffusion models.

### Approved Open Questions
- Scaling Continuous-time Generative Models: These directions address specific bottlenecks in computational efficiency and scalability, providing a clear trajectory for future architectural development in continuous-time generative models.

### Rejected Candidates
- [open_question] Continuous-time Generative Model Extensions (`future-directions-for-continuous-time-generative-modeling`) - other: The original candidate was too broad and bundled multiple distinct research directions; it has been refined into a more focused question about scaling and efficiency.

## Links

- [Abstract](https://arxiv.org/abs/2604.27443)
- [PDF](https://arxiv.org/pdf/2604.27443)

