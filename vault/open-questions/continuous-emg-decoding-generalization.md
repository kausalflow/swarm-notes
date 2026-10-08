---
created_at: '2026-10-08T11:41:44Z'
source_papers:
- '[[openalex-2610.06450-emg-fm-bench-a-comprehensive-benchmark-for-foundation-model]]'
title: Generalization to Continuous EMG Decoding
---

**Background:** Foundation models pretrained on general time-series corpora are increasingly adapted to electromyography (EMG) signals, but their transfer performance varies widely across different downstream tasks and signal distributions.

**Question / Future Work:** Investigate whether the performance consistency observed across upper-limb classification, lower-limb classification, and continuous EMG-to-text decoding generalizes to a broader and more diverse set of continuous electromyographic decoding tasks and sequence-to-sequence datasets beyond emg2qwerty.

**Why It Matters:** Crucial for establishing whether task-consistency findings in foundation model adaptation hold universally across all types of continuous neuromuscular decoding or if they are restricted to specific task formulations.

**Evidence:** Because emg2qwerty is the only sequence-decoding dataset in the benchmark, additional datasets are needed to determine whether this consistency generalizes to other continuous decoding tasks.