---
title: "NotImplemented"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/notimplemented/
last_modified_at: 2021-09-07T22:45:50+09:00

---

## `NotImplemented`: This Method is Not Implemented with These Operands

`NotImplemented` object가 뜻하는 바는 numerical method나 [rich comparison method](/language/python/special_methods/#Rich-Comparison)가 주어진 operand에 대한 연산을 지원하지 않는다는 것이다.
Python에서는 이 경우 `TypeError`를 발생시키지 않고 `NotImplemented`를 return하는데,
그 이유는 파이썬에서 연산자를 구현하는 방식 때문이다.

기본적으로 모든 이항연산자들은 left operand의 method 중 연산자에 대응하는 method를 호출한다.
예를 들면, `x + y`는 `x.__add__(y)`와 **거의** 같다.
즉, **다르다**.
연산자와 이에 해당하는 method가 다른 동작을 하는 경우는 `NotImplemented`를 리턴하는 경우이다.

연산자는 대응하는 method가 `NotImplemented`를 리턴할 경우,
`TypeError`를 발생시키기 전에 관련된 다른 method들도 테스트한다.
예를 들어, `x + y`에 해당하는 method는 `x.__add__(y)`도 있지만, `y.__radd__(x)`도 있다.
"관련된 다른 method"는 연산자마다 정해져 있다.
만약 모든 method들이 `NotImplemented`를 리턴한다면, 그제서야 `TypeError`를 발생시킨다.

```python
>>> x = [1, 2, 3]
>>> y = 2
>>> x * y
[1, 2, 3, 1, 2, 3]
>>> y * x
[1, 2, 3, 1, 2, 3] # ?????
```

`list * int`는 list의 concatenation으로 정의되었기 때문에 line 3~4는 당연한 결과이다.
그러나 `int * list`는 상식적으로 정의가 되지 않아야 하는데, 왜 `y * x`가 `x * y`와 같은 결과를 return하는 것일까??

```python
>>> x.__mul__(y)
[1, 2, 3, 1, 2, 3]
>>> x.__rmul__(y)
[1, 2, 3, 1, 2, 3]
>>> y.__mul__(x)
NotImplemented
>>> y.__rmul__(x)
NotImplemented
```

`y * x`를 했을 때, 먼저 `y.__mul__(x)`를 시도하고, 결과가 `NotImplemented`이기 때문에 이어서 `x.__rmul__(y)`를 시도하는 것이다.

<br>

모든 글: [Python](/language/python/) [Language](/language/)
