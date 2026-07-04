---
created_at: '2026-07-04T07:37:53Z'
source_papers:
- '[[openalex-2607.00348-gtls-a-gpu-accelerated-method-for-periodic-transit-detection]]'
title: Optimizing In-Transit Chi-Squared Calculation
---

**Background:** The Transit Least Squares (TLS) algorithm, while effective at detecting small, Earth-sized planets by accounting for stellar limb darkening, is computationally intensive due to the requirement of performing point-by-point summation for the in-transit chi-squared calculation. This computational cost scales as O(n²) with the number of data points n, creating a bottleneck that becomes significant for large-scale photometric datasets.

**Question / Future Work:** Improving the efficiency of the in-transit chi-squared calculation, which currently acts as the dominant performance bottleneck, remains a challenge due to the lack of a recursive evaluation strategy comparable to the one used for out-of-transit residuals. Development of new algorithms or parallelization strategies to mitigate the workload imbalance arising from variable transit durations is necessary for faster, large-scale transit searches.

**Why It Matters:** This is a critical bottleneck preventing the scaling of TLS-style searches to the next generation of large-scale, high-cadence photometric surveys. Solving this would directly enable faster pipelines for future missions like PLATO and ET.

**Evidence:** evaluation of the in-transit χ2 term becomes the dominant computational bottleneck in the overall search pipeline.