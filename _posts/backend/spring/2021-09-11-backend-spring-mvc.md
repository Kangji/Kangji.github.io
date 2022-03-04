---
title: "MVC"
layout: single
categories:
  - Backend
  - Spring
permalink: /backend/spring/mvc/
last_modified_at: 2021-09-11T04:48:50+09:00

---

## MVC Pattern

MVC는 Model-View-Controller의 약자로, 소프트웨어에서 흔히 사용되는 디자인 패턴이다.
MVC 패턴은 사용자 인터페이스로부터 비즈니스 로직을 분리시키는 장점이 있다.
MVC 패턴은 model, view, controller 세 부분으로 이루어져 있다.

### Model

Model은 application data를 나타내고 처리하는 부분이다.

### View

View는 사용자에게 보여지는 것들을 담당하는 부분이다.

### Controller

Controller는 사용자의 요청을 처리하는 부분으로, business logic을 구현하고 있고, view와 model 사이의 통신을 담당한다.

### MVC Mechanism

먼저, 사용자의 요청을 controller가 받아서 요청에 따라 알맞은 model을 호출한다.
Model은 data를 처리한 후 응답을 다시 controller에게 보내고, controller는 응답을 view에게 보낸다.
View는 응답을 처리한 결과를 다시 controller에게 보내고, controller가 결과를 사용자에게 반환한다.

### Model 1 & 2

MVC를 구현하는 방식에는 model 1과 model 2가 있는데, 차이는 model 1은 controller와 view가 통합되어 있다는 것이다.
위의 MVC Mechanism도 model 2 방식이고, 사실상 model 1 방식은 쓰이지 않는다고 봐도 된다.

<br>

모든 글: [Spring](/backend/spring/) [Backend](/backend/)
