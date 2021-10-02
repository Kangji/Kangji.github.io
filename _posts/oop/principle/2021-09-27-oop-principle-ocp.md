---
title: "OCP"
layout: single
categories:
  - OOP
  - OOP Principle
permalink: /oop/principle/ocp/
last_modified_at: 2021-09-27T16:18:50+09:00

---

이전 글: [SRP](/oop/principle/srp/)

## Open Closed Principle

Open-Closed Principle(OCP), 즉 개방-폐쇄 원칙은 객체는 변화에는 닫혀있고, 확장에는 열려있어야 한다는 원칙이다.
즉, 객체의 수정은 최소화하면서도 확장성을 높여야 한다는 말이다.
알쏠달쏭한 말이다. 쉽게 풀어서 설명하려고 해도 어렵다.

## Example

SRP 원칙에서 사용한 예시를 보자.

```java
public interface Sender {
  void sendMsg(final string rawMsg);
}

@Inject
public class SSLSender implements Sender {
  private final EncodingScheme encodingScheme;


  public SSLSender (final EncodingScheme encodingScheme) {
    this.encodingScheme = encodingScheme;
  }

  @Override
  public void sendMsg(final String rawMsg) {
    final byte[] encodedMsg = encodingScheme.encode(rawMsg);
    // msg sending logic
  }
}

public interface EncodingScheme {
  byte[] encode(final String rawMsg)
}

public class Utf8 implements EncodingScheme {
  @Override
  public byte[] encode(final String rawMsg) {
    // encoding logic
  }
}

public class EnUs implements EncodingScheme {
  @Override
  public byte[] encode(final String rawMsg) {
    // encoding logic
  }
}
```

이 코드에서 `SSLSender`는 `EncodingScheme`에 대한 확장에 열려 있다.
왜냐하면, `SSLSender` class가 `EncodingScheme` 인터페이스를 참조하기 때문이다.
따라서 아무 수정 없이도 새로운 `EncodingScheme`을 구현한 클래스 또한 `SSLSender`의 생성자로 넘길 수 있다.

같은 이유로, `SSLSender`는 `EncodingScheme`에 대한 변화에 닫혀 있다.
왜냐하면, `SSLSender` class로부터 `EncodingScheme`에 대한 개념을 추출하여 Extract Class를 만들었기 때문이다.
모든 변화는 `SSLSender` class가 아닌 `EncodingScheme`을 구현한 각각의 클래스들에 일어나게 된다.
따라서 더 이상 `SSLSender`는 `EncodingScheme`에 종속적이지 않다.

OCP를 적용하는 방법은 적절한 확장의 축을 잡고 인터페이스를 선언하는 것이라고 할 수 있겠다.

<br>

모든 글: [OOP Principle](/oop/principle/) [OOP](/oop/)
