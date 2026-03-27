---
# CSL-compatible fields
title: "Provably Efficient Long-Time Exponential Decompositions of Non-Markovian Gaussian Baths"
author:
  - literal: "Zhen Huang"
  - literal: "Zhiyan Ding"
  - literal: "Ke Wang"
  - literal: "Jason Kaye"
  - literal: "Xiantao Li"
  - literal: "Lin Lin"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25708"

# Custom fields
paper_id: "2603.25708"
paper_source: "arxiv"
domain: "physics"
tags:
  - "theory"
  - "computational-physics"
  - "time-series"
  - "mathematical-analysis"
architectures:
  []
datasets:
  []
skill: "GeneralMLSkill"
processed_at: "2026-03-27T09:09:38Z"
created_at: "2026-03-27T09:09:38Z"
---

# Provably Efficient Long-Time Exponential Decompositions of Non-Markovian Gaussian Baths

**Authors**: Zhen Huang, Zhiyan Ding, Ke Wang, Jason Kaye, Xiantao Li, Lin Lin
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25708](https://arxiv.org/abs/2603.25708)

## Summary

This work provides rigorous complexity bounds for representing the correlation functions of non-Markovian Gaussian baths using sums of complex exponentials, a technique central to pseudomode and Hierarchical Equations of Motion (HEOM) methods. The analysis shows that for many spectral densities, the required number of exponentials is independent of the total simulation time $T$, achieving time-uniform complexity. The $T$-dependence only emerges polylogarithmically when the spectral density exhibits strong nonanalytic features like step discontinuities. The results confirm that the primary computational bottleneck for long-time simulation is the presence of sharp singularities in the bath spectrum, rather than the duration $T$ itself.

## Key Contributions

- Rigorous complexity bounds for representing non-Markovian Gaussian bath correlation functions on $[0,T]$ using sums of complex exponentials (as in pseudomode/HEOM methods).
- Demonstrating time-uniform complexity (independence of $T$) for a broad class of spectral densities.
- Quantifying the polylogarithmic dependence on $T$ introduced only by spectral densities with strong singularities (e.g., step discontinuities or inverse power-law divergences).
- Showing mild or absent temperature ($β$) dependence for bosonic and fermionic baths, respectively.

## Limitations

The analysis focuses on the complexity of the exponential decomposition of the bath correlation function, rather than the full simulation time complexity, which may involve other factors depending on the specific integration method used thereafter.

## Open Questions & Future Work

- [[complexity-bounds-for-tensor-network-influence-functionals]]
- [[optimal-complexity-for-multi-band-systems]]
- [[complexity-analysis-for-coupled-lindblad-theories]]

## Key Concepts

- [Pseudomode Methods](../concepts/pseudomode-methods.md): A family of numerical techniques used to simulate open quantum systems interacting with non-Markovian Gaussian environments by approximating the bath correlation functions with exponential sums.
- [Hierarchical Equations of Motion](../concepts/hierarchical-equations-of-motion.md): A set of coupled differential equations derived from the quantum master equation to describe the time evolution of a system interacting with a bath, often approximated using exponential decompositions.

## Limitations

The analysis focuses on the complexity of the exponential decomposition of the bath correlation function, rather than the full simulation time complexity, which may involve other factors depending on the specific integration method used thereafter.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25708)
- [PDF](https://arxiv.org/pdf/2603.25708)

