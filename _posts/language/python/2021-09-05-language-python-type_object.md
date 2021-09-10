---
title: "Type Object in Python"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/type_object/
last_modified_at: 2021-09-03T16:20:01+09:00

---

이전 글: [Object in Python](/language/python/object/)

<br>

## Type vs Object

파이썬에서 **type**과 **object**는 서로 비슷하면서 굉장히 햇갈리는 개념이다.
(굉장히 헷갈리니 이해할 때까지 이 글을 반복해서 읽는 것을 추천한다.)

1. python에서 모든 것은 object이다.
2. 모든 object는 type을 가진다.
3. 그런데 '모든 것'에는 type도 포함된다. 즉, type도 object이다. 이처럼 data type을 표현하기 위한 object들을 ***type object***라고 부른다.
4. 심지어 object 개념조차도 object이다.
5. 그러면 3에서 *type object*들은 object니깐 1, 2에 의해 type을 가진다.
6. 마찬가지로 4에서 `object` object도 type을 가진다.
7. 엥...??

### `object` object

위의 4번에 대한 답이 `object` object이다.
Python에서 모든 data를 object abstraction으로 나타내기 위해 `object`라는 데이터가 정의되어야 하고, 이는 당연히 규칙에 의해 object이다.

### `type` object

위의 5번에 대한 답이 `type` object이다.
`type` object는 *type object*들의 type에 대한 abstraction이다.
모든 *type object*들의 type은 `type` object 또는 `type` object를 base로 갖는 *type object*이고,
이렇게 *type object*들의 type을 나타내는 *type object*들을 **[metaclass](/language/python/metaclass/)**라고 한다.
당연히 `type` object도 metaclass이다.
같은 단어가 계속 반복돼서 너무 헷갈리니 ***plain text와 아닌 것을 잘 구분하자***.

```python
>>> type(int)
<class 'type'>
>>> type(float)
<class 'type'>
>>> type(type)
<class 'type'>
>>> type(object)
<class 'type'>
```

이처럼 `int`, `float` 등의 type이 `type` object인 것을 알 수 있다.
`type` object도 *type object*이므로, `type` object의 type은 `type` object이다.
(이게 무슨 말장난같은...)

### Getting Confused

슬슬 헷갈리기 시작한다. 심지어 아래 코드를 보면 더더욱 머리가 아플 것이다!

```python
>>> isinstance(type, type)
True
>>> isinstance(type, object)
True
>>> isinstance(object, type)
True
>>> isinstance(object, object)
True
```

뭐....라고??? `type`이 `object`의 instance이고 `object`가 `type`의 instance라고??
그럼 `type`과 `object`는 같은 것인가??

```python
>>> type is object
False
```

그건 아니라고??
심지어 `type`과 `object`는 각각 자기자신의 instance???
그럼 뭐야 대체??

### More Precise Definition of **Object**

파이썬의 모든 데이터를 나타내는 primitive abstraction인 [Object](/language/python/object/)의 정의는 이렇다.

## Two Primitive Objects

파이썬에서 기본이 되는 두 object(`type`, `object`)가 있다.
이 둘을 포함한 모든 object는 이 두 object와 관계가 있다.

- `object` object는 특별히 다른 *type object*를 base로 갖지 않는 *type object*들의 default base이다.
따라서 수학적 귀납법에 의해 모든 *type object*는 직접적 혹은 간접적으로 `object` object를 base로 갖는다.
당연히 `type` object도 *type object*이므로 `object` object를 base로 갖는다.
Base가 없는 유일한 *type object*는 `object` object이다.
- `type` object는 특별히 다른 *type object*를 type으로 갖지 않는 *type object*들의 type이다. 앞에서 이미 다뤘으니 넘어가...
기전에 `object` object도 *type object*라는 점을 짚고 넘어가자. `object` object는 object type을 표현하는 object인 것이다.

### `isinstance()` Function

`isinstance(arg1, arg2)` 함수는 `arg1` object가 `arg2` object 혹은 `arg2`의 subclass의 인스턴스인지,
즉 `arg1`의 type이 `arg2` 혹은 그 subclass인지를 return하는 함수이다.
어떤 object가 `arg2`의 object라는 것은 직간접적으로 이 object가 `arg2`를 base로 갖는다는 것을 의미한다.

- `isinstance(object, object)`는 `object` object의 type인 `type` object가 `object` object를 base로 갖기 때문에 `True`를 return한다.
- `isinstance(object, type)`은 `object` object의 type이 `type` object이기 때문에 `True`를 return한다.
- `isinstance(type, object)`는 `type` object의 type인 `type` object가 `object` object를 base로 갖기 때문에 `True`를 return한다.
- `isinstance(type, type)`은 `type` object의 type이 `type` object이기 때문에 `True`를 return한다.

### Class is Equivalent to Type

이쯤 되면 느끼겠지만 Python에서 type과 class는 동치이다.

```python
>>> class Temp:
...   pass
...
>>> type(Temp)
<class 'type'>
```

이처럼 class인 `Temp` object도 type이 `type` object인 *type object*이다.

<br>

다음 글: [Type in Python](/language/python/type/)

모든 글: [Python](/language/python/) [Language](/language/)
