---
created_at: '2026-07-04T07:35:51Z'
source_papers:
- '[[openalex-2607.00720-detecting-the-undetectable-enhancing-unsupervised-time-serie]]'
title: Improving Stability of Minimax Feedback
---

**Background:** Active learning frameworks for time series anomaly detection often rely on minimax-based learning objectives that maximize reconstruction errors for anomalous samples to distinguish them from normal ones. This approach is prone to learning instability and performance degradation under diverse data distributions.

**Question / Future Work:** The minimax loss strategy, while effective at discriminating between normal and abnormal patterns, may lead to training instability or suboptimal performance depending on the characteristics and diversity of labeled anomaly samples. Future research should investigate alternative feedback mechanisms, such as metric learning techniques, to enhance training stability and generalization without heavy reliance on adversarial pseudo-labels.

**Why It Matters:** The reliance on minimax-based feedback is a core component of this framework's contribution, and its inherent instability represents a fundamental trade-off in reconstruction-based anomaly detection systems.