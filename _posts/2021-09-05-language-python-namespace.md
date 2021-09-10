---
title: "Python Namespace"
layout: single
categories:
  - Language
  - Python
permalink: /language/python/namespace/
last_modified_at: 2021-09-05T16:39:44+09:00

---

## Namespace란??

Namespace는 파이썬뿐만 아니라 C++ 등에서도 존재하는 개념으로, 변수 이름 String과 변수가 referencing하는 인스턴스를 각각 key, value로 저장한 dictionary이다.
모든 scope마다 namespace가 정의되어 있으며, 변수를 선언/대입/참조할 때마다 namespace를 확인하여 참조하게 된다.
값을 참조만 할 때는, 현재 scope의 namespace 뿐만 아니라 외부 scope의 namespace까지도 참조할 수 있다.

### Namespace 출력하기

- `globals()`: global namespace를 보여준다.
- `locals()`: 이 함수를 호출한 scope의 namespace를 보여준다.

### 선언/대입할 때

변수를 선언/대입할 때는 현재 scope만 참조한다. 현재 scope에 목표 변수가 정의되어 있지 않다면 현재 scope에 새롭게 정의한다.

```python
x = 3 # assign x = 3 in global namespace
def func():
    x = 4 # assign x = 4 in func namespace
    x = 5 # change x = 5 in func namespace
print(x) # x = 3 in global namespace
```

### 참조할 때

변수를 참조할 때는 현재 scope 및 상위 scope들의 namespace를 참조하게 된다.
만약 변수가 여러 namespace에 정의되어 있다면, 가장 가까운 scope의 것을 참조한다.

```python
x = 3 # assign x = 3 in global namespace
def func1():
    x = 4 # assign x = 4 in func1 namespace
    def func2():
        print(x) # use x = 4 from func1 namespace
```

<br>

모든 글: [Python](/language/python/) [Language](/language/)
