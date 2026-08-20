---
created_at: '2026-08-20T05:21:09Z'
source_papers:
- '[[openalex-2608.16070-oceanlight-efficient-global-ocean-forecasting-via-geometry-a]]'
title: Dynamic Unstructured Mesh Adaptation
---

**Background:** Data-driven global ocean forecasting models rely on static climatological unstructured meshes, failing to capture transient and short-term oceanic processes that affect high-resolution forecasting accuracy.

**Question / Future Work:** Investigate and develop methods for rapidly constructing and adapting unstructured meshes according to daily ocean conditions rather than long-term climatological averages, thereby capturing transient ocean processes for improved forecasting accuracy.

**Why It Matters:** Dynamic mesh adaptation is critical for capturing rapidly evolving ocean phenomena such as sudden upwellings and storm surges without incurring the prohibitive computational overhead of global fine grids.

**Evidence:** The unstructured mesh used in this model is constructed based on climatological state, meaning that it primarily reflects long-term averaged oceanic conditions rather than capturing daily dynamical variability.