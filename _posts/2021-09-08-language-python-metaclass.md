---
title: "Metaclass"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/metaclass/
last_modified_at: 2021-09-08T15:41:50+09:00

---

이전 글: [Python Built-in Types](/language/python/type/)

<br>

## Type of Type

이전 글에서 말한 것 처럼 metaclass는 *type object*의 type을 나타내는 *type object*이다.
`type` object는 metaclass이고, `type` object를 base로 하는 모든 *type object*는 metaclass이다.

## How to Set Metaclass

Class를 정의할 때 base를 적는 부분에 metaclass를 표시해준다.
그러면 표시해준 object가 type이 된다.
모든 *type object*의 default type이 `type` object이므로 default metaclass는 `type` object라고 할 수 있다.

```python
import abc
class Temp(metaclass=abc.ABCMeta):
    pass

>>> type(Temp)
<class 'abc.ABCMeta'>
```

## Construction of Instance

```python
class Temp:
    def __init__(self):
        print("Temp.__init__ called")

x = Temp() # What are called here??
```

line 5는 `Temp.__class__.__call__(Temp)`와 같다. 그러면 `type` object의 내부 구현을 보자.
(동작 방식대로 코드를 쓴 것일 뿐, 실제 구현체와는 다를 수 있다.)

```python
class type:
    def __call__(cls, *args, **kwargs):
        return cls.__new__(cls, *args, **kwargs).__init__(*args, **kwargs)
```

`type.__call__(Temp)`는 `Temp.__new__()`로 `Temp`의 instance를 만들고, `instance.__init__()`으로 초기화한다.
따라서 `type` object 대신 `__call__` 부분을 customize한 다른 metaclass를 사용한다면 instance 생성 과정을 다르게 만들 수 있다.

## Example: Singleton Pattern

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in SingletonMeta._instances:
            SingletonMeta._instances[cls] = type.__call__(cls, *args, **kwargs)
        return SingletonMeta._instances[cls]

class MyClass(metaclass=SingletonMeta):
    pass

>>> a = MyClass()
>>> b = MyClass()
>>> id(a)
140468114365888
>>> id(b)
140468114365888
```

이렇게 `__call__`이 이미 호출된 적이 있으면 최초 호출시에 생성한 instance를 return하기 때문에,
`SingletonMeta`의 instance는 Singleton이 된다.

<br>

다음 글: [Closure](/language/python/closure/)

모든 글: [Python](/language/python/) [Language](/language/)
