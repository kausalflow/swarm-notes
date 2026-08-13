---
# CSL-compatible fields
title: "SSHafe: A Real-Time SSH Brute Force Attack Detection and Novel Credential Rotation Standard"
author:
  - literal: "Aditya Mitra"
  - literal: "Amar Kumar Mandal"
  - literal: "A. Shah"
  - literal: "Iqra Naz"
  - literal: "E. Fatih Yetkin"
  - literal: "Tuğçe Ballı"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09066"

# Custom fields
paper_id: "2608.09066"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "anomaly-detection"
  - "robustness"
  - "security"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:10:18Z"
created_at: "2026-08-13T06:10:18Z"
---

# SSHafe: A Real-Time SSH Brute Force Attack Detection and Novel Credential Rotation Standard

**Authors**: Aditya Mitra, Amar Kumar Mandal, A. Shah, Iqra Naz, E. Fatih Yetkin, Tuğçe Ballı
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09066](https://arxiv.org/abs/2608.09066)

## Summary

This paper introduces SSHafe, a real-time system for detecting and mitigating SSH brute-force attacks by extracting behavioral features through multi-scale sliding windows from authentication logs and classifying them with a lightweight LightGBM model. Upon attack detection, SSHafe automatically blocks the targeted account and initiates a novel passkey-based password-rotation workflow that binds authentication and credential updates into a single cryptographic flow. Experimental results on benchmark data and live adversarial traffic demonstrate 99.96% accuracy and rapid attack suppression within ten seconds.

## Key Contributions

- Proposes SSHafe, a real-time SSH brute-force detection and mitigation system combining multi-scale sliding-window time-series feature engineering with a lightweight LightGBM classifier.
- Achieves a detection accuracy of 99.96% on benchmark data and effectively identifies slow, distributed, and threshold-aware attacks within ten seconds on live adversarial traffic.
- Introduces a novel passkey-based password-rotation standard that unifies authentication and credential updating into a single cryptographically bound flow without OTPs, email verification, or session cookies.

## Archivist Review

Applied strict filtering for the TimeSeriesSkill vault. The paper focuses on cybersecurity (SSH brute-force detection and passkey credential rotation), which falls outside the core temporal forecasting, modeling, and representation learning scope of this vault. Consequently, no concepts or open questions were approved.

### Rejected Candidates
- [open_question] Multi-Signal Intrusion Detection Integration (`multi-signal-intrusion-detection-integration`) - low_impact: The question proposes broad future work combining security logs across multiple systems, which is standard multi-source SIEM integration rather than a specific unresolved methodological bottleneck in time-series forecasting or ML architectures.

## Links

- [Abstract](https://arxiv.org/abs/2608.09066)
- [PDF](https://arxiv.org/pdf/2608.09066)

