---
title: Branching Strategy
layout: single
categories:
  - Dev
  - Git
permalink: /dev/git/53/
last_modified_at: 2024-01-30T14:43:37

---

# Branching Strategy

## Git Flow

- **master**
    - stable & always on production-ready state
    - tag with release version
- **develop**
    - contains development changes for next release
- **feature**
    - implement new feature
    - merge into develop
- **release**
    - detailed check for release
    - merge into develop & master
- **hotfix / patch**
    - fix urgent bugs from **master**
    - merge into develop & master

## GitHub Flow

- Better for short release-interval
- **master is always deployable**
- **feature branch - pr - review - testing - deploy - merge**

<br>

[Back](/dev/git/)