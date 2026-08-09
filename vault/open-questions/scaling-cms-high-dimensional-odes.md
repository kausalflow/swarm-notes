---
created_at: '2026-08-09T05:40:55Z'
source_papers:
- '[[openalex-2608.05777-curriculum-multiple-shooting-for-robust-training-of-neural-a]]'
title: Scaling Curriculum Multiple Shooting
---

**Background:** Neural and universal differential equations are trained on low-dimensional time-series data, but scaling these approaches to high-dimensional biological and omics datasets remains an open technical challenge.

**Question / Future Work:** Investigate how curriculum multiple shooting (CMS) and related advanced ODE training strategies scale to high-dimensional dynamical systems, such as genome-wide omics time-series data where models contain large numbers of states and parameters.

**Why It Matters:** High-dimensional dynamical systems modeling is critical for applications like single-cell genomics and systems biology, yet existing ODE training strategies often break down or become computationally intractable as state and parameter dimensions grow.

**Evidence:** Second, the models considered here are low-dimensional (<20 states), so it remains unclear how CMS scales to high-dimensional data, such as omics time-series data that are increasingly modeled with NODEs in biology [20, 47].