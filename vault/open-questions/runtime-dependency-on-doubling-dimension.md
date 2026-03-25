---
source_papers:
- '[[2603.23490-dynamic-light-spanners-in-doubling-metrics]]'
title: Runtime Dependency on Dimension
---

**Background:** The final step in achieving fully dynamic light spanners with polylogarithmic update time in doubling metrics involves minimizing the dependency of the runtime on the metric space's aspect ratio ($\Phi$). The current solution's runtime depends on $(\log \Phi)^{O(d)}$.

**Question / Future Work:** Can the runtime bound for maintaining a dynamic light spanner in doubling metrics be improved such that the exponent of $\log \Phi$ (or $\log n$) is independent of the doubling dimension $d$? Ideally, the update time should be in $O(\log n)$ time, matching the best known runtime for dynamic sparse spanners.