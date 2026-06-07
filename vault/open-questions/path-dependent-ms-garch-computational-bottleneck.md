---
created_at: '2026-06-07T08:20:28Z'
source_papers:
- '[[openalex-2606.06190-multi-scale-markov-switching-garch]]'
title: Path-Dependent MS-GARCH Computation
---

**Background:** Markov-Switching GARCH models using independent parallel GARCH processes within each regime simplify computation but ignore the influence of volatility inherited from preceding regimes. This path-independence assumption often leads to discontinuities in volatility paths and persistent residual ARCH effects in standardized residuals.

**Question / Future Work:** It is currently unresolved how to maintain the computational tractability of multi-scale MS-GARCH models while simultaneously incorporating path-dependent variance dynamics, such as those found in the Gray (1996) specification. Developing efficient, path-dependent multi-scale MS-GARCH frameworks would likely resolve the remaining ARCH effects identified in residual diagnostics and improve the realism of regime-to-regime volatility transitions.

**Why It Matters:** The persistence of residual ARCH effects suggests that the current model, while superior to a single-regime GARCH, still fails to fully capture volatility clustering. This remains a significant bottleneck in volatility forecasting and risk management applications where accurately accounting for volatility carry-over is crucial.

**Evidence:** The fundamental cause is the path-independence assumption of the Haas et al. (2004) specification: when the market transitions from Crisis back to Calm, the Calm GARCH variance immediately reverts to its unconditional level, ignoring the elevated volatility inherited from the Crisis state. This creates a discontinuity in the implied volatility path that manifests as residual ARCH in the standardised residuals.