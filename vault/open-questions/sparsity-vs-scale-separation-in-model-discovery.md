---
created_at: '2026-05-21T08:40:22Z'
source_papers:
- '[[openalex-2504.00359-discovering-a-low-dimensional-temperature-control-architectu]]'
title: Sparsity vs. Scale Separation
---

**Background:** Mathematical models of physiological systems often exhibit scale separation, where certain parameters or terms are essential for global dynamics but are orders of magnitude smaller than others. Standard model selection techniques using sparsity penalties often prune these essential smaller terms, leading to models that fail to capture the observed system behavior.

**Question / Future Work:** Developing model selection algorithms that can simultaneously maintain parsimonious model structures (sparsity) while respecting scale separation in both parameter coefficients and term impacts remains a major challenge. Current thresholding methods often mistakenly prune terms essential for governing long-term dynamic behavior.

**Why It Matters:** This is a fundamental bottleneck for data-driven modeling of complex biological and physical systems characterized by hierarchical control processes and disparate time scales.

**Evidence:** Designing a threshold to promote sparsity and respect scale separation in both coefficient size and term size is a challenging problem in model selection for partially observed systems.