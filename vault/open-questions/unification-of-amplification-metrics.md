---
created_at: '2026-06-01T10:10:29Z'
source_papers:
- '[[openalex-2509.08048-forecasting-generative-amplification]]'
title: Unification of amplification metrics
---

**Background:** Generative networks are increasingly used to simulate high-energy physics events at the LHC to overcome computational bottlenecks. Quantifying the statistical "amplification" (the degree to which a generated dataset effectively exceeds the statistical power of its training data) remains a critical open challenge for assessing the reliability of these simulations.

**Question / Future Work:** A unified and universally applicable metric for generative amplification in high-dimensional physics phase spaces is currently lacking. While methods like averaging (based on phase-space integrals) and differential amplification (based on hypothesis testing) provide useful estimates, they often produce slightly different results, and the choice of an optimal summary statistic or integration region is not uniquely determined. Developing a robust, standardizable framework that resolves these discrepancies without requiring large holdout datasets is a key research direction.

**Why It Matters:** As generative networks replace classical simulation chains, the lack of a standardized, reliable metric for amplification introduces unknown systematic uncertainties into collider physics analyses. Tracking this allows for the development of benchmarks to trust simulated data at the HL-LHC.

**Evidence:** The amplification factors from averaging and differential estimates differ slightly, which is not unexpected... Our comparison does not prefer one estimate over the other. Instead, it shows the importance of selecting an amplification measure that is appropriate for a given dataset and application.