---
title: "Closure"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/closure/
last_modified_at: 2021-09-08T17:35:50+09:00

---

이전 글: [Metaclass](/language/python/metaclass/)

<br>

## First Class Object

OOP에서 first class object(일급 객체)란 다른 모든 entity에 통용 가능한 operation이 지원되는 entity를 말한다.
우리가 관심있는 first class object의 성질은 함수의 argument/return value로 쓰일 수 있다는 점이다.
파이썬에서 `function` type의 object들은 first class object이다.

## Closure

Closure의 정의는 자신을 둘러싼 scope의 state를 기억하는 함수이다.
이 조건을 만족하기 위해 closure는 다음과 같은 형태여야 한다.

```python
def outer_func(*args, **kwargs):
    def inner_func(*args, **kwargs):
        # do some business logic...
    return inner_func
```

### Nonlocal Scope

global scope는 어디에서나 접근 가능하다.
그렇기 때문에 closure를 둘러싼 scope를 기억하는 것이 의미를 갖기 위해서는 global이어서는 안된다.
즉, global도 local도 아닌 중간 단계의 scope(nonlocal이라고 부른다)가 필요하고, 최소 3개의 scope가 있어야 한다.
따라서 closure는 반드시 중첩된 형태여야만 하는 것이다.

### Free Variable

Closure는 nonlocal scope의 state를 기억한다고 했는데, 모든 걸 다 기억하는 건 아니다.
Closure에서 참조하는 변수들만 기억하고, 이를 **free variable**이라고 한다.
이전 글에서 `function` type인 object들의 special attribute 중 `__closure__`라는 것이 있었는데, 이 attribute가 free variable들을 referencing한다.
이렇게 closure가 free variable들을 referencing하기 때문에, 바깥 함수가 심지어 메모리에서 제거된다고 하더라도 free variable들은 사라지지 않는다.

## Usage of Closure

### Wrapping Function

```python
def customize(func):
    def wrapper(*args, **kwargs):
        print("start function")
        func(*args, **kwargs)
        print("end function")
    return wrapper

def myFunc(*args, **kwargs):
    # do some business logic
    ...

myFunc = customize(myFunc)
```

`customize` 함수의 인자로 임의의 함수를 넘기면 함수 실행 전후에 prompt를 출력해주는 wrapped function을 return해준다. 이런 식의 사용이 [decorator](/language/python/decorator/)의 원리이다.

### Memoization

```python
def memoization(func):
    cache = {}
    def wrapper(*args):
        if args not in cache.keys():
            cache[args] = func(*args)
        return cache[args]
        
def myFunc(*args):
    # do some business logic
    ...

myFunc = memoization(myFunc)
```

Nonlocal scope를 활용해서 memoization을 구현할 수 있다. 이제 myFunc는 `cache`라는 free variable에 argument와 그 return값을 저장하고, argument가 key에 있으면 함수를 수행하지 않고 곧바로 결과를 return한다.

<br>

다음 글: [Decorator](/language/python/decorator/)

모든 글: [Python](/language/python/) [Language](/language/)
