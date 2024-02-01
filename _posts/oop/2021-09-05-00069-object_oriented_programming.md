---
title: Object Oriented Programming (OOP)
layout: single
categories:
  - Oop
permalink: /oop/69/
last_modified_at: 2024-02-01T16:06:03

---

## Imperative Programming

초창기 프로그램은 단순히 명령의 나열로, 명시된 순서대로 instruction을 수행한 후 결과를 내는 것이었다.
Assembly는 물론이고, C언어조차 goto를 이용했었다.
따라서 프로그래밍이란 어떤 알고리즘을 어떤 순서대로 써나가는 순차적 방식을 따랐다.

이런 방식은 알고리즘의 복잡도가 올라가고 코드가 길어질수록 가독성, 중복 등의 문제가 산적한 스파게티 코드가 되며,
유지보수에 심각한 문제를 초래한다.

## Procedural Programming

1968년 다익스트라가 프로그램을 프로시져 단위로 나누고 프로시져끼리 호출하는 구조적 프로그래밍 방식을 제안하였다.
프로그램을 작은 단위로 나누어 개발할 수 있어 모듈성의 증가로 이어졌다.
이는 프로그램을 여러 프로시져로 나눈 후 각 프로시져를 구현하는 top-down 방식이다.

## Object-Oriented Programming

기존의 방식들은 instruction 처리를 구조화하지만, 데이터에는 관심을 가지지 않는다.
OOP는 기존의 패러디임과 다르게 프로그램을 객체 단위로 구성하는 방식이다.
객체는 데이터(attribute)와 데이터의 행동 및 다른 객체와의 상호작용(method)을 묶어 하나의 개념으로 나타낸 것이다.
객체지향 방식은 먼제 객체를 정의한 후 객체들을 조합하여 프로그램을 만드는 bottom-up 방식이다.

## Why OOP?

OOP의 목표는 가독성과 재사용성이다.
객체를 통해 유연하고 쉽게 확장 가능한 코드를 만들어 유지보수를 쉽게 한다.

<br>

[Back](/oop/)