---
title: "AOP"
layout: single
categories:
  - Backend
  - Spring
permalink: /backend/spring/aop/
last_modified_at: 2021-09-27T14:18:50+09:00

---

## Aspect Oriented Programming

각 business logic들은 핵심 logic과 부가적인 logic으로 나눌 수 있는데,
특히 각 business logic의 부가적인 부분들은 핵심 logic에 종속성이 없는 경우도 많고, 여러 logic에서 반복적으로 나타나는 경우도 많다.

이 때 각 logic에서 부가적인 logic들을 business logic과 분리하여 따로 모듈화하는 것을 AOP, 즉 관점 지향 프로그래밍이라고 한다.
따라서 AOP는 [SRP](/oop/principle/srp/)를 적용시킨 사례라고 볼 수 있겠다.

이 때 부가적인 logic을 모듈화한 것을 aspect라고 한다.

## Spring AOP

Spring에서 aspect는 사실 proxy object이다.
IoC container에 등록된 aspect class는 runtime에서 target object가 호출될 때 생성되어 이 호출을 가로챈다.
개인적인 생각인데, 파이썬에서 descriptor의 원리와 비슷하다고 느꼈다.

Aspect class도 container에 bean으로 등록해야 한다.

## Terminology

### Target

핵심 로직을 담고 있는 모듈로 aspect를 적용할 대상이다.

### Advice

타겟에 부여할 부가기능을 정의한 모듈이다.

### Join Point

Advice가 적용될(join) 수 있는 위치를 말한다. **적용된 곳이 아님**.
보통 target class의 모든 method가 join point가 된다.

### Pointcut

Advice를 적용할 method를 나타내는 정규표현식이다.

### Aspect

AOP의 기본 단위이다. Aspect = Advice + PointCut이라고 볼 수 있다.
Aspect 객체는 singleton으로 존재하는데, 잠깐 생각해보면 이해된다.

### Advisor

Spring에서만 쓰는 용어인데, aspect와 비슷하게 advice + pointcut이다.
Aspect와 다른 점은 결국 object의 목적이라고 생각된다.
Aspect가 **부가기능**을 정의한 객체라면, advisor는 advice를 제공하는 객체이다.
같은 기능이더라도 초점이 다르다고 생각이 된다.

### Weaving

Weaving은 advice를 삽입하는 과정을 말한다.

## Types of Advice

### Around

Target method를 감싸서 실패 여부와 상관없이 앞뒤로 부가기능을 수행한다.

### Before

Target method가 수행되기 이전에 부가기능을 수행한다.

### After Returning

Target method가 정상적으로 수행된 후 부가기능을 수행한다.

### After Throwing

Target method가 exception을 발생시킬 때 부가기능을 수행한다.

### After (Finally)

After 또는 After Finally Advice는 target method 수행 후 실패 여부와 상관없이 부가기능을 수행한다.

## Implementation

### Aspect Class

```java
@Component
@Aspect
public class DummyAspect {
    // ...
}
```

`@Component` annotation으로 해당 클래스를 container에 등록하고,
`@Aspect` annotation으로 해당 클래스가 aspect임을 알린다.

### Pointcut Method

```java
@Component
@Aspect
public class DummyAspect {
    @Pointcut("bean(serviceController)")
    private void targetA() {};

    @Pointcut("execution(public * *(UserDto, ..))")
    private void targetB() {};

    @Pointcut("within(com.myproject.*)")
    private void targetC() {};
    
    @Pointcut("targetA() && targetB() && bean(myBean)")
    private void targetD() {};
}
```

`@Pointcut` annotation을 이용하여 네 개의 pointcut을 정의했다.
그 중 A, B, C는 pointcut regex를 이용한 방식이고, D는 pointcut을 조합하는 방식이다.
참고로 regex에서 *는 전부, 그리고 ..는 path에서 나오면 하위 패키지까지 포함한다는 뜻이고 method parameter에서 나오면 0개 이상의 임의의 type의 parameter를 뜻한다.
이 외에도 `target`, `args`, `annotation`, `@target`, `@args`, `@within`, `@annotation` 등 매우 다양한 pointcut regex가 있는데, 이들은 주로 pointcut보다는 advice annotation에서 사용된다.

