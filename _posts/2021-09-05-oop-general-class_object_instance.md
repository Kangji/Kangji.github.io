---
title: "Class vs Object vs Instance"
layout: single
categories:
  - OOP
  - General OOP
permalink: /oop/general/class_object_instance/
last_modified_at: 2021-09-05T17:01:50+09:00

---

## Class

클래스는 설계도이자 틀이다. 표현하고자 하는 대상의 state(field)와 action(method)에 대한 정의를 담고 있다.

```java
final class Exam {
    private List<Subject> subjectList;

    public Exam(final List<Subject> subjectList) {
        if (subjectList.size() == 0) {
            raise NoExamException();
        }
        
        subjectList.forEach(this.subjectList::add);
    }

    public startTest(final int period) {
        try {
            subjectList.get(period).start();
        } catch (Exception e) {
            raise NoExamException();
        }
    }
}
```

## Object

객체는 그래서 내가 클래스를 가지고 구현하고자 하는 대상을 말한다. 위 클래스를 예시로 들자면,
"`Exam` 클래스"는 "시험"이라는 객체를 구현하는 설계도인 셈이다.

## Instance

그렇다면 instance는 뭘까?? 사실 object와 instance는 굉장히 유사한 개념이고, 사람들이 많이들 혼용해서 쓴다.
하지만 엄밀하게 보면 이 둘은 다르다. Instance는 Object를 실체화 시킨 것이다.

```java
Exam midTerm = new Exam(new ArrayList<>(Arrays.aslist(
    new Math(), new English(), new Physics())));
Exam finalExam = new Exam(new ArrayList<>(Arrays.aslist(
    new English(), new Math(), new Physics(),
    new Chemistry(), new Algorithm()));
```

이 예시에서 `midTerm`과 `finalExam`은 모두 `Exam`이라는 객체의 인스턴스지만, 두 인스턴스는 서로 다르다.

<br>

모든 글: [General OOP](/oop/general_oop/) [OOP](/oop/)
