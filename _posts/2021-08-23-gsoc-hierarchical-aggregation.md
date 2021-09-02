---
title: "[GSOC 2021] Nemo Optimization by WAN Hierarchical Aggregation and Fidelity Control"
layout: single
categories:
  - GSOC
permalink: /nemo-wan-hierarchical-aggregation/
last_modified_at: 2021-08-23T23:00:00+09:00
header:
  teaser: /assets/images/gsoc.png

---

## 1. My Work
WAN Hierarchical Aggregation aims to add additional intermediate accumulation operator in front of final combine operator that accumulates data among physically nearby containers prior to shuffling across WAN, when needed.

## 2. What is done
The work can be separated into two parts, compile time and runtime.

### Compile Time
* Implemented **Intermediate combine**.
  * Previous Combine.PerKey transform consists of 2 steps.
    1. **Partial combine**(a.k.a. pre-aggregation) accumulates elements in each containers. Therefore, data transfer accross network is not needed in this step.
    2. **Final combine** shuffles all data(hashed by key) and then combine.
  * Additional(and optional) step that accumulates the pre-aggregated data partially(only among nearby containers) is implemented and inserted between 1(partial) and 2(final).
  * This new type of transform is only used in intermediate accumulator vertex, which is special type of operator vertex.
* Added new type of communication channel, **Partial Shuffle**, which represents data transfer from upstream operator to intermediate accumulator vertex. It resembles shuffle, but the difference is taht data shuffle occurs only among physically nearby containers.
* Implemented **optimization pass** that inserts intermediate accumulator vertex, which performs hierarchical aggregation prior to shuffle, only when it is expected to be effective.
* Implemented new vertex execution property, **ShuffleExecutorSetProperty**, consists of several node groups and each group represents physically close nodes.
* Implemented unit tests.

### Runtime
* Implemented new stage execution property, **TaskIndexToExecutorIDProperty**, that stores information about which container & node each task is allocated at.
  * Information will be stored at runtime, when TaskDispatcher dispatches a task to any container.
  * It will be used when upstream tasks of partial shuffle communication channel decide where to emit data.
* Implemented data transfer logic on partial shuffle communication channel.
  * Data from each executor must be transferred to nearby executors only.
* Implemented constraint when scheduling intermediate combine stage which consists of intermediate accumulator vertex, so that the tasks are evenly distributed across all node groups(ShuffleExecutorSetProperty).

## 3. TODO
* Code Refactoring
* Need more conditions to be implemented to make decision whether applying the pass is effective or not. Current logic is too naive.
* Currently the implemented scheduling constraint simply distributes tasks in the intermediate combine stage evenly to each node groups. It is expected to be updated, related to WAN aware scheduling policy.

## Github links
- Compile-time: [472-intermediate-combine](https://github.com/Kangji/incubator-nemo/commits/472-intermediate-combine?author=Kangji)
- Runtime: [472-comm-channel](https://github.com/Kangji/incubator-nemo/commits/472-comm-channel?author=Kangji)
