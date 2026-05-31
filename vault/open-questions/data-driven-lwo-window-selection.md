---
created_at: '2026-05-31T08:09:07Z'
source_papers:
- '[[openalex-2605.30292-leave-a-window-out-modifying-the-jackknife-for-predictive-in]]'
title: Data-driven window selection
---

**Background:** The leave-a-window-out (LWO) predictive inference method introduces a hyperparameter representing the window length, which must be chosen to account for the temporal dependence structure of the data.

**Question / Future Work:** Determining a fully data-driven procedure for selecting the optimal window length hyperparameter for LWO that balances statistical efficiency and rigorous coverage guarantees remains an important research challenge.

**Why It Matters:** Automated hyperparameter selection is critical for the practical deployment of LWO, as improper window size selection can lead to either invalid coverage or unnecessary statistical inefficiency.