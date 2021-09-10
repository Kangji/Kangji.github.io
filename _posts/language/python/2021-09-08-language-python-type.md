---
title: "Python Built-in Types"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/type/
last_modified_at: 2021-09-08T04:45:37+09:00

---

이전 글: [Type Object in Python](/language/python/type_object/)

<br>

## object & type

`object`와 `type`은 앞에서 언급했으므로 생략

## NoneType

파이썬에서는 C/C++나 Java의 `null`과 같은 역할을 하는 `None`이라는 object가 있는데, 이 object의 type이 `NoneType`이다.
추가적으로 파이썬에는 `void` type이 없기 때문에 리턴값이 없는 메소드나 함수는 모두 `None` object를 리턴한다.

```python
>>> type(None)
<class 'NoneType'>
>>> type(NoneType)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'NoneType' is not defined
```

그런데, `NoneType` object를 확인하려고 보니 정의되어있지 않단다. 엥???
이 현상은 [namespace](/language/python/namespace/) 때문에 일어나는 일이다.
`None` object의 `__class__` attribute가 `NoneType` object를 가리키고 있지만,
`'NoneType'`이라는 이름으로 namespace에 등록되어 있지 않기 때문에 line 4~6과 같은 에러를 마주하게 된다.

```python
>>> type(type(None))
<class 'type'>
```

이런 꼼수를 사용하면 `NoneType` object의 type이 `type` object라는 것을 알 수 있다.
어쨌든 파이썬에는 `NoneType`이라는 type이 존재하고, type이 `NoneType`인 object는 `None` object가 유일하다.

## NotImplementedType

`None` object와 비슷한 느낌을 풍기는 [`NotImplemented`](/language/python/notimplemented/)라는 object도 있다. 이 object의 type은 `NotImplementedType`이다.
마찬가지로 type이 `NotImplementedType`인 object도 `NotImplemented` object가 유일하다.
말 그대로 구현되지 않음을 표현하는 객체이다.

## ellipsis

파이썬에서 `...`을 `Ellipsis`라고 한다. `...`의 사용법은 다음과 같다.

- `pass` 대신 사용
- type hinting에서 "any type"이란 뜻으로 사용
- `NumPy` 등에서 `:`과 같은 의미로 사용

`...`의 type이 바로 `ellipsis` object이다(대문자 아님).
마찬가지로 type이 `ellipsis`인 object도 `Ellipsis`(또는 `...`)가 유일하다.

## Numeric Types

Numeric type들은 수를 나타내는 객체들을 표현하는 type들의 분류이다.
모든 numeric type들의 instance들은 불변이다.

### float

파이썬에서 `float`의 machine level 구현은 기본적으로 double-precision이다.

### complex

복소수. `complex`는 machine level에서 단순히 두 double-precision 부동소수로 이루어져 있다.
이 말을 `complex`의 instance가 attribute로 두 `float` type instance를 가진다고 착각하면 안 된다.
`z.real`, `z.imag`로 `z`의 실수부와 허수부에 해당하는 `float` type 객체를 얻을 수 있다.

### Integral Types

#### int

다른 언어들이 data size별로 여러 정수 type을 가지고 있는 것과는 달리 파이썬은 `int` 단 하나만 가지고 있다.
`int`는 무한대의 범위를 표현할 수 있다. (정확히는 Virtual Memory가 허용하는 범위까지)
이게 가능한 이유는 모든 것이 object이기 때문이다.

당연하지만, 2's complement로 정수를 표현한다.

#### bool

참 또는 거짓을 나타내는 type이다. Type이 `bool`인 object는 `True`와 `False` 단 두 개 뿐이다.

## Sequence Types

파이썬에서 sequence라고 부르는 type들은 **finite ordered set of objects indexed by non-negative numbers**를 표현하는 *type object*들이다.
`len()` 함수를 통해 길이를 알아낼 수 있고, slicing이 가능하다.
Type이 sequence type에 속하는 object들은 불변일수도, 가변일수도 있다.

### Imutable Sequence Types

#### str

익숙한 `str` *type object*이다.

#### tuple

익숙한 `tuple` *type object*이다.

#### bytes

`str` object와 상당히 유사하다. Machine-level에서 보면 array of 8-bit bytes이다.
Type이 `bytes`인 literal들은 `b'abc'`처럼 표현한다.
`decode()` 함수를 통해 같은 내용의 `str` type인 object를 얻을 수 있다.

### Mutable Sequence Types

#### list

익숙한 `list` *type object*이다.

#### bytearray

가변인 점을 제외하면 `bytes` object와 일치한다.

## Set Types

Set이라고 불리는 *type object*들은 **finite unordered set of unique, immutable objects**를 표현하는 *type object*들이다.
순서는 없지만 `len()`도 사용 가능하고, iterable하다.

### set

익숙한 `set` *type object*이다.

### frozenset

