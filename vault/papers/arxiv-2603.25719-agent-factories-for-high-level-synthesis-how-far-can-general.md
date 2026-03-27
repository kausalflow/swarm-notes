---
# CSL-compatible fields
title: "Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?"
author:
  - literal: "Abhishek Bhandwaldar"
  - literal: "Mihir Choudhury"
  - literal: "Ruchir Puri"
  - literal: "Akash Srivastava"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25719"

# Custom fields
paper_id: "2603.25719"
paper_source: "arxiv"
domain: "tool-use"
tags:
  - "agent"
  - "tool-use"
  - "llm"
  - "optimization"
  - "code-generation"
  - "emergent-abilities"
architectures:
  []
datasets:
  - "HLS-Eval"
  - "Rodinia-HLS"
skill: "GeneralMLSkill"
processed_at: "2026-03-27T06:07:15Z"
created_at: "2026-03-27T06:07:15Z"
---

# Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?

**Authors**: Abhishek Bhandwaldar, Mihir Choudhury, Ruchir Puri, Akash Srivastava
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25719](https://arxiv.org/abs/2603.25719)

## Summary

This paper investigates the efficacy of general-purpose coding agents for High-Level Synthesis (HLS) optimization by introducing the Agent Factory, a two-stage pipeline that decomposes designs, performs sub-kernel optimization via pragmas, and uses an Integer Linear Program (ILP) to guide the assembly of globally promising configurations. The second stage deploys multiple autonomous agents over these ILP candidates to explore cross-function optimizations missed by the initial decomposition. Evaluations on HLS-Eval and Rodinia-HLS demonstrate that scaling the number of agents provides significant speedups, achieving up to $20\times$ improvement, and these agents successfully rediscover complex hardware optimization patterns without explicit domain training. The results position agent scaling as a highly effective optimization axis for automated hardware design exploration.

## Key Contributions

- Introduction of the Agent Factory, a two-stage pipeline that coordinates multiple general-purpose coding agents for hardware synthesis optimization.
- Demonstration that scaling the number of agents (from 1 to 10) yields a mean $8.27\times$ speedup over baseline on HLS benchmarks, with peak speedups exceeding $20\times$ on streamcluster.
- Validation that general-purpose LLMs, without explicit hardware-specific fine-tuning, can rediscover known hardware optimization patterns like pragma recombination and loop fusion.
- Empirical finding that the best global optimization solutions often emerge from configurations not ranked highly by the initial Integer Linear Program (ILP) based on sub-kernel decomposition.

## Limitations

The study relies on a specific, high-capability proprietary model (Claude Code Opus 4.5/4.6) and the results might not generalize directly to smaller or open-source models without further testing.

## Key Concepts

- [Agent Factories](../concepts/agent-factories-for-hls.md): A two-stage pipeline that constructs and coordinates multiple autonomous optimization agents to perform hardware design optimization from high-level specifications.

## Datasets

- [HLS-Eval](../datasets/hls-eval.md)
- [Rodinia-HLS](../datasets/rodinia-hls.md)

## Limitations

The study relies on a specific, high-capability proprietary model (Claude Code Opus 4.5/4.6) and the results might not generalize directly to smaller or open-source models without further testing.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25719)
- [PDF](https://arxiv.org/pdf/2603.25719)

