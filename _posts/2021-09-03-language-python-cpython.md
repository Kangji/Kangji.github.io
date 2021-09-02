---
title: "CPython"
layout: single
categories:
  - Language
  - Python
tags:
  - CPython
permalink: /language/python/cpython/
last_modified_at: 2021-09-03T02:52:37+09:00

---

## CPython이란??

CPython은 Python의 [구현체](/language/programming_language/0/#언어-구현체language-implementation) 중 가장 처음 만들어진 구현체이자 가장 널리 쓰이는 구현체이다.
사실 CPython과 PyPy외에는 거의 쓰이지 않고, CPython이 default implementation이기도 하다.
따라서 파이썬의 구현에 대해 공부한 것들은 전부 CPython이라고 봐도 된다.
CPython은 C언어로 쓰여졌는데, 이 때문에 Python이 C로 구현됐다고 알려지기도 했다.

### CPython 구조

CPython은 Java 프로그램의 실행과정과 유사하게 동작한다.
CPython은 compilation과 interpretation을 모두 하는데, Python 코드를 bytecode로 compile하고 나서 이를 실행(interpretation)하기 때문이다.
`.pyc` 파일들이 compile된 bytecode들이다.
