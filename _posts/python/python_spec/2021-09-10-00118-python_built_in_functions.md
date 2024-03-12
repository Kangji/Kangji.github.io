---
title: Python Built In Functions
layout: single
categories:
  - Python
  - Python Spec
tags:
  - Grammar
permalink: /python/python_spec/118/
last_modified_at: 2024-03-11T17:51:24

---

Python built-in function들을 살펴본다.
`open`, `exec` 등과 같이 systems programming에 관련된 내용은 제외했다.

## `abs(i)`

i의 절댓값을 구하는 함수. `i.__abs__()`를 호출한다.

## `aiter(it)`

Async iterable `it`의 `it.__aiter__()`를 호출하여 Async iterator를 return한다.

## `all(it)`

Iterable `it`의 element가 1개 이상 논리값이 거짓이면 False를, o/w True를 return한다.

## Awaitable `anext(it)`

Async iterator `it`의 `it.__anext__()`를 호출하여 coroutine을 return한다.

## `any(it)`

Iterable `it`의 element가 1개 이상 논리값이 참이면 True를, o/w False를 return한다.

## `ascii(obj)`

`repr(obj)`과 유사하나 non-ASCII를 `\U` 등으로 escape하여 return한다.

## `bin(obj)`

`obj.__index__()`를 호출하여 얻은 정수를 `0b`로 시작하는 binary string으로 변환한다. 

## Class `bool(obj)`

`bool` class를 호출하면 `obj`의 논리값을 return한다.
논리값은 다음 순서로 구한다.

1. `obj.__bool__()`을 구현하면 호출한 결과를 return한다.
2. `obj.__len__()`을 구현하면 `호출한 결과 > 0`을 return한다.
3. `True`를 return한다.

## `callable(obj)`

`obj`가 callable인지, 즉 `obj`의 type이 `__call__`을 구현하는지를 return한다.

## `chr(i)`

Unicode point `i`에 해당하는 string representation을 return한다.
예를 들어, `chr(97)`은 `'a'`, `chr(8364)`는 `'€'`. `ord()`의 inverse function이다.

유효한 범위는 0 ~ 1,114,111(0x10FFFF)이다.

## `delattr(obj, name)`

`obj.__delattr__(name)`를 호출하여 주어진 객체의 dictionary에서 해당 attribute를 삭제한다.
`del obj.name`과 같다.

## `dir(obj)`

`obj.__dir__()`를 호출하여 `obj`의 valid attribute list를 return한다.
이는 `obj`의 attribute dictionary 뿐만 아니라 access 가능한 모든 attribute이다.

## `divmod(a, b)`

`a.__divmod__(b)`를 호출하여 몫과 나머지를 return한다.

## `enumerate(it, start = 0)`

Iterable `it`의 각 element에 `start`부터 순서대로 번호를 붙인 tuple을 element로 가지는 iterator를 return한다.

## `filter(func, it)`

Iterable `it`의 element를 함수 `func`로 filtering한 iterator를 return한다.

## `format(value, format_spec='')`

`value`의 formatted representation, controlled by format_spec을 return한다.
f-string과 같다.

## `getattr(obj, name)`

`obj`의 attribute `name`을 lookup하는 함수. `obj.name`과 같다.

## `globals()`

Global namespace를 return하는 함수.

## `hasattr(obj, name)`

`getattr(obj, name)`의 성공 여부를 return하는 함수.

## `hash(obj)`

`obj.__hash__()`를 호출하여 hash-value를 구하는 함수.

## `hex(obj)`

`obj.__index__()`를 호출하여 얻은 정수를 `0x`로 시작하는 hex string으로 변환하는 함수.

## `id(obj)`

`obj`의 identity를 return하는 함수.

## `isinstance(obj, tp)`

`obj.__class__`가 `tp.__mro__`에 속하는지를 return하는 함수.
OOP 관점에서 `obj`가 `tp` 또는 그 superclass의 instance인지 여부.

## `issubclass(tp1, tp2)`

`tp2`가 `tp1.__mro__`에 속하는지를 return하는 함수.
OOP 관점에서 `tp1`이 `tp2`의 subclass인지 여부.

## `iter(it)`

Iterable `it`의 `it.__iter__()`를 호출하여 iterator를 return한다.

## `len(obj)`

`obj`의 `obj.__len__()`을 호출하여 길이를 return한다.

## `locals()`

현재 local scope의 namespace를 return한다.

## `map(func, it)`

Map-reduce의 Map. Iterable `it`의 각 element에 function `func`를 적용한 iterator.

## `max()`

Item들 중 최댓값을 return한다.

## `min()`

Item들 중 최솟값을 return한다.

## `next(it)`

Iterator `it`의 `it.__next__()`를 호출하여 다음 element를 return한다.

## `oct()`

`obj.__index__()`를 호출하여 얻은 정수를 `0o`로 시작하는 oct string으로 변환하는 함수.

## `ord(c)`

Unicode character `c`의 unicode point를 return하는 `chr()`의 역함수.

## `pow(base, exp)`

`base.__pow__(exp)`를 호출한다.

## `repr(obj)`

`obj.__repr__()`을 호출하여 객체의 printable representation을 담은 문자열을 return한다.
이 문자열의 내용이 interpreter에서 우리가 보는 것과 일치한다.
예를 들어 `s = 'hello'`면 s는 5글자 문자열이지만, interpreter는 `'hello'`로 보여주고,
`repr(s)`는 7글자 문자열 `'hello'`이다.

## `round(i)`

`i.__round__()`롤 호출하여 반올림한 결과를 return한다.

## `setattr(obj, name, value)`

`obj.__setattr__(name, value)`를 호출하여 object의 attribute를 set하는 함수.
`obj.name = value`와 같다.

## `sorted(it)`

Iterable `it`의 element를 정렬한 list를 return한다.

## `sum(it)`

Iterable `it`의 element를 모두 합한(`__add__`) 결과를 return한다.

## `vars(obj)`

`obj`의 writable attribute를 저장한 `obj.__dict__`를 return한다.

## `zip(*it)`

Iterable들의 각 element를 zip한 tuple을 element로 가지는 iterator를 return한다.

<br>

[Back](/python/python_spec/)