- `bean(id)`는 해당 id를 가진 bean의 모든 method를 뜻한다.
- `within(path)`는 해당 path 내에 정의된 모든 method를 뜻한다. Path로 모듈이나 패키지, 혹은 클래스 레벨까지 나타낼 수 있다. 패키지를 생략하면 현재 패키지를 뜻한다.
- `execution([accessor, retType] [methodName with class name including optional package path]([method parameter]))`는 해당 prototype을 가진 method를 뜻한다.
  - 맨 앞에 `*`를 사용하면 모든 접근제어자와 모든 반환형 뜻한다. 접근제어자나 return type 둘 중 하나만 wildcard를 사용할 수도 있다.
  - class와 method 이름을 쓸 때 같은 package에 있는 class면 package path를 생략할 수 있다.
  - class와 method 이름을 쓸 때도 wildcard를 사용할 수 있다.
- `@annotation(annotation)` regex는 해당 annotation이 붙은 모든 method를 뜻한다. Annotation을 직접 정의한 후 유용하게 사용할 수 있다.

### Advice Method

```java
@Component
@Aspect
public class DummyAspect {
    @Pointcut("bean(serviceController)")
    private void targetA() {};

    @Pointcut("execution(public void *(..))")
    private void targetB() {};
    
    @Pointcut("targetA() && targetB()")
    private void targetC() {};

    @Around("execution(public void *)")
    public Object adviceOne(ProceedingJointPoint pjp) {
        // ...
    }

    @Before("within(com.java.*)")
    public void adviceTwo(JointPoint jp) {
        // ...
    }

    @AfterReturning("allTarget()")
    public void adviceThree(JointPoint jp) {
        // ...
    }

    @AfterReturning(pointcut="allTarget()", returning="ret")
    public void adviceFour(JointPoint jp, Object ret) {
        // ...
    }

    @AfterThrowing("allTarget() && args(account,..)")
    public void adviceFive(Account account) {
        // ...
    }

    @AfterThrowing(pointcut="allTarget()", throwing="e")
    public void adviceSix(JointPoint jp, Exception e) {
        // ...
    }

    @After("allTarget()")
    public void adviceSeven(JointPoint jp) {
        // ...
    }
}
```

#### Parameters of Advice

Advice method들은 여러 가지 parameter를 가질 수 있는데, 천천히 살펴보자.

- `JointPoint`: advice 종류에 관계없이 advice의 첫 번째 인자로 `JointPoint` 타입을 가질 수 있다.
이 친구는 joint point, 즉 target method를 나타낸다. `getArgs`, `getThis` 등 유용한 메소드들이 있다.
  - Around type의 advice는 반드시 `ProceedingJointPoint` type의 첫 번째 인자를 가져야 한다. 그래야 advice가 언제 target method를 수행하는지 나타낼 수 있다.
- Target method의 parameter: pointcut regex중 args를 이용해서 target method의 parameter type을 제한할 수 있다.
그런데 advice에서 target method의 argument를 사용해야 하는 경우가 있을 수 있는데, 이 때 target method의 해당 parameter를 advice의 parameter로 잡아줄 수 있다. `adviceFive` 참고.
원래 `args` pointcut regex는 argument type limitation인데,
advice의 argument에서 type이 명시되어 있기 때문에 advice parameter와 target method parameter를 매칭시키기 위해서 변수 이름을 사용한다.
- `returning`: `AfterReturning` annotation의 경우 target method의 return을 사용해야 하는 경우 이를 annotation에서 명시해줄 수 있다.
Advice의 parameter 중에서 target method의 return으로 사용되는 것의 이름을 annotation의 `returning` argument로 넘겨주면 된다.
- `throwing`: `returning`과 비슷하게, `AfterThrowing`에서 발생한 exception을 나타낸다.

#### Advice Ordering

두 개 이상의 advice가 하나의 join point에 적용될 때, 같은 aspect의 advice일 경우 before on the way in, after on the way out 순으로 적용된다.
즉, before advice는 위에가 먼저, after advice는 아래가 먼저 적용된다. 헷갈리면 annotation이 적용되는 순서가 밑에서부터 적용된다는 것을 생각하면 될 것 같다.

<br>

모든 글: [Spring](/backend/spring/) [Backend](/backend/)
