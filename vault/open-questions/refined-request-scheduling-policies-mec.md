---
created_at: '2026-03-27T15:44:26Z'
source_papers:
- '[[openalex-2603.23323-pnap-lifecycle-aware-edge-multi-state-sleep-for-energy-effic]]'
title: Refined Request Scheduling Policies
---

**Background:** The processing model for service time at ECs utilizes separate queues for different request types (lifecycle vs. user requests) scheduled with a preemptive priority discipline, where higher-priority requests can preempt lower-priority ones.

**Question / Future Work:** More refined policies for scheduling requests across the defined priority queues are possible beyond the current preemptive discipline with same-priority FIFO, which the authors explicitly leave for further study. This suggests an open technical question regarding optimal preemptive scheduling rules when balancing service continuity (lifecycle operations) against immediate user request processing.

**Why It Matters:** Exploring refined, non-preemptive, or alternative priority scheduling policies may yield better performance trade-offs between service continuity and immediate user response times than the adopted preemptive discipline.

**Evidence:** More refined policies are of course possible but are left for further study.