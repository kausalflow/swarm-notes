---
created_at: '2026-10-08T11:42:07Z'
source_papers:
- '[[openalex-2604.19746-calibration-induced-systematics-in-salt3-training-and-their]]'
title: Unresolved FoM Calibration Shift Artifacts
---

**Background:** Photometric calibration uncertainties in supernova surveys propagate into cosmological analyses through both light-curve fitting and supernova light-curve model training.

**Question / Future Work:** Future investigations are needed to resolve unexpected artifacts in the figure of merit dependence on calibration shift amplitudes, particularly regarding nonlinear behaviors and anomalies where training-plus-fitting error combinations yield smaller degradation than fitting alone at larger shift scales.

**Why It Matters:** Resolving these nonlinearities and counterintuitive trends is vital for accurately modeling systematic error budgets and covariance matrices in upcoming Stage IV dark energy surveys.

**Evidence:** There are a few artifacts in Figure 10 that are not understood. First, FoM-vs-shift is reasonably linear with the exception of shift value 6. Second, while we naively expect that Train+Fit should always have smaller FoM compared to Fit, we see the opposite trend for some shift values, particularly for shift > 5. These discrepancies are well beyond the uncertainty levels expected for Stage IV surveys of approximately 1-2 mmag [70]. Future studies should investigate the origin of these effects.