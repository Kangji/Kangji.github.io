---
title: "SQL Basic"
layout: single
categories:
  - Database
  - SQL
permalink: /database/sql/0/
last_modified_at: 2021-08-29T16:37:00+09:00

---

## 1. DBMS

데이터베이스(DB)라는 말은 많이 들어봤을 것이다. 데이터베이스는 단순히 데이터 저장소라고 볼 수 있다. 흔한 엑셀 파일도 어떻게 보면 데이터베이스인 것이다.
인터넷 기술이 발달하고 데이터의 양이 늘어나면서 사람이 손으로 데이터를 관리하는 것은 사실상 불가능해졌다.
이런 상황에서 데이터 관리를 도와주는 시스템이 바로 DBMS, Database Management System이다.

## 2. RDB, RDBMS

DB 중에서도 OOP 개념을 사용하여 table을 정의하고, foreign key를 이용하여 table들 사이의 관계를 정의하는 형식의 DB를 관계형 DB, Relational Database라고 한다.
당연히 RDBMS는 RDB Management System이다.

### RDB의 구조

하나의 데이터베이스는 여러 개의 table을 가지고, 각 table은 OOP에서의 객체와 유사하다.
![Table](/assets/images/database/table.png)
Table의 맨 첫 row가 table의 field들을 담고 있는데, class의 field와 상당히 유사하다.
각 field는 `int unsigned`, `char(64)`, `varchar(20)` 등의 type이 있고, Nullable, default 등을 설정할 수도 있다.
그 다음 두 번째 row부터는 한 row가 하나의 record인데, table이 객체라면 record는 인스턴스이다.

RDB, RDBMS, SQL에 대한 자세한 내용은 향후 Database 관련 포스팅에서 다루겠다.

참고: [Database System Concepts](https://www.db-book.com/db6/slide-dir/index.html)

### RDBMS의 종류

RDBMS에는 Oracle DB, SQLite, MySQL 등이 있다.

- Oracle DB는 유료라는 단점이 있다.
- MySQL은 오픈소스라서 가장 널리 쓰였으나, Oracle이 인수한 후 라이센스 문제가 대두되면서 많은 유저가 이탈했다.
- SQL Server는 MS에서 만든 거라 Window에서 사용이 가능하다는 장점이 있다.
- SQLite는 DB를 서버가 아닌 파일로 저장하기 때문에 가벼운 크기의 데이터를 관리하는데 용이하다.

## 3. SQL

SQL은 Structured Query Language의 약어로, Statement 하나하나가 RDBMS에 보내는 query라서 이런 이름이 붙었다.
SQL은 용도에 따라 DDL, DML, DCL로 나뉜다.

### Data Definition Language

DDL은 DB에 table을 생성/삭제하는 등 database 자체에 대한 작업에 쓰인다.

```sql
create database my_db;
show databases;

use my_db;

create table membership (
    id varchar(20),
    age int unsigned,
    primary key(id)
);
```

Line 1은 my_db라는 이름의 database를 MySQL 서버에 만드는 쿼리이다.

Line 2는 서버에 있는 database들을 요청하는 쿼리이다.

Line 3~4는 my_db에 회원 id와 나이 정보를 담고 있는 membership이라는 table을 생성하는 쿼리이다.

`create` 외에도 `alter`, `drop` 등이 있다.

### Data Management Language

DML은 데이터 검색/삽입/수정/제거 등 실질적으로 데이터를 관리하는데 쓰인다.

```sql
select id from membership;
insert into membership(id, age) values ('Kangji', 24);
```

위 예시는 membership table에서 모든 record의 id field를 요청하는 쿼리와, membership table에 새로운 record를 삽입하는 쿼리이다.

### Data Control Language

DCL은 Access Control에 쓰인다. `grant`, `revoke` 등이 있다.

## 4. MySQL

### 설치

```sh
# ubuntu
$ sudo apt-get install mysql-server mysql-client

# MacOS
$ brew install mysql
```

### 서버 켜기

```sh
# ubuntu
$ service mysql start

# MacOS
$ mysql.server start
```

### MySQL 접속

일단 root 권한으로 접속한다. 처음에는 root user의 pw는 설정되어 있지 않다.

```sh
# MacOS
$ mysql -u root -p
```

`-u`는 user를, `-p`는 password를 뜻한다.

### MySQL 유저 추가

```sql
> use mysql;
> create user 'username'@localhost;
> alter user 'username'@localhost identified by 'password';
```

### User 권한 설정

```sql
> grant all privileges on db_name.table_name to 'username'@localhost identified by 'password';
> show grants for 'username'@localhost;
```

<br>

모든 글: [SQL](/database/sql/) [Database](/database/)
