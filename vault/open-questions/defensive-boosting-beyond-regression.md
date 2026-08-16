---
created_at: '2026-08-16T05:17:56Z'
source_papers:
- '[[openalex-2608.13554-defensive-boosting-for-online-probabilistic-forecasting]]'
title: Extensive Multi-Class Defensive Boosting
---

**Background:** Online probabilistic forecasting algorithms combine online learning algorithms for weak hypothesis classes to achieve robust predictive performance across diverse adversarial settings.

**Question / Future Work:** Investigate whether the strong theoretical guarantees and empirical efficiencies of defensive boosting can be effectively extended to broader classes of non-binary, multi-class, or structured prediction problems beyond binary and bounded real-valued outcomes, while maintaining optimal oracle complexity.

**Why It Matters:** Extending defensive boosting beyond binary and bounded regression to more complex structured prediction tasks is a crucial direction for broadening the applicability of online boosting algorithms.

**Evidence:** Finally, we note that our algorithm also handles arbitrary bounded real-valued outcomes, and its squared-loss span guarantee holds unchanged, just as it does in the binary setting. Appendix D describes this in more detail, and evaluates this extension on three chronological regression streams.