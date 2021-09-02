---
title: "Virtual Environment"
layout: single
categories:
  - Language
  - Python
tags:
  - Tutorial
permalink: /language/python/venv/
last_modified_at: 2021-08-30T02:17:00+09:00

---

## Virtual Environment란??

가상환경이란?? 자바는 maven으로 프로젝트별로 패키지 관리를 할 수 있지만, 파이썬은 그렇지 않다.
하지만 이 문제는 파이썬 가상환경을 활용하여 해결한다.
파이썬에서 가상환경은 하나의 PC에서 프로젝트별로 독립된 python interpreter와 runtime environment를 setting할 수 있게 해주는 고마운 친구이다.
가상환경 덕분에 프로젝트 배포시 사용자 PC의 환경을 고려하지 않아도 된다.

### 가상환경 생성

```sh
# install virtualenv package first
$ pip install --upgrade virtualenv

# change to project directory
$ cd /your/project/directory

# create virtual environment
$ virtualenv venv

# or create virtual environment with python interpreter version specified
# make sure the specified version of interpreter is installed on your PC
$ virtualenv venv --python=3.9.1
```

우선, `pip`로 `virtualenv` 패키지를 다운받는다.
그 후 프로젝트 directory로 이동한 후 위 command로 프로젝트 디렉토리에 `venv`라는 이름의 가상환경 폴더를 생성한다.
관습적으로 가상환경 폴더 이름은 `venv` 또는 `.venv`로 짓는다.

### 가상환경 활성화

```sh
# activation
$ source venv/bin/activate

# check python interpreter version
(venv) $ python --version
Python 3.9.1

# check python interpreter location
(venv) $ which python
/your/project/directory/venv/bin/python
```

위 command를 실행하고 나면, shell에 `(venv)`라고 표시된다.
이는 현재 `venv`라는 이름의 가상환경이 활성화되어 있다는 뜻이다.
가상환경이 활성화된 상태에서 python interpreter의 버젼과 위치를 확인해보자.
그러면 내가 설정한 버젼의 interpreter가 `venv/bin`에 있는 것을 알 수 있다.

### 가상환경 비활성화

```sh
# deactivation
(venv) $ deactivate

# after deactivation
$ 
```

### 패키지 설치

가상환경이 활성화된 상태에서 `pip` 등을 이용해 패키지를 설치하면 전역이 아닌, 활성화된 가상환경에 패키지가 설치된다.
주로 프로젝트 개발 시 필요한 패키지가 많기 때문에, `requirements.txt` 파일을 이용하여 한 번에 관리한다.
마찬가지로 requirements.txt라는 파일명은 관습이다.

```sh
# create requirements.txt
(venv) $ pip freeze > requirements.txt

# install requirements.txt
(venv) $ pip install -r requirements.txt
```

`pip freeze` 명령어를 사용하면 설치된 패키지들과 그 버젼을 확인할 수 있다.
Shell pipe를 이용해서 그 내용을 `requirements.txt`에 담을 수 있다.

`pip install`에서 `-r` 옵션을 사용하면 파일을 인자로 받아서 그 파일 안의 패키지를 명시된 버젼으로 설치할 수 있다.

<br>

모든 글: [Django](/backend/django/) [Backend](/backend/)