불변인 점을 제외하면 `set` object와 거의 일치한다.
심지어 hashable이기 때문에 dictionary key로도 사용 가능하다.

## Mapping Types

### dict

`key: value` pair를 담고 있는 object를 나타내는 *type object*이다.
key는 immutable object만 사용할 수 있고, key의 검색은 hash값을 사용하기 때문에 O(1)이다.
가변이고, pair가 들어온 순서를 보존한다.

### mappingproxy

`mappingproxy` type은 `__setattr__`이 없는 것을 제외하고 `dict` type과 동일하다.

## Callable Types

호출할 수 있는 object들을 표현하는 *type object*들의 분류이다.
엄밀히 따지면 모든 *type object*들은 그들의 type 또는 그 상위 type인 `type` object가 `__call__()`을 구현하므로 callable이지만,
우리가 관심있는 것은 user defined function, built-in function, method 등이다.
참고로, 어떤 object를 호출한다는 것은 그 object의 type의 `__call__()`을 호출하는 것이다.

### function

`function` object는 `def` keyword를 이용해 정의한 모든 **user-defined function**들의 type이다.
그리고 **global namespace에 없다**. (하지만`types` 모듈에서 찾아볼 수 있다...)

`function` type의 object들은 여러 가지 special attribute들을 가지는데, 아래 예시와 함께 살펴보자.

```python
>>> def myAdd(x: int, y: int, z=3, *args, w=4) -> int:
...     """Custom addition function."""
...
...     return x + y + z + w + sum(args)
...
>>> myAdd.func_attr = 7
>>>
>>> # line separator #
>>>
>>> myAdd.__annotations__
{'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
>>> myAdd.__class__
<class 'function'>
>>> myAdd.__closure__
>>> myAdd.__code__
<class 'code'>
>>> myAdd.__defaults__
(3,)
>>> myAdd.__kwdefaults__
{'w': 4}
>>> myAdd.__dict__
{'func_attr': 7}
>>> myAdd.__doc__
'Custom addition function.'
>>> myAdd.__globals__
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'myAdd': <function myAdd at 0x7f8c002201f0>}
>>> myAdd.__name__
'myAdd'
>>> myAdd.__qualname__
'myAdd'
>>> myAdd.__module__
'__main__'
```

- line 10 ~ 11: `__annotations__`는 line 2의 annotation str이다.
- line 12 ~ 13: `myAdd` object의 type이 `function` object인 것을 알 수 있다.
- line 14: `__closure__`는 [closure](/language/python/closure/)의 free variable들을 tuple of `cell` typed objects로 표현한 것이다.
`cell` object는 `__closure__`에서 free variable을 표현하기 위한 *type object*로, python3.8에 새롭게 추가됐다. 아직까지 별 기능은 없는 듯 하다.
`cell` object는 global namespace에 없지만 역시나 `types` 모듈에서 찾아볼 수 있다.
`myAdd`는 closure가 아니라서 `None`이다.
- line 15 ~ 16: `__code__`는 `code` type의 object인데, object의 bytecode이다.
`code` object도 global namespace에 없고 `types` 모듈에서 찾아볼 수 있다.
- line 17 ~ 20: `__defaults__`는 default argument들을 tuple로 저장하고,
`__kwdefaults__`는 **keyword-only parameter**들과 default value를 dictionary로 저장한다.
keyword-only parameter는 line 1에서 `*args` 다음에 나오는 parameter들이다.
- line 21 ~ 22: `__dict__`는 `function` type의 object들 뿐만 아니라 모든 object에 다 있는 special attribute이다.
Object의 writable attribute들을 dictionary로 저장한다.
- line 23 ~ 24: `__doc__`는 주석이다.
- line 25 ~ 26: `__globals__`는 `myAdd` object를 가지고 있는 namespace이다.
- line 27 ~ 30: `__name__`은 object의 이름이다. `__qualname__`은 hierarchy를 포함한 이름이다.
- line 31 ~ 32: `__module__`은 `myAdd` object가 만들어진 module의 이름이다.

### method

`method` object는 모든 **instance method**와 **[class method](/language/python/class_static_instance_method/)**들의 type이다.
Instance method는 class instance의 method이다.

```python
>>> class Temp:
...     def foo(self):
...         pass
...
>>> x = Temp()
>>> type(Temp.foo)
<class 'function'>
>>> type(x.foo)
<class 'method'>
>>> x.foo
<bound method Temp.foo of <__main__.Temp object at 0x7fa46001da30>>
```

왜 `Temp.foo`의 type은 `function` object이고 `x.foo`의 type은 `method` object일까?
`Temp.foo`는 `Temp` object의 `function` type attribute이고,
`x.foo`는 `x` object의 **`method`** type attribute이기 때문이다.

