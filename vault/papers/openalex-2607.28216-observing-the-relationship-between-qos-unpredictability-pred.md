---
# CSL-compatible fields
title: "Observing the Relationship between QoS Unpredictability, Prediction Error, and User Activity in a Remote Desktop Service"
author:
  - literal: "Keisuke Ishibashi"
  - literal: "Xuliang Deng"
  - literal: "Yoshiaki Kitaguchi"
  - literal: "Kenichi Nagami"
  - literal: "Ichiro Mizukoshi"
  - literal: "Akira Sato"
  - literal: "Daiyu Nobori"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.28216"

# Custom fields
paper_id: "2607.28216"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:27:36Z"
created_at: "2026-08-02T07:27:36Z"
---

# Observing the Relationship between QoS Unpredictability, Prediction Error, and User Activity in a Remote Desktop Service

**Authors**: Keisuke Ishibashi, Xuliang Deng, Yoshiaki Kitaguchi, Kenichi Nagami, Ichiro Mizukoshi, Akira Sato, Daiyu Nobori
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.28216](https://arxiv.org/abs/2607.28216)

## Summary

This paper investigates the relationship between Quality of Service (QoS) fluctuations and user activity in Remote Desktop Services using real-world usage logs from the Thin-Telework System. Unlike prior experimental studies focusing solely on average QoS metrics, the authors analyze time-series of round-trip time (RTT), packet counts, and byte counts to show that QoS unpredictability (temporal standard deviation) and prediction error (instantaneous deviation from the mean) are significantly associated with user behavior. These findings offer valuable psychological and behavioral insights into how network variability impacts remote work engagement.

## Key Contributions

- Analyzed real-world usage logs from a production Remote Desktop Service (Thin-Telework System) to study the relationship between QoS metrics and user activity.
- Demonstrated that QoS unpredictability (temporal fluctuation such as standard deviation) and prediction error (instantaneous deviation from the mean) are significantly associated with user activity, unlike prior work limited to average RTT in experimental setups.
- Provided behavioral insights into user activity in interactive remote desktop environments by linking network QoS statistics to psychological mechanisms of unpredictability and error.

## Limitations

The study is observational and relies on logs from a specific remote desktop system (Thin-Telework System), which may limit generalizability to other platforms without further validation.

## Open Questions & Future Work

- [[confounding-factors-qos-user-activity]]

## Archivist Review

Approved one open question concerning confounding factors in QoS-activity relationships as it targets causal identification in observational telecommunications logs. Rejected the long-term observation question as a routine call for more data/longer windows. No concepts met the stringent standards for generalizable forecasting methods.

### Approved Open Questions
- Confounders in QoS-Activity Relationships: Essential for establishing causal relationships rather than mere correlations between network unpredictability metrics and user engagement in distributed enterprise systems.

### Rejected Candidates
- [open_question] Long-Term RDS User Dynamics (`long-term-observation-rds-dynamics`) - low_impact: Standard dataset duration extension request rather than a conceptual architectural or methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.28216)
- [PDF](https://arxiv.org/pdf/2607.28216)

