---
created_at: '2026-03-25T21:18:04Z'
source_papers:
- '[[2603.23490-dynamic-light-spanners-in-doubling-metrics]]'
title: Doubling Dimension Independent Exponent
---

**Background:** The update time complexity for dynamic light spanners in doubling metrics is currently polynomial in $\log\Phi$ with an exponent dependent on the doubling dimension ($d$).

**Question / Future Work:** Can the runtime bound for dynamic light spanners be improved such that the exponent of $\log\Phi$ (or $\log n$) is independent of the doubling dimension $d$? Ideally, the goal is a runtime of $O(\log n)$ with an exponent of $O(d)$.