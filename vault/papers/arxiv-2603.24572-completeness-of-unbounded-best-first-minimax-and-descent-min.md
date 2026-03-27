---
# CSL-compatible fields
title: "Completeness of Unbounded Best-First Minimax and Descent Minimax"
author:
  - literal: "Quentin Cohen-Solal"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24572"

# Custom fields
paper_id: "2603.24572"
paper_source: "arxiv"
domain: "reinforcement-learning"
tags:
  - "reinforcement-learning"
  - "agent"
  - "planning"
  - "evaluation"
architectures:
  []
datasets:
  []
skill: "GeneralMLSkill"
processed_at: "2026-03-26T06:26:30Z"
created_at: "2026-03-26T06:26:30Z"
---

# Completeness of Unbounded Best-First Minimax and Descent Minimax

**Authors**: Quentin Cohen-Solal
**Date**: 2026-03-25
**Paper ID**: [arxiv:2603.24572](https://arxiv.org/abs/2603.24572)

## Summary

This paper addresses the theoretical completeness of two minimax search algorithms, Unbounded Best-First Minimax and Descent Minimax, which are fundamental in knowledge-free reinforcement learning but are known to be incomplete. The authors generalize these algorithms by incorporating the completion technique and formally prove that this generalized class of algorithms is complete, guaranteeing they compute the best possible strategy in two-player perfect information games. Furthermore, experimental validation is provided, confirming that the completion technique empirically enhances the winning performance of these search methods. The work resolves an open question regarding the efficacy of the completion technique in achieving optimal strategy determination.

## Key Contributions

- Generalized Unbounded Best-First Minimax and Descent Minimax algorithms incorporating the completion technique.
- Demonstrated that the generalized algorithms (with completion) are complete, meaning they are guaranteed to compute the best possible strategy.
- Showcased through experimentation that the completion technique significantly improves the winning performance of these minimax search algorithms.

## Limitations

The theoretical completeness proof applies to a specific class of algorithms (generalized Best-First Minimax and Descent Minimax with completion), and the practical applicability to all state-of-the-art knowledge-free RL algorithms requires further investigation.

## Open Questions & Future Work

- [[practical-utility-of-unbounded-minimax-variants]]

## Limitations

The theoretical completeness proof applies to a specific class of algorithms (generalized Best-First Minimax and Descent Minimax with completion), and the practical applicability to all state-of-the-art knowledge-free RL algorithms requires further investigation.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.24572)
- [PDF](https://arxiv.org/pdf/2603.24572)

