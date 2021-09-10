---
title: "Descriptor"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/descriptor/
last_modified_at: 2021-09-10T03:52:50+09:00

---

이전 글: [Decorator](/language/python/decorator/)

<br>

## Descriptor란?

Descriptor는 `__get__`, `__set__` 혹은 `__delete__` 중 적어도 한 개 이상을 구현하고 있는 class의 object를 뜻한다.

## Attribute Lookup

파이썬에서 dot operation으로 object의 attribute에 접근할 때, 내부적으로는 special method들을 이용한다.

```python
instance.attribute
# is actually
type(instance).__getattribute__(instance, 'attribute')

instance.attribute = value
# is actually
type(instance).__setattr__(instance, 'attribute', value)

del instance.attribute
# is actually
type(instance).__delattr__(instance, 'attribute')
```

그런데 이 method들은 각각 내부적으로 `type(instance.attribute)` object가 `__get__`, `__set__`, `__delete__` 메소드를 가지고 있는지 확인한 후, 있으면 호출한다.
따라서 우리는 descriptor를 이용하면 attribute로의 접근을 customize할 수 있다.

### Prototype

```python
__get__(self, obj, objtype=None)
__set__(self, obj, value)
__delete__(self, obj)
```

`__getattribut__`에서 `__get__`은 `instance`가 *type object*인지 아닌지에 따라 넘기는 인자가 달라진다.
*type object*가 아니면 `obj` = `instance`, `objtype` = `type(instance)`이다.
그런데 *type object*이면 `obj` = `None`, `objtype` = `instance`이다.

## Type of Descriptors

`__set__`나 `__delete__`를 구현하면 **data descriptor**, 그렇지 않으면 **non-data descriptor**라고 한다.

## Usage

### Dynamic Lookup

동적으로 값이 계속 바뀌는 attribute를 만들고 싶을 때 사용할 수 있다.

```python
class AttributeCount:
    def __get__(self, obj, objtype=None):
        return len(obj.__dict__)
    
    def __set__(self, obj, value):
        raise AttributeError

class MyClass:
    num_attr = AttributeCount()

a = MyClass()

>>> a.num_attr
0
>>> a.x = 3
>>> a.num_attr
1
```

line 15에서 `x`라는 attribute가 새로 생겨서 `a`의 `__dict__`에 추가되었다. 그래서 그 다음 줄에서 `num_attr` 값이 커졌다.

### Validator

`__set__`에서 유효성 검사 logic을 넣어줄 수 있다.

## Property Decorator

`property`라는 *type object*가 있는데, `property` object는 descriptor이다.

```python
class Foo:
    def __init__(self, x):
        self._x = x
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

a = Foo(3)

>>> a.x
3
>>> Foo.x
<property object at 0x7ff0981bed60>
```

이런 클래스가 있을 때, `@property`가 x를 decorating하므로 Foo.x는 기존 함수 `Foo.x(self)`를 wrapping하는 `property` type의 object가 되었다.
그리고 아래 코드는 `property` class를 python code로 표현해본 것이다. (실제로는 C로 구현되어 있다.)

```python
class property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)
    
    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)
    
    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)
    
    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)
    
    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
```

<br>

다음 글: [Class, Static, Instance Method](/language/python/class_static_instance_method/)

모든 글: [Python](/language/python/) [Language](/language/)
