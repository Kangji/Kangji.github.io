---
title: "Object in Python"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/object/
last_modified_at: 2021-09-05T14:29:50+09:00

---

## Everything is Object

파이썬에서는 모든 것이 객체라는 말을 들어봤을 것이다.
이 말의 뜻은 정확히는 파이썬에서 데이터를 표현하는 기본 abstraction이 객체라는 단위이고,
모든 데이터가 객체 또는 객체 사이의 관계로 나타내어진다는 말이다.
즉, 정수도, 클래스도, 인스턴스도 모두 다 객체이다. 그리고 어떤 의미에서는 파이썬 코드 또한 객체이다.
클래스, 인스턴스, 객체가 혼동된다면 이 글을 먼저 읽고 오자.

[Class vs. Object vs. Instance](/oop/general/class_object_instance/)

## Components of Object

파이썬의 모든 객체는 **Identity**, **Type**, **Value**, 그리고 0개 이상의 **Base**를 가진다.

### Identity

Identity는 모든 인스턴스가 가지는 고유한 불변의 정수이다.
`id()` 함수가 객체의 identity를 return한다.
한편, CPython에서는 인스턴스의 메모리 주소를 identity로 사용한다.
그리고 `is` operator는 두 인스턴스의 identity를 비교한다.

### Type

모든 객체는 불변 속성인 [type](/language/python/type/)을 가진다.
객체의 type은 어떤 연산을 지원할지 결정하고, 객체가 가질 수 있는 Value를 정의한다.
`type()` 함수가 객체의 type을 return한다. 이 함수는 단순히 모든 object가 가지고 있는 special attribute인 `__class__`가 referencing하는 객체를 return한다.
이 때, return값 또한 객체([type object](/language/python/type_object/))이다.

### Value

모든 객체는 값(value)을 가지고, 값은 가변(mutable) 혹은 불변(immutable)이다.
한편, 가변 객체를 referencing하는 불변 객체의 경우 불변임에도 불구하고 내용물은 바뀔 수 있다(changeable).
앞서 type이 객체가 가질 수 있는 value를 정의한다고 했는데, 객체의 불변성 또한 type에 따라 결정된다.

맨 처음에 정수도 객체라고 했는데, 정수 2를 생각해보자. 이 객체는 value가 `2`인 한 객체일 뿐이다.
![dir_of_2](/assets/images/language/python/dir_of_2.png)
이처럼 `2`라는 객체 또한 수많은 attribute를 가지고 있다.

### Base

Base는 OOP에서 superclass와 거의 유사한 개념이다.
모든 object는 0개 이상의 base를 가질 수 있는데, 이 말은 다중상속이 가능하다는 뜻이다.
다중상속이 가능한 이유는 파이썬에서 상속은 class object끼리의 관계로 나타내어지기 때문이다.
기본적으로 base는 class의 성질이기 때문에 [type object](/language/python/type_object/)들만 base를 가질 수 있다.
Base들은 type object들이 가지고 있는 special attribute인 `__bases__`에 tuple로 저장된다.

```python
>>> x = 3
>>> x.__base__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute '__base__'
```

### Name of an Object

그리고 한 가지 중요한 사실은 일반적으로 object의 이름은 object의 일부가 아니다.
Object의 이름은 [namespace](/language/python/namespace/)에 {"object name": class object}로 저장되어 있는 외부 성질이다.
하지만 class, function, method 등등의 경우 `__name__`이라는 special attribute에 object의 이름이 저장된다.

<br>

다음 글: [Type Object in Python](/language/python/type_object/)

모든 글: [Python](/language/python/) [Language](/language/)
