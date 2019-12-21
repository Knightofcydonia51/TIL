# Algorithm



### 시험에 임하기 전
>1. 배열 내의 숫자를 직접적으로 바꿔가며 풀어야 하는 시뮬레이션의 경우,  바꿔야 할 숫자인지를 검증하기 위해 첫번째 순회를 할 때 체크를 하고, 이후 다시 순회해서 숫자를 일괄적으로 바꿔줘야 한다.
>2. 나누기 연산을 할 때 0으로 나눠지는 경우는 반드시 예외처리를 해주자.
>3. 문제를 풀 때는 항상 N제한(입력의 크기)를 읽고 들어가는 것이 좋다.  시간복잡도(O(N))이 1억 이하면 1초안에 풀린다.
>4. 








### split, join, strip, replace

```python
a=' h, i '

a.strip()
>'h, i'

a=a.split(',')
>['h', ' i']

a=''.join(a)
>'h i'

a=a.replace(" ","")
>'hi'
```



### 정규표현식

```python
[0-9]			\d		숫자
[^0-9]			\D		텍스트 + 특수문자 + 화이트스페이스
[ \t\n\r\f\v]	\s		스페이스, TAB, 개행(new line)
[^ \t\n\r\f\v]	\S		텍스트 + 특수문자 + 숫자
[a-zA-Z0-9]		\w		텍스트 + 숫자(특수문자는 제외. 단, 언더바 포함) 
[^a-zA-Z0-9]	\W		특수문자 + 공백

^은 not의 의미로 쓰임.


import re

blabla='안녕&*$(@&(*$asdk995'
p='\W'
print(re.findall(p, blabla))
> ['&', '*', '$', '(', '@', '&', '(', '*', '$']

blabla='DFFD55$$'
p='[A-Z]'
print(re.findall(p, blabla))
> ['D', 'F', 'F', 'D']
```



### 소수점 출력 제한

```python
b=12.45456
print('%.2f' % b)
> 12.45

print(round(b,3))
> 12.455
```



### 튜플과 리스트의 공통점과 차이점

>둘다 순서가 있는 iterable 객체
>
>튜플은 불변(immutable), 리스트는 가변(mutable)
>
>리스트는 append 사용가능, 튜플은 불가
>



### if else 한줄로 쓰기

```python
return True if len(s)==0 else False
```

