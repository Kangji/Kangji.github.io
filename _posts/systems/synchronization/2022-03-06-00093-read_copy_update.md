---
title: Read Copy Update (RCU)
layout: single
categories:
  - Systems
  - Synchronization
tags:
  - OS
permalink: /systems/synchronization/93/
last_modified_at: 2024-02-05T17:26:42

---

Even RwLock needs to update the state **in synchronization variable**,
which undergoes the same performance issue: lock contention.

## Read-Copy-Update Overview

* Goal: very fast read
* Restricted update
  * Writer computes a new version
  * Publish the new version with single atomic write
  * Readers may see old or new version
* Integrated with scheduler
* Grace Period
  * When all readers lose the reference to old version, then gc.

![Read Copy Update](/assets/images/systems/synchronization/rcu.png)

<br>

[Back](/systems/synchronization/)