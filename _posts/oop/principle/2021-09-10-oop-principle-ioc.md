---
title: "IoC"
layout: single
categories:
  - OOP
  - OOP Principle
permalink: /oop/principle/ioc/
last_modified_at: 2021-09-10T20:39:50+09:00

---

## Inversion of Control

일반적인 프로그램은 프로그램 코드들이 주체가 되어 프로그램의 흐름(control flow)을 결정하고 제어한다.
그러나 IoC 패러다임에서는 코드들은 프레임워크에 종속적이게 되고, 프레임워크가 각 코드를 제어하게 된다.

## Example: Dependency Injection

[DI](/oop/principle/di/)도 IoC가 적용된 예시이다.
서로 의존적일 수 있는 두 객체를 프레임워크가 각각 따로 생성하고 주입해줌으로써 정작 두 객체 사이의 의존성은 제거될 수 있다.

## Example: Event-Driven Programming

Event-Driven programming에서 event loop는 단순히 프레임워크나 런타임 환경에서 발생한 이벤트에 따라 이벤트 종류에 맞는 handler를 실행하는 작업을 반복한다.
이 때, event loop의 흐름을 제어하는 것은 결국 event를 발생시키는 프레임워크 또는 런타임 환경이 되므로 IoC가 적용되었다고 볼 수 있다.

## Other Examples

이 외에도 Callback함수, Scheduler 등도 다 IoC 패러다임이 적용된 예시이다.

<br>

모든 글: [OOP Principle](/oop/principle/) [OOP](/oop/)
