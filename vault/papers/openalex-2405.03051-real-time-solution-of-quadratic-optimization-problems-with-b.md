---
# CSL-compatible fields
title: "Real-Time Solution of Quadratic Optimization Problems with Banded Matrices and Indicator Variables"
author:
  - literal: "Andres Gomez"
  - literal: "Shaoning Han"
  - literal: "Leonardo Lozano"
issued:
  date-parts:
    - [2026, 10, 23]
url: "https://arxiv.org/abs/2405.03051"

# Custom fields
paper_id: "2405.03051"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "optimization"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:28:54Z"
created_at: "2026-10-25T09:28:54Z"
---

# Real-Time Solution of Quadratic Optimization Problems with Banded Matrices and Indicator Variables

**Authors**: Andres Gomez, Shaoning Han, Leonardo Lozano
**Date**: 2026-10-23
**Paper ID**: [openalex:2405.03051](https://arxiv.org/abs/2405.03051)

## Summary

This paper investigates mixed-integer quadratic optimization problems featuring banded matrices and indicator variables, which frequently occur in time-series change-point detection and anomaly monitoring. The authors develop a decision diagram-based approach that exploits temporal dependencies to construct exact and approximate representations, running in polynomial time for bandwidth-one matrices. Furthermore, they demonstrate an additive approximation scheme for fixed bandwidths and condition numbers, enabling real-time online solving via shortest path algorithms in milliseconds.

## Key Contributions

- Proposes a decision diagram-based method for solving mixed-integer quadratic optimization problems with banded matrices and indicator variables arising in time-series monitoring and anomaly detection.
- Shows that for problems with bandwidth equal to one, the proposed method runs in polynomial time, and yields an additive approximation scheme when the bandwidth and condition number are fixed.
- Demonstrates through computational experiments that the algorithm compares favorably against state-of-the-art off-the-shelf solvers for bandwidths <= 3 and achieves millisecond-level online execution.

## Archivist Review

After careful review, no concepts or open questions met the strict high-bar criteria for permanence in the vault. The paper addresses mixed-integer quadratic optimization with banded matrices using decision diagrams, which is primarily an operations research and optimization topic rather than a core machine learning forecasting methodology or reusable temporal modeling paradigm.

### Rejected Candidates
- [open_question] Tracking States in Epsilon-Exact Decision Diagrams (`theoretically-tracking-merged-states-epsilon-exact-decision-diagrams`) - low_impact: The question focuses on specific matrix-dependent state tracking in decision diagrams rather than a broad, reusable structural bottleneck across forecasting models.

## Links

- [Abstract](https://arxiv.org/abs/2405.03051)
- [PDF](https://arxiv.org/pdf/2405.03051)

