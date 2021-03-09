# mySQL 유용한 명령어들

`ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_OUTCOME | VARCHAR(N) | FALSE    |



## SELECT *

```mysql
SELECT * FROM ANIMAL_OUTS

ANIMAL_ID	ANIMAL_TYPE	DATETIME	NAME	SEX_UPON_OUTCOME
A349480	Dog	2013-12-22 11:30:00	Daisy	Spayed Female
A349733	Dog	2017-09-27 19:09:00	Allie	Spayed Female
```



## DATE_FORMAT

YYYY-MM-DD 00:00:00 format에서 시간을 제외한 형식만 출력하기

```mysql
SELECT ANIMAL_ID,NAME,DATE_FORMAT(DATETIME, '%Y-%M-%D') AS '대문자' FROM ANIMAL_INS

ANIMAL_ID	NAME	대문자
A349996	Sugar	2018-January-22nd
A350276	Jewel	2017-August-13th
A350375	Meo	2017-March-6th



SELECT ANIMAL_ID,NAME,DATE_FORMAT(DATETIME, '%y-%m-%d') AS '소문자' FROM ANIMAL_INS

ANIMAL_ID	NAME	소문자
A349996	Sugar	18-01-22
A350276	Jewel	17-08-13
A350375	Meo	17-03-06
```



## HOUR

YYYY-MM-DD 00:00:00 에서 시간만 출력하기

```mysql
SELECT HOUR(DATETIME) AS '시' FROM ANIMAL_INS

NAME	시
Sugar	14
Jewel	13
Meo	15
Harley	4
Gia	16
```



IF 절 사용하기

```mysql

```



2개 이상 조건의 WHERE절

```mysql

```

 





## JOIN



![SQL Join](img/SQL Join.png)



LEFT JOIN을 사용해 왼쪽 테이블에는 존재하지만 오른쪽 테이블에는 존재하지 않는 값을 리턴하기

```mysql
SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_OUTS AS OUTS
LEFT JOIN ANIMAL_INS AS INS ON OUTS.ANIMAL_ID=INS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID


```





# 부록 : NoSQL

- 