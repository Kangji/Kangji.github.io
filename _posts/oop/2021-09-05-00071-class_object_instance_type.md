---
title: Class vs. Object vs. Instance vs. Type
layout: single
categories:
  - Oop
tags:
  - Language Theory
permalink: /oop/71/
last_modified_at: 2024-02-01T18:52:33

---

OOP에서 class, object, instance는 비슷한 개념으로 혼용되기 쉽다.
그리고 OOP와 Type Theory에서 class와 type도 혼용되기 쉽다.

## Object

OOP에서 객체는 실제 세상에 존재하는 개념을 code와 data로 표현해서 하나로 묶어 놓은 것이다.
OOP에서는 프로그램을 객체와 객체의 상호작용으로 구성한다.

## Class

클래스는 객체의 설계도(구현)이자 틀이며, encapsulation 그 자체이다.
표현하고자 하는 대상의 data/state(attribute)와 action(method)에 대한 정의를 담고 있다.

## Instance

인스턴스는 클래스를 통해 실체화시킨 객체이다.
모든 객체가 반드시 인스턴스는 아니지만 인스턴스는 객체이다.

## Example

```java
Person alice = new Person("alice");
Person bob = new Person("bob");
```

이 예시에서 `alice`와 `bob`은 모두 객체이며, `Person`이라는 클래스의 인스턴스이다.

## Class vs. Type

Class와 type이 혼용되는 경우는 대게 클래스를 객체의 type으로 오해하기 때문이다.
클래스 이름을 type으로서 사용할 뿐, class와 type은 엄연히 다르다.
Type은 인터페이스, 클래스는 type의 구현인 셈이다.

또한 대부분 언어에서 클래스가 아닌 primitive type들이 존재한다.

한편, type theory에 의하면 type은 모든 term에 assign된 분류로,
주로 각 term이 가질 수 있는 value에 따라 결정된다.
또한 type은 기반이 되는 type system에 따라 달라진다.

<br>

[Back](/oop/)