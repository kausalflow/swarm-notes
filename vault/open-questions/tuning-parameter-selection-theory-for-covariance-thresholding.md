---
created_at: '2026-05-17T07:30:18Z'
source_papers:
- '[[openalex-2605.14491-adaptive-long-run-variance-thresholding-for-sparse-covarianc]]'
title: Consistency of Threshold Tuning
---

**Background:** High-dimensional covariance estimation requires selecting regularization parameters that remain consistent under complex temporal dependencies.

**Question / Future Work:** There is a need for rigorous theoretical guarantees for data-driven tuning parameter selection in the context of adaptive thresholding, as current approaches often rely on empirical methods like block cross-validation without established consistency proofs.

**Why It Matters:** Statistical consistency of the resulting sparse estimator depends heavily on optimal parameter selection, and the absence of such theory limits the applicability of these models in critical infrastructure or research environments.

**Evidence:** Although we do not provide a theoretical justification for this data-driven procedure, our numerical studies show that it performs reasonably well.