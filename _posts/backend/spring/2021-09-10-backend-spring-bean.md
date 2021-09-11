---
title: "Spring Bean"
layout: single
categories:
  - Backend
  - Spring
permalink: /backend/spring/bean/
last_modified_at: 2021-09-10T21:03:50+09:00

---

이전 글: [IoC Container](/backend/spring/ioc/)

<br>

## Spring Bean

이전 글에서 스프링 프레임워크는 IoC Container가 객체 간 의존성을 관리한다고 했다.
이렇게 IoC Container가 관리하는 객체들을 **Bean**이라고 한다.

## Usage of Bean

스프링에서 IoC Container에 빈을 등록하고 필요한 곳에 주입하기 위해 annotation을 사용한다.

### Component Annotation

가장 기본적인 annotation은 `@Component`이다. 이 annotation이 붙어 있는 class는 자동으로 spring bean으로 등록된다.

```java
@Component
public class MyClass implements MyInterface {
  // ...
}
```

`@Component` 외에도 이를 상속하는 annotation들인 `@Controller`, `@Service`, `@Repository`를 사용할 수도 있다.
이 세 가지에 대한 내용은 다음 글에서 spring의 layered architecture를 다룰 때 설명하겠다.

### AutoWire Annotation

등록된 bean을 주입하고 싶은 곳에 `@Autowire` annotation을 사용한다.

```java
@SpringBootApplication
public class MyApplication {
  @Autowired
  final MyInterface myBean;

  // ...
}
```

### Configuration & Bean Annotation

`@Configuration`과 `@Bean` annotation을 활용하는 방법도 있다.
어플리케이션 설정을 담당하는 Configuration class를 만들고 `@Configuration` annotation을 붙인다.
그리고 빈으로 등록할 객체들을 return하는 method들을 만들고 `@Bean`을 붙인다.

```java
@Configuration
public class MyAppConf {
  @Bean
  public MyInterface createMyClassBean() {
    MyClass myClass = new MyClass();
    return myClass;
  }
}
```

<br>

다음 글: [Spring Architecture](/backend/spring/architecture/)

모든 글: [Spring](/backend/spring/) [Backend](/backend/)
