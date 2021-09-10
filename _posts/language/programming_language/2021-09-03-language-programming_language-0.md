---
title: "프로그래밍 언어란"
layout: single
categories:
  - Language
  - Programming Language
permalink: /language/programming_language/0/
last_modified_at: 2021-09-03T02:37:05+09:00

---

## 프로그래밍 언어 되돌아보기

프로그래밍 언어가 컴퓨터를 돌리기 위한 것이라고 생각하기 쉽다.
하지만 역사적으로 보면 프로그램을 돌리기 위해 만들어진 것이다.
수학자들이 **기계적으로 계산 가능한 함수**를 정의하는 과정에서 프로그래밍 언어의 개념이 등장했다.
프로그래밍 언어를 고안해서 이 언어로 정의될 수 있는 것들을 "기계적으로 계산 가능한 함수"라고 제안했다.
그리고 이 함수들을 기계적으로 빠르게 계산하기 위해 등장한 기계가 바로 컴퓨터이다.
눈치가 빠르다면 소프트웨어나 프로그램의 실체가 "기계적으로 계산 가능한 함수"라는 것을 깨달았을 것이다.
그리고, 모든 소프트웨어나 프로그램은 언어를 기반으로 한다.

## 컴퓨터의 역사

컴퓨터의 시작은 1930년대로 거슬러 올라간다.

### Turing Machine

수학자 앨런 튜링에 의해 제안된 개념으로, 오토마타의 일종이며, 앞서 말했던 임의의 "기계적으로 계산 가능한 함수"를 계산하기 위한 가상의 기계이다.
Turing machine은 **state**와 더불어 symbol을 기록할 수 있는 cell로 이루어진 무한히 긴 **tape**, 그리고 특정 state에서 특정 symbol을 읽었을 때 해야 할 행동을 정의한 **action table**로 이루어져 있다.
눈치가 빠르다면 튜링머신의 state, tape, action table이 각각 컴퓨터의 register, memory, ISA로 발전했다는 것을 알아차렸을 것이다.

### Universal Turing Machine

하나의 행동표를 가진 turing machine은 하나의 함수만 계산할 수 있다.
하지만 우리가 원하는 기계는 모든 "기계적으로 계산 가능한 함수"를 계산할 수 있어야 한다. 그래서 등장한 개념이 universal turing machine이다.
Universal turing machine은 임의의 turing machine의 state set과 action table을 tape에 기록함으로 임의의 turing machine의 역할을 할 수 있다.

### Von Neumann Model

Universal turing machine을 실제로 전자공학적으로 구현해낸 사람이 폰 노이만이다.
그가 universal turing machine을 바탕으로 디자인한 hardware architecture가 **von neumann model**이며, 이 기계가 **컴퓨터의 시초**이다.

## 언어 구현체(Language Implementation)

이렇게 만들어진 전자적인 계산장치, 즉 컴퓨터는 전기신호를 통해 제어하는데, 전기신호의 유무를 0과 1로 표현하는 2진법 표현이 사용되었다.
따라서 컴퓨터는 0과 1로 구성된 특정 패턴의 전기신호가 들어오면 이에 맞게 정해진 동작을 하는 형태이다.
여기서 "0과 1로 구성된 특정 패턴"을 우리는 **기계어**라고 부른다.
그런데 기계어는 사람이 읽기에 너무나 불편해서 기계어와 특정 기호를 1대 1로 대응시켜서 사람이 읽기에 조금 더 편한 형태로 만들었고, 그것이 **어셈블리어**이다.

여기서 우리는 한 가지 문제를 마주하게 된다.
우리가 만드는 소프트웨어는 프로그래밍 언어를 기반으로 하는데, 컴퓨터는 기계어만 이해할 수 있다.
따라서 프로그래밍 언어를 기계어로 변환시키는 과정을 거치거나, 혹은 프로그래밍 언어를 직접 실행해주는 프로그램이 필요하다.
이처럼 프로그램을 컴퓨터가 수행할 수 있도록 하는 시스템을 **언어 구현체**라고 한다.
구현체는 compiler와 interpreter 두 가지로 구분된다.
당연하게도 한 가지 언어를 구현하는 방식은 여러 가지일 수 있다.

### Compiler

언어 구현체로서의 컴파일러는 프로그램을 읽고, 이를 기계어로 변환한다.
하지만 넓은 의미의 컴파일러는 한 프로그래밍 언어로 쓰여진 프로그램을 다른 프로그래밍 언어로 번역하는 일을 한다.
더 넓은 의미의 컴파일러는 프로그램 뿐만 아니라, 정해진 type의 input을 받아서 정해진 type의 output으로 변환시키는 일을 한다.
이 때 input과 output은 의미론적으로 반드시 동일해야 한다.

컴파일러는 보통 frontend, optimizer, backend로 이루어져 있다.

#### Frontend

Frontend는 input을 해석하고 내부적 자료구조인 intermediate representation(IR)으로 변환하는 일을 한다.

#### Optimizer

Optimizer는 IR을 최적화한다.

#### Backend

Backend는 최적화된 IR을 output으로 변환하는 일을 한다.

### Interpreter

인터프리터는 프로그래밍 언어로 쓰여진 프로그램을 기계어로 변환하는 과정을 거치지 않고, 곧바로 실행한다.
인터프리터는 소스 코드를 실행 가능한 단위로 parsing하는 단계와, 실제로 수행하는 execution 단계로 나뉜다.
이 구조 덕분에 인터프리터를 이용하면 소스 코드를 line 단위로 수행하는 것이 가능하다. 대표적인 예시가 shell이다.

#### Java Virtual Machine(JVM)

JVM은 대표적인 인터프리터로, bytecode를 JVM specification에 맞게 실행해주는 프로그램이라고 보면 된다.
Bytecode는 machine code처럼 생겼으나, architecture에 independent해서 portability가 큰 장점이다.
CPU가 기계어를 실행하는 것처럼 interpreter가 bytecode를 실행한다.
Java 뿐만 아니라, Scala 등 다양한 언어들이 Java bytecode로 컴파일될 수 있도록 설계되어 있다.

<br>

모든 글: [Programming Language](/language/programming Language/) [Language](/language/)
