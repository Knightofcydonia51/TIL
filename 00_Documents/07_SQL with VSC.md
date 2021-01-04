# SQL



ORM : 객체지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에 데이터를 변환하는 기술.

![](C:\Users\student\Desktop\0_UkOqM_a_agYwUOoV.png)



sql 문법을 몰라도 조작 가능**, python의 클래스로 DB를 조작할 수 있다**





python manage.py sqlmigrate articles 0001



python manage.py shell_plus





## csv를 가져와서 테이블로 만드는 작업

csv파일은 폴더 내 경로에 함께 있어야 함.

터미널상에서 하고싶은 폴더 디렉토리 내로 간 다음,

sqlite3 tutorial.sqlite3

.databases

.mode csv

.import csv파일명 examples



## 명령어 일람

.exit : sql 종료.

.tables : 테이블 목록 조회.

.schema 테이블명 : 스키마 구조 확인

drop table 테이블명; : 테이블 드랍

.headers on

.mode column : 깔끔하게 보기



insert into 테이블명(컬럼명1, 컬럼명2, ...) values (밸류1, 밸류2, ...); : 데이터 삽입

insert into 테이블명 values (밸류1, 밸류2, ...) : 모든 컬럼에 데이터 삽입할 때

delete from 테이블명 where id=2; : 테이블에서 id가 2인 컬럼 삭제

update 테이블명 set column1=value1

alter table 테이블명 rename to 바꿀테이블명 : 테이블 이름 바꾸기

alter table 테이블명 ADD COLUMN 컬럼명 데이터타입; : 테이블에 컬럼 추가

