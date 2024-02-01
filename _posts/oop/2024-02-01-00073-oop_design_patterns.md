---
title: OOP Design Patterns
layout: single
categories:
  - Oop
permalink: /oop/73/
last_modified_at: 2024-02-01T20:39:57

---

Reference: [Refactoring Guru](https://refactoring.guru)

# Creational Patterns

Object instantiation

## Factory Patterns

- Factory Method
  - Abstract class with factory method which returns abstract class (product)
  - Concrete classes implement factory method which returns concrete class (product)
- Abstract Factory
  - Group of factory methods, which produce different objects
  - Two orthogonal domains: factory and product

## Builder

- Encapsulates the dynamic construction
- Director holds a predefined combination of builder options

## Prototype

- `Clone` trait

## Singleton

- Ensures a single instance

### Java Singleton

- Private constructor
- `getInstance()`
  - Multithreading Issue ⇒ Synchronize
- `synchronized`
  - Performance Issue ⇒ Double Check to avoid contention after created
  - OOO Execution / Cache Coherence ⇒ volatile
- Early initialization
  - Early initialized static field
- Static holder singleton
  - Use private static inner class with instance as static field
  - Private static inner class is initialized when first accessed (lazy)

# Structural Patterns

Object composition

## Adapter

- Convert an interface into another interface as clients expect
- Composition of adaptee / implement target interface

## Bridge

- Split the large class into two parts
- Composition of parts (interface)

## Composite

- Tree structure: Leaf Component or Composite Component (Group of Component) both implements Component interface

## Decorator

- **Dynamically** attaches additional features in **runtime**

## Facade

- A **god** object which provides a unified interface to a set of interface subsystems
- Defines higher level interface

## Proxy

- Access-controls to the original object
- Class diagram is similar with decorator, but the difference is access control

# Behavioral Patterns

Assignment of responsibilities between objects

## Chain of Responsibility

- Chain of handlers, each handles independent operation and pass input to next
- Chain is mutable in runtime
- Class diagram is similar with decorator & proxy

## Iterator

- Iterates over the data structure without revealing it’s structure

## Mediator

- All interaction between objects are managed by central mediator in order to loose the (many-to-many) dependencies.
- Each object now only depends on mediator object.

## Observer

- Pub/sub structure
- Subject(Publisher) invokes the method of Observer(Subscriber)
- Prevents polling

## State

- State Machine
- Delegates code which varies based on the state, including state transition code

## Strategy

- Similar to state but there is no transition
- Class that represents concrete algorithm
- Unlike state, the object changes the strategy itself

## Visitor

- Element & Visitor: two orthogonal domain
  - Visitor corresponds to the method of each element
- Visitor implements a single operation of all concrete elements
  - Element has `accept` method that invokes provided(as an argument) visitor.
- Use visitor pattern when elements are fixed and methods are extensible.

### Example

Deserialization

- Element: primitive types + compound types
- Method: `fn deserialize<T>(element) -> T` => implement Visitor for each `T`

<br>

[Back](/oop/)