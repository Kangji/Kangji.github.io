---
title: "TDD"
layout: single
categories:
  - Dev
  - Test
permalink: /dev/test/tdd/
last_modified_at: 2021-09-12T05:49:50+09:00

---

## Test Driven Development

개발 전에 먼저 테스트 코드를 작성하는 개발 패러다임을 **TDD(Test Driven Development)**라고 한다.
TDD는 세 단계로 이루어져 있다.

### 1. Test Code 작성

이 때는 코드가 아직 구현되지 않았기 때문에, 당연히 test가 실패한다. 이 상태를 **Red**라고 한다.

### 2. Test를 통과하도록 코드를 구현

TDD에서는 테스트가 잘 작성되었다는 가정 하에, test만 통과하면 코드는 맞는 코드이다. 이 상태를 **Green**이라고 한다.

### 3. Refactoring

하지만 이 상태의 코드는 굉장히 지저분한 상태이기에 refactoring 과정을 반드시 거치게 된다.
Refactoring 후 여전히 green 상태라고 장담할 수 없고, 다시 red로 돌아갔을 가능성이 꽤 크다.

따라서 step 1부터 3가 계속 사이클처럼 돌아가게 되는 것이다.

## Decoupling of Business Logic and Test

테스트 코드를 작성할 때 구현에 의존적이면 안 된다.
구현 후 테스트 코드를 작성하는 경우 이미 개발자가 내부 구현을 온몸으르 다 느낀 후라서 구현의 특이성을 자연스럽게 테스트코드에 반영하게 될 가능성이 매우 높다.
따라서 개발 하기 전에 먼저, 내부 로직이 blackbox인 채로 최대한 많은 input과 output들만으로 test code를 작성하자.
