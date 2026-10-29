---
created_at: '2026-10-29T11:11:56Z'
source_papers:
- '[[openalex-2610.35352-from-stochastic-transport-models-to-high-dimensional-bayesia]]'
title: Adaptive Online Calibration of Stochastic Transport
---

**Background:** Stochastic transport models used in geophysical data assimilation depend on offline calibration procedures, making the development of online or adaptive calibration methods that continuously update transport coefficients as the flow changes an open challenge.

**Question / Future Work:** The statistics of unresolved scales evolve over time as underlying fluid flows change, meaning offline-calibrated stochastic models become progressively less representative. Developing computationally efficient methods for adaptive or online calibration that continuously update stochastic transport models during filtering remains an open research problem.

**Why It Matters:** Online and adaptive calibration bridges the gap between static offline parameter learning and real-time operational data assimilation where flow regimes dynamically shift.

**Evidence:** Rather than viewing calibration as a one-off offline procedure, it may be preferable to update the stochastic parametrisation periodically using more recent data. An even more attractive possibility is to perform the calibration continuously, allowing the stochastic transport model to adapt automatically to changes in the underlying dynamics. The development of computationally efficient methods for adaptive or online calibration remains an important open research problem and represents a promising direction for future work.