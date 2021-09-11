---
title: "Spring Architecture"
layout: single
categories:
  - Backend
  - Spring
permalink: /backend/spring/architecture/
last_modified_at: 2021-09-11T04:48:50+09:00

---

이전 글: [Spring Bean](/backend/spring/bean/)

<br>

## Layered Architecture

Layered Architecture는 컴퓨터공학에서 abstraction layer별로 역할을 분리시켜서 각 component들을 decoupling시킨 구조이다.
따라서 각각의 layer는 다른 layer가 무슨 일을 하는지는 신경을 쓸 필요가 없다.
그리고 각 layer들은 인접한 layer들끼리만 상호작용한다.
이는 network에서의 OSI model 등 컴퓨터공학에서 흔히 찾아볼 수 있는 구조이다.

### 3-Tier Architecture

소프트웨어 개발에서 흔히 사용하는 layered architecture는 3-tier architecture로,
각각 presentation tier, logic tier, data tier이다.
Presentation tier는 UI로, 사용자와 상호작용하며 요청을 받아 logic tier에 전달하고, 다시 응답을 받아 사용자에게 전달한다.
Logic tier는 business logic을 구현하고 있다.
마지막으로 data tier는 database와 이에 대한 접근을 관리하는 tier이다.
Logic tier에서 data에 접근이 필요할 경우 data tier를 통해 접근하게 된다.

## Spring is Layered

스프링 프레임워크 또한 layered architecture이다.
스프링 프레임워크의 세 layer를 각각 presentation layer, service layer(a.k.a. business layer), repository layer(a.k.a. data access layer)라고 한다.
또한 스프링 프레임워크는 MVC 패턴으로 디자인되어 있는데, model, view, controller가 이 세 layer에 포함되어 있다.

### Presentation Layer

우선 presentation layer는 사용자의 모든 요청을 dispatcher servlet이 받아서 handler mapping을 통해 요청에 해당하는 controller를 실행시킨다.
Controller는 요청에 대한 처리를 service layer에 요구하고, 응답을 받아 data를 model 객체에 담아 사용할 view 정보와 함께 dispatcher servlet에 넘긴다.
그러면 dispatcher servlet은 view resolver를 통해 view를 선택하고, client에게 요청이 처리된 결과를 반환한다.

### Service Layer

Service layer는 우리가 만드는 서비스의 business logic을 구현하고 있는 부분이다.
Presentation layer에서 넘어온 요청에 대한 처리를 거쳐 응답을 다시 presentation layer로 넘기는데,
database에 접근이 필요하면 repository layer로 필요한 정보를 넘겨서 data를 받아온다.
일반적으로 하나의 business logic은 하나의 transaction으로 동작하여, ACID 특성을 가진다.

### Repository Layer

Repository layer는 db에 대한 접근을 구현하고 있는 부분이다.
이 역할을 하는 객체를 DAO(Data Access Object)라고 한다(DAO가 repository layer 그 자체라고 볼 수 있다).
즉, service layer에서 db에 접근이 필요할 때, DAO 객체를 이용해서 접근하는 것이다.

### DTO

DTO(Data Transfer Object)는 각 layer 사이에서 정보를 주고받을 때 사용하는 객체이다.
DTO를 사용하는 목적은 객체 안에 필요한 정보만 담아 불필요한 정보를 없애기 위해서이다.

<br>

다음 글: [Spring Boot](/backend/spring/springboot/)

모든 글: [Spring](/backend/spring/) [Backend](/backend/)
