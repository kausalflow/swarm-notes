---
created_at: '2026-05-10T07:22:10Z'
source_papers:
- '[[openalex-2408.02129-earthquake-magnitudes-depend-on-seismic-history-as-revealed]]'
title: Interpretability of seismic magnitude prediction features
---

**Background:** Earthquake forecasting models typically rely on the separability assumption, where magnitude distributions are treated as independent of earthquake locations and timing. Recent neural network models, such as MAGNET, have demonstrated that earthquake magnitudes possess identifiable dependencies on seismic history, which challenges this assumption.

**Question / Future Work:** Further research is required to perform ablation studies that quantify the relative contribution of different seismic history components (e.g., recent event sequences versus longer-term seismicity rates) to the neural network's predictive performance. Identifying these influential features would enhance model interpretability and provide deeper insights into the underlying physical mechanisms that allow for magnitude predictability.

**Why It Matters:** Ablation studies are critical for transitioning from black-box predictive models to physically informed, interpretable seismic models, enabling researchers to distinguish between mere statistical artifacts and genuine physical precursors.

**Evidence:** Specifically, future work should include ablation studies to determine the relative informativeness of the individual encoders, e.g. recent history versus local seismicity rate, to provide deeper insights into the physical mechanisms the model is leveraging.