---
created_at: '2026-07-23T07:26:51Z'
source_papers:
- '[[openalex-2607.17507-residual-guided-multi-resolution-refinement-of-foundation-mo]]'
title: Stacking Test-Time Adaptation and Output Refinement
---

**Background:** Test-time adaptation dynamically updates model parameters online using auxiliary losses, whereas output refinement frameworks adjust predictions at inference time without modifying internal parameters.

**Question / Future Work:** Investigate the combination of parameter-updating test-time adaptation methods with inference-time output refinement wrappers like RGMR to evaluate potential complementary gains under distribution shifts.

**Why It Matters:** Combining parameter-based test-time adaptation with output-space refinement frameworks represents an important architectural exploration for balancing model stability and plasticity under distribution shifts.

**Evidence:** RGMR also differs from test-time adaptation: TTA updates parameters online with auxiliary losses, while RGMR refines outputs without touching parameters. The two are therefore complementary and could in principle be stacked; we leave this combination to future work.