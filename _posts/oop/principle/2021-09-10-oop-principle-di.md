---
title: "Dependency Injection"
layout: single
categories:
  - OOP
  - OOP Principle
tags:
  - SOLID
permalink: /oop/principle/di/
last_modified_at: 2021-09-10T20:16:50+09:00

---

## Dependency란??

OOP에서 dependency란 객체 간의 종속성을 뜻한다.
A 객체가 B 객체에 종속적이라는 것은, B 객체가 A 객체에 대해 알고 있어야 한다는 뜻이다.
그리고 이런 식의 dependency는 OOP에서 반드시 **지양**해야 한다. 그 이유는, modularity를 해치기 때문이다.

```java
class Foo {
    final Bar bar;

    public Foo(final int barValue) {
        bar = new Bar(barValue);
    }
}

class Bar {
    final int barValue;

    public Bar(final int barValue) {
        this.barValue = barValue;
    }
}
```

이런 코드가 있다고 생각해보자. 이 때, `Foo` 객체는 `Bar` 객체에 대한 정보를 알고 있어야만 한다.
왜냐하면, Foo 내부에서 Bar의 생성자를 호출하기 때문이다.
만약 프로그램 스펙이 바뀌어서 `Bar` 객체에 `final int barKey`라는 field가 추가되고 생성자 또한 이에 맞게 수정된다면,
`Bar` class가 `Foo` class에 종속적이기 때문에 `Foo` class에도 수정이 이루어져야 한다.
간단한 프로그램에서는 괜찮지만, 이런 식의 dependency가 이리저리 얽히고 섥힌 프로젝트에서는 한 object를 수정하려고 할 때도 수많은 코드를 수정해야 할 수도 있다.

## Dependency Injection

이런 일을 방지하기 위해서 우리는 객체 간의 종속성을 깨주어야 하고, 좋은 방법이 DI라고 불리는 **Dependency Injection**이다.
DI는 말 그대로, 한 객체에 의존적인 객체를 외부에서 만들어서 주입해줌으로써 두 객체간의 의존성을 제거하자는 것이다.

DI를 만족하는 `Foo` class는 다음과 같아진다.

```java
interface BarInterface {
    public Value getBarValue();
    public Key getBarKey();
}

class Bar implements BarInterface {
    final Value barValue;
    final Key barKey;

    public Bar(final Key barKey, final Value barValue) {
        this.barKey = barKey;
        this.barValue = barValue;
    }

    public Value getBarValue() {
        return this.barValue;
    }

    public Key getBarKey() {
        return this.barKey;
    }
}

class Foo {
    final BarInterface bar;

    public Foo(final BarInterface bar) {
        this.bar = bar;
    }
}
```

이제, `Foo` class는 외부에서 `BarInterface`를 구현하는 class의 instance를 만든 후에 생성자의 argument로 넘겨줌으로써 `Bar` class에 대해 아무것도 몰라도 되고,
`Bar` class가 어떻게 수정되더라도 `BarInterface`를 구현하기만 한다면 아무 문제가 없다.

<br>

모든 글: [OOP Principle](/oop/principle/) [OOP](/oop/)
