---
title: "SRP"
layout: single
categories:
  - OOP
  - OOP Principle
permalink: /oop/principle/srp/
last_modified_at: 2021-09-27T16:18:50+09:00

---

## Single Responsibility Policy

Single Responsibility Policy(SRP), 즉 단일 책임 원칙은 한 클래스가 한 가지 책임만 가져야 한다는 원칙이다.
그 이유는 여러 책임을 가지게 되면 그만큼 변화의 축이 생기기 때문이다.
SRP가 잘 적용된 클래스는 자연스럽게 본 클래스의 책임을 제외한 다른 변화에 대해 닫혀있게 된다.

## Example

```java
// no SRP
public interface Sender {
  void sendMsg(final String rawMsg, final String encodingScheme);
}

public class SSLSender implements Sender{
  @Override
  public void sendMsg(final String rawMsg, final String encodingScheme) {
    final byte[] encodedMsg = encode(rawMsg, encodingScheme);
    // msg sending logic
  }

  private byte[] encode(final String rawMsg, final String encodingScheme) {
    if (encodingScheme.equals("utf-8")) {
      // encoding logic
    } else if (encodingScheme.equals("en-US")) {
      // encoding logic
    } // any more logics...
    return encodedMsg;
  }
}
```

위 코드에서 SSLSender는 두 가지 책임을 가지고 있다. 하나는 message를 encoding하는 것, 그리고 다른 하나는 message를 보내는 것이다.
따라서 위 class는 1) encoding logic이 추가되거나 변경될 때, 2) message sending logic이 추가되거나 변경될 때마다 고쳐야 한다.
즉, 2개의 변화의 축(axis of change)를 가지고 있다. 이 경우 class의 수정이 잦아지게 되고, [OCP](/oop/principle/ocp/) 원칙도 잘 지켜지지 않기 때문에 별로다.
그나마 method가 분리되어 있어서 좀 낫지, 하나의 method에 두 logic이 섞여서 구현되었을 경우 더 끔찍하다.

우리는 `SSLSender` class에서 message encoding logic을 따로 추출하여 extract class를 만들 것이다.

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

이제, SSLSender class는 message를 보내는 책임만을 가지게 되어서 encoding logic에 수정사항이 생겨도 고칠 이유가 없다.
게다가, OCP 원칙도 잘 적용되어서 새로운 type의 encoding scheme이 구현되더라도 고칠 필요가 없다. 즉 확장에 열려 있다.

<br>

다음 글: [OCP](/oop/principle/ocp/)

모든 글: [OOP Principle](/oop/principle/) [OOP](/oop/)
