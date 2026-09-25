---
created_at: '2026-09-25T09:54:26Z'
source_papers:
- '[[openalex-2609.25791-a-functional-central-limit-theorem-for-locally-stationary-ti]]'
title: Extensions of Non-Stationary Functional Limit Theory
---

**Background:** The asymptotic theory for locally stationary time series in infinite-dimensional Banach spaces relies on functional central limit theorems, but extending these invariance principles beyond Hilbert spaces or type-2 spaces requires overcoming significant challenges in controlling tail behaviors and infinite-dimensional tightness without assuming geometric restrictions.

**Question / Future Work:** While functional central limit theorems and change-point detection procedures have been established for locally stationary time series taking values in general separable Banach spaces without type-2 or cotype assumptions, future research must address extending these methods to broader classes of non-stationary models, such as those with time-varying long-run variances or gradual trend changes, and developing fully data-driven bootstrap or self-normalization techniques across arbitrary infinite-dimensional Banach spaces.

**Why It Matters:** This identifies critical methodological directions for non-stationary functional data analysis, moving beyond 'at most one change' models and constant long-run variance assumptions to more flexible time-varying frameworks in Banach spaces.

**Evidence:** In the context of locally stationary time series, the “at most one change” setting is not the most appropriate. Instead, we are often interested in detecting gradual changes of a smoothly varying mean μ(t)=E[H(t,F0)], where the long-run variance might vary over time. One approach would be to show the joint convergence of a bootstrap approximation and the partial sum processes... All of these approaches require their own central limit theorems, which can presumably be derived with the same arguments as Theorem 8.