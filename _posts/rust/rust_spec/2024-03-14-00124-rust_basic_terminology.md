---
title: Rust Basic Terminology
layout: single
categories:
  - Rust
  - Rust Spec
tags:
  - Grammar
permalink: /rust/rust_spec/124/
last_modified_at: 2024-03-14T22:30:23

---

## Value

Value is an entity represented by a set of bits.

## Variable

Variable is an abstract container for a value.

Variables can be referenced by one or more identifier: in most case only referenced by a single identifier. In this case it is called variable name.

## Variable Binding

Association between variable name and variable (or value stored in variable).

## Scope

Valid range of variable binding.

Compiler blocks the access to the variable via its name out of its scope.

## Type

The way value or value stored in variable might be resovled as.

## Reference

Conceptually, any value that refers to the variable and its value, such as memory address, are called reference of a variable or value.

All values are either referential or non-referential value.

## Resource

Any sort of hardware resources.
In most case it refers to memory.

<br>

[Back](/rust/rust_spec/)