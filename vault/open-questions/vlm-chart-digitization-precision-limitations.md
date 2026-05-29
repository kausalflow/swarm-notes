---
created_at: '2026-05-29T08:39:19Z'
source_papers:
- '[[openalex-2605.27195-epicurvebench-evaluating-vlms-on-epidemic-curve-digitization]]'
title: VLM Chart Digitization Limitations
---

**Background:** Vision-language models frequently struggle with the accurate digitization of structured numerical time-series from visual charts due to issues with numerical precision and truncation in long sequences.

**Question / Future Work:** How to overcome systemic limitations in numerical reasoning and temporal truncation for VLM-based chart digitization remains an open challenge, particularly when evaluation metrics like ECS expose gaps that standard key-value benchmarks conceal.

**Why It Matters:** This addresses the gap between performance on generic chart benchmarks and task-specific utility in high-impact domains like public health.

**Evidence:** The diagnostic error breakdown points to concrete weaknesses—most prominently numerical imprecision on dense series and truncation of long series—for future models to address.