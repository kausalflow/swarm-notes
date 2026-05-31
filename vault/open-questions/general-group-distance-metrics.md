---
created_at: '2026-05-31T08:08:58Z'
source_papers:
- '[[openalex-2605.29780-entropic-and-algebraic-transcript-based-tools-in-time-series]]'
title: Distance Metrics for General Groups
---

**Background:** The Cayley and Kendall distances provide rigorous metrics for quantifying dissimilarity between permutations within symmetric groups. Translating these distance metrics to general finite groups is currently achieved through embedding techniques, such as Cayley's theorem.

**Question / Future Work:** Developing a computationally efficient and theoretically robust way to define and compute distances in general groups without relying on specific group embeddings would be a significant advancement. Currently, the methodology for non-symmetric groups depends on the choice of Cayley's isomorphism, which can introduce gaps in the distance values and complicates direct interpretation. Future work should investigate whether distance metrics can be derived directly from the algebraic structure (e.g., the group's multiplication table) rather than through permutation-based encoding.

**Why It Matters:** This is a fundamental methodological limitation for applying transcript-based tools to arbitrary groups beyond symmetric groups, as it affects the sensitivity and range of dissimilarity quantification.

**Evidence:** However, this does not happen with D_C,K(Φ)(a,b) because Φ(G) is a subgroup of cardinality |G| of the group Sym(G), whose cardinality is |G|!, so not all possible distances can be realized (unless |G|=2). We call “the gaps in D_C,K(Φ)” the values in {0,1,...,D_C,K,max(Φ)} missing from the distance matrix...