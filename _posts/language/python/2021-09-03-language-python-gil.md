---
title: "Global Interpreter Lock"
layout: single
categories:
  - Language
  - Python
tags:
  - CPython
permalink: /language/python/gil/
last_modified_at: 2021-09-03T03:42:37+09:00

---

## Global Interpreter Lock(GIL)

CPython은 내부적으로 reference counting과 garbage collection을 통해 자원을 관리한다.

### Reference Count

모든 instance는 **reference count**라는 필드를 가지는데, 이 인스턴스를 referencing하는 객체의 수를 센다.
따라서 객체가 생성되고 소멸할 때마다 그 객체가 referencing하는 모든 인스턴스의 reference count를 늘리거나 줄여야 한다.

### Garbage Collection

C에서는 dynamic allocation을 통해 user가 명시적으로 memory를 할당하거나 해제해주어야 하지만,
Java나 Python 등에서는 **garbage collector**라는 background thread가 주기적으로 reference count를 확인하고 불필요한 메모리를 해제해준다.

### Race Condition

Single threaded program에서는 문제가 없지만, multithreading에서는 이야기가 달라진다.
여러 thread에서 동시에 한 instance의 reference count를 건드리는 경우는 꽤 자주 있을 것인데,
이 경우 race condition이 발생한다.
따라서 이를 막기 위해서 모든 instance는 lock이 있어야 하는데, lock acquire와 release는 생각보다 computational cost가 크기 때문에,
결과적으로 엄청난 성능 저하를 유발하게 된다.
게다가 수많은 lock을 만들 경우, deadlock이 발생할 가능성이 높다.

### Conclusion

CPython은 이런 문제를 해결하기 위해 python interpreter 자체가 lock을 지니도록 하고, 각 thread가 실행되기 위해서는 반드시 이 lock을 잡아야 하도록 설계되었다.
이 lock이 바로 **GIL**이다.
GIL의 문제점은 multicore 환경에서 발생하는데, core가 여러 개여도 GIL 때문에 한 번에 한 thread만 수행될 수 있어서 성능 측면에서 큰 손해이다.
하지만 CPU bounded program이 아니라면 체감상 차이는 크지 않다.

<br>

모든 글: [Python](/language/python/) [Language](/language/)
