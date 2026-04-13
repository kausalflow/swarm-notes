---
created_at: '2026-04-13T07:07:59Z'
source_papers:
- '[[openalex-2503.23960-testing-for-integer-integration-in-functional-time-series]]'
title: Joint asymptotic theory development
---

**Background:** The current statistical framework for testing integer versus fractional integration in functional time series relies on asymptotic theory that requires specific conditions for the bandwidth parameter q, particularly when addressing anti-persistent or weakly nonstationary components. A joint asymptotic theory that allows for the simultaneous convergence of the memory parameter to zero and the sample size to infinity is lacking.

**Question / Future Work:** The development of a unified asymptotic theory that captures the behavior of test statistics when the memory parameter d is close to the null integer value (local-to-zero asymptotics) is a significant gap. Future work is needed to provide a rigorous framework that does not rely on sequential asymptotics or restrictive assumptions about the relationship between the sample size and the bandwidth parameter, allowing for more reliable inference in cases of near-integer integration.

**Why It Matters:** Joint asymptotics are crucial for establishing the size and power properties of tests when the process is near an integer integration order, which is common in empirical applications like yield curves and mortality rates.

**Evidence:** While a joint asymptotic theory in which d1 -> 0 and T -> infinity simultaneously may be more useful, to the best of the authors’ knowledge, no requisite theory exists for the setup considered, which represents a potential avenue for future research.