line 1 ~ 3에서 `Temp` class를 정의할 때 `Temp` object가 생성된다.
이 때 `Temp` object의 attribute로써 `function` type의 `foo` object도 같이 생성된다.
반면 line 5에서 `Temp` type의 `x` object가 생성될 때 `x`의 attribute로써 `foo` object도 같이 생성된다.
line 10 ~ 11을 보면 `x.foo`가 **bound method**라고 하는데, 이처럼 모든 `method` type의 object는 한 object에 bounded이다.
Class instance가 생성될 때 `Temp` object에 접근해서 attribute들 중에 `function` type의 object가 있으면,
해당 object와 class instance, class object를 묶어서 `method` object를 생성한다.
따라서 `x.foo`는 `x`, `Temp`, `Temp.foo`에 종속적이다(bounded).

`Temp` object의 attribute들 중에 `method` type의 object가 있을 수도 있는데(class method가 이렇다),
이 때 대응하는 `x`의 attribute는 새로운 `method` type의 object를 만들지 않고 그냥 그 object가 된다.
(예를 들어 그 attribute 이름이 `bar`라고 하면 `Temp.bar`와 `x.bar`가 동일한 object)

```python
>>> x.foo.__func__
<function Temp.foo at 0x7fa260260310>
>>> type(x.foo.__self__)
<class '__main__.Temp'>
```

`method` type인 object들의 중요한 special attribute는 `__func__`와 `__self__`이다.
`__self__`는 class instance를, `__func__`는 method가 가지고 있는 `function` type의 object를 가리킨다.
`method` type인 object에서 `function` type인 object들의 special attribute들도 대부분 지원하는데,
거의 전부가 다 단순히 `function` type인 object들의 special attribute를 그대로 가리키고 있다.

`method` object의 `__call__()`은 wrapper라고 볼 수 있다.
`method` object가 가지고 있는 function의 `__call__()`을 호출하면서, 첫 번째 인자로 `__self__`를 넘긴다.
그래서 `x.foo()`를 호출하는 것과 `Temp.foo(x)`를 호출하는 것은 사실상 동일하다.
그래서 python은 관습적으로 코드를 작성할 때 class 안에서 function의 첫 번째 argument를 `self`라고 하는 것이다.

### builtin_function_or_method

`builtin_function_or_method` object는 `len()`, `globals()` 등등 built-in function들의 type이다.
이와 동시에 `list`, `dict` 등의 built-in type의 object들의 method들도 `builtin_function_or_method` type의 object들이다.

```python
>>> type(len)
<class 'builtin_function_or_method'>
>>> myList = list()
>>> type(myList.append)
<class 'builtin_function_or_method'>
>>> type(list.append)
<class 'method_descriptor'>
```

위 예시에서 `list.append` object의 type이 `method_descriptor`임을 알 수 있다.
Descriptor에 대해서는 향후 포스팅에서 다루겠다.

### Type Objects

*type object*의 instance가 만들어지는 과정은 다음과 같다.

```python
class MyClass:
    def __init__(self, x):
        self.x = x

myClass = MyClass(3)

>>> type(myClass)
<class '__main__.MyClass'>
>>> type(MyClass)
<class 'type'>
```

앞에서도 계속 언급했지만, 모든 *type object*들은 `type` object 또는 `type` object를 base로 하는 *type object*들을 type으로 갖는다.
line 5를 실행하면 MyClass의 type인 `type` object의 `__call__(MyClass, 3)`이 호출된다.
이어서 `__call__(MyClass, 3)`은 `instance = MyClass.__new__(MyClass, 3)`을 호출해서 instance를 생성하고,
`MyClass.__init__(instance, 3)`을 호출해서 `instance`를 customize한 후 `return instance`한다.

`MyClass`가 `__call__()`을 구현한다면 `myClass`도 callable이 된다는 것을 알 수 있을 것이다.

## module

Module은 파이썬 코드의 기본 단위이다. 이런 module이라는 abstraction을 표현한 type이 `module` object이다.
`module` type의 object들은 `__dict__`가 dictionary로 표현된 namespace를 가리키고 있다.

## Internal Types

Python interpreter가 내부적으로 사용하는 몇몇 type들이 user에게도 노출되어 있다.

### code

대표적인 것이 `code` object이다. 앞에 설명했으니 넘어가자.

### traceback

Exception이 발생했을 때 stack trace를 나타내는 object들의 type이 `traceback` object이다.

### slice

`1:2:3` 처럼 배열의 indexing에 사용되는 object들의 type이 `slice` object이다.
`start`, `step`, `stop`으로 이루어져 있다.

### method-wrapper

```python
>>> type(object.__call__)
<class 'method-wrapper'>
```

이게 뭘까?? `method-wrapper`type은 CPython 내부적으로 사용하는 type으로, C로 구현된 함수를 wrapping한다.
`method` type과의 차이는 wrapping하는 대상이 파이썬 함수인지 C 함수인지이다. Wrapping 방식은 똑같다.

<br>

다음 글: [Metaclass](/language/python/metaclass/)

모든 글: [Python](/language/python/) [Language](/language/)
