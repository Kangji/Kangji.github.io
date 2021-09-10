---
title: "Class, Static, Instance Method"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/class_static_instance_method/
last_modified_at: 2021-09-10T19:53:50+09:00

---

이전 글: [Descriptor](/language/python/descriptor/)

<br>

## Class, Static, Instance Method

OOP를 경험해본 대부분 사람들은 static method와 instance method의 차이를 잘 알고 있을 것이다.
그런데 파이썬에는 class method라는 개념이 하나 더 있다.
class method는 static method와 유사하지만, 그 차이점을 분명히 알아야 한다.

## Instance Method

Instance method는 우리가 흔히 알고 있는 그 method이다.
Class를 정의할 때 해당 class의 namespace에 있는 함수를 wrapping하는 `method` type의 object들이 이것이다.
Instance method는 내부적으로 binding되어 있는 instance와 그 type, wrapping하는 function을 referencing하고 있다.

```python
class method:
    def __call__(self, *args, **kwargs):
        return self.__func__(self.__self__, *args, **kwargs)
```

`method` object의 `__call__`이 이처럼 구현되어 있기 때문에 method를 호출하면 자연스럽게 function이 호출되고 첫 번째 인자로 instance가 들어간다.

## Static Method

OOP에서 Static method는 instance가 아닌, class에 종속된 method를 말한다.
파이썬에서 모든 것은 object이기 때문에 `staticmethod` object도 존재한다. 그리고 당연하겠지만 `staticmethod` object는 *type object*이다.

Class에서 static method를 만들 때 `@staticmethod`라는 [decorator](/language/python/decorator/)를 사용하는데,
해당 class의 namespace에서 정의된 함수를 wrapping하는 `staticmethod` type의 object를 만든다.
그리고 `staticmethod`는 [descriptor](/language/python/descriptor/)라서 이 attribute를 lookup할 때 `staticmethod` object에 정의된 `__get__`이 호출된다.

```python
class staticmethod:
    def __init__(self, func):
        self.__func__ = func
    
    def __get__(self, obj, objtype=None):
        return self.__func__

class Foo:
    @staticmethod
    def bar(x, y):
        return x + y

x = Foo()

>>> x.bar(3, 4)
7
>>> Foo.bar(3, 4)
7
```

`Foo` object의 namespace에 `function` type의 `bar` object가 생성되고,
`@staticmethod` decorator에 의해 `staticmethod(bar)`가 호출되어 `staticmethod` type의 object가 생성되고,
`bar`가 이 object로 re-mapping된다.

그런 다음 `x.bar` 또는 `Foo.bar`를 호출했을 때, `__getattribute__`로 찾아낸 object가 descriptor이기 때문에 이 object의 `__get__`까지 호출된다.
그런데 `staticmethod` object의 `__get__`을 보면 받는 인자에 관계없이 처음 생성했던 `function` type의 object가 return되는 것이다.
따라서 instance method와는 달리, `x.bar`나 `Foo.bar` 둘 다 **`Foo` object의 scope**에서 정의되었던 `function` type의 object이다.

## Class Method

Python에서 class method는 static method와 비슷한 개념이지만 구현이 달라서 동작이 조금 다르다.
마찬가지로 `classmethod`라는 *type object*가 있고, 이 또한 descriptor이다.
`@classmethod` decorator를 사용하면 `classmethod` type의 object가 생성되는데, 내부에 원래 `function` type의 object를 담고 있고,
`__get__`에서 원래 함수와 class object를 가지고 `method` object를 생성해서 return한다.
즉, class method는 class object가 가지고 있는 method라고 생각하면 된다. (이래서 static method와 비슷한 개념으로 사용된다)
그리고 method 호출 시 함수의 첫 번째 인자로 instance가 아닌 class object를 넘겨준다.

```python
class Foo:
    x = 3
    y = 4

    @classmethod
    def bar(cls):
        return cls.x + cls.y

a = Foo()

>>> a.bar()
7
>>> Foo.bar()
7
```

하지만 보면 알겠듯이 static method와 syntax가 엄연히 달라서 잘 알고 사용해야 한다.

<br>

다음 글: [Slot](/language/python/slot/)

모든 글: [Python](/language/python/) [Language](/language/)
