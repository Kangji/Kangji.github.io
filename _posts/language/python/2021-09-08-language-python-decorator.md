---
title: "Decorator"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/decorator/
last_modified_at: 2021-09-08T18:58:50+09:00

---

이전 글: [Closure](/language/python/closure/)

<br>

## Not Annotation

파이썬 코드를 보면 함수나 메소드 위에 `@property`처럼 annotate되어 있는 것을 본 적이 있을 것이다.
그러나 이것들은 Java의 annotation과는 다르다. 이들을 **decorator**라고 부른다.

## Decorator

Decorator의 동작 원리는 다음과 같다.

```python
@myDeco
def myFunc(*args, **kwargs):
    ...
```

위 코드는 아래 코드와 동치이다.

```python
def myFunc(*args, **kwargs):
    ...

myFunc = myDeco(myFunc)
```

여기서 우리는 decorator가 callable이어야 한다는 것을 알 수 있다.

## Usage

주로 decorator는 함수를 wrapping하는데 많이 사용한다. 이전 글에서 closure가 하는 일을 떠올려보라. Closure의 외부 함수를 decorator로 사용하면 된다.

Decorator를 이용할 경우, 코드의 반복을 피할 수 있고, 코드 은닉에도 도움이 된다.

## Implementation

### Closure

[Closure](/language/python/closure/)를 이용한 decorator의 구현 방법. 이전 글을 참고하라.

### Decorator Class

모든 object는 callable이기만 하면 decorator로 사용할 수 있기 때문에, `__call__()`을 구현하는 임의의 class의 instance는 decorator로 사용할 수 있다.

```python
class MyDeco:
    def __init__(self, *args, **kwargs):
        # customize free variables
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # do some business logic
            ret = func(*args, **kwargs)
            # do some business logic
            return ret
        return wrapper
```

이 때 `wrapper`가 closure이며, closure의 free variable은 `self`, 즉 `MyDeco` type의 object가 된다. 그리고 이 object는 `__init__` 덕분에 원하는대로 customizing이 가능해서 더욱 flexible한 decorator가 만들어진다.

### Example

```python
class TestFailException(Exception):
    pass

class RunWithTest:
    def __init__(self, expected_result):
        self._expected = expected_result
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if ret != self._expected:
                raise TestFailException
            return ret
        return wrapper

@RunWithTest(7)
def myFunc(x, y):
    return x + y
```

`RunWithTest(7)` decorator를 적용한 myFunc는 이제 단순 덧셈에 추가적으로
덧셈 결과가 7이 아닐 경우 `TestFailException`을 발생시키는 함수가 되었다.

내부 implementation을 살펴보자.

- line 16에서 decorator의 동작 원리대로 `myFunc = RunWithTest(7)(myFunc)`가 수행된다.
- `RunWithTest(7)`이 먼저 수행된다. 이 결과 `_expected = 7`인 `RunWithTest` type의 object가 만들어진다.
- 그 다음 만들어진 object가 호출되는데, 이 때 이 object의 type인 `RunWithTest` object에서 `__call__(created_anonymous_object, myFunc)`의 return값이 myFunc가 된다.
- `__call__`의 내부 구현에 따르면 `wrapper` closure가 myFunc가 된다.

## Conclusion

Decorator는 간편하고, 활용도가 높으며, 강력하다. 그러나 작동 원리에 대한 수준 높은 이해가 동반되어야 할 것이다.
애초에 파이썬 언어 특성 자체가 high flexibility, low accessibility라고 생각해서...

<br>

다음 글: [Descriptor](/language/python/descriptor/)

모든 글: [Python](/language/python/) [Language](/language/)
