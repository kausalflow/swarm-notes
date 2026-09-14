---
# CSL-compatible fields
title: "A Quantum Bluestein's Algorithm for Arbitrary-Size Quantum Fourier Transform"
author:
  - literal: "Nan-Hong Kuo"
  - literal: "Renata Wong"
issued:
  date-parts:
    - [2026, 9, 11]
url: "https://arxiv.org/abs/2512.15349"

# Custom fields
paper_id: "2512.15349"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-14T10:11:18Z"
created_at: "2026-09-14T10:11:18Z"
---

# A Quantum Bluestein's Algorithm for Arbitrary-Size Quantum Fourier Transform

**Authors**: Nan-Hong Kuo, Renata Wong
**Date**: 2026-09-11
**Paper ID**: [openalex:2512.15349](https://arxiv.org/abs/2512.15349)

## Summary

The paper introduces a quantum analogue of Bluestein's algorithm (QBA) to compute exact N-point Quantum Fourier Transforms for arbitrary, non-power-of-two lengths $N$ without zero-padding distortions. By factoring the QFT unitary into three diagonal quadratic-phase gates and two radix-2 QFT subcircuits, the approach achieves an asymptotic gate complexity of $O(N)$ using $O(\log N)$ qubits. The correctness of QBA is validated using Qiskit simulations, making it especially useful for applications like biomedical time-series analysis and quantum kernels where arbitrary signal lengths frequently occur.

## Key Contributions

- Proposes a quantum analogue of Bluestein's algorithm (QBA) that implements an algebraically exact N-point Quantum Fourier Transform (QFT) for arbitrary N without relying on zero-padding.
- Factors the N-dimensional QFT unitary into three diagonal quadratic-phase gates and two standard radix-2 QFT subcircuits of size M >= 2N - 1.
- Achieves an asymptotic gate complexity of O(N) while utilizing O(log N) qubits.
- Validates the exact correctness of QBA through concrete Qiskit implementation for arbitrary-length inputs.

## Archivist Review

The submitted paper deals with quantum algorithms (Quantum Bluestein's Algorithm for QFT) rather than machine learning for time-series forecasting, making its concepts and open questions too specific to quantum circuit design for the knowledge vault.

### Rejected Candidates
- [open_question] Deterministic Non-Probabilistic Quantum Convolution (`deterministic-non-probabilistic-quantum-convolution`) - low_impact: The paper is fundamentally a quantum computing paper on arbitrary-size Quantum Fourier Transforms, which falls outside the core time-series machine learning and forecasting scope of the vault.

## Links

- [Abstract](https://arxiv.org/abs/2512.15349)
- [PDF](https://arxiv.org/pdf/2512.15349)

