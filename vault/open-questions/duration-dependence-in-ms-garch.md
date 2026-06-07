---
created_at: '2026-06-07T08:20:28Z'
source_papers:
- '[[openalex-2606.06190-multi-scale-markov-switching-garch]]'
title: Regime Duration Dependence Modeling
---

**Background:** Markov-switching models typically rely on the first-order Markov assumption, where transition probabilities depend solely on the current state and not the duration spent within that state. Empirically observed phenomenon of duration dependence in financial market regimes suggests that the probability of exiting a state may change as a function of the time already spent in that state.

**Question / Future Work:** The development of semi-Markovian MS-GARCH architectures, where transition probabilities are conditioned on regime duration, is a potential avenue to better capture market dynamics. Such models would allow for transition probabilities that evolve based on how long a system has been in a particular regime, offering a more realistic representation of structural market equilibria versus transient shocks.

**Why It Matters:** The first-order Markov assumption is a known simplification that likely fails to capture the 'memory' of market states. Incorporating duration dependence is essential for improving the accuracy of regime transition timing and duration forecasting in complex, non-stationary financial time series.

**Evidence:** The first-order Markov assumption implies that regime transitions depend only on the current state, not on how long the system has been in that state. Durland and McCurdy (1994) documented empirical evidence of duration dependence in US GNP growth regimes, motivating semi-Markov models in which transition probabilities depend on regime age.