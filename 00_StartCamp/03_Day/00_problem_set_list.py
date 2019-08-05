# 문제1. 문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 만드세요.

# str=input()
# print(str[:1],str[-1:])
# print(f'첫글자는 {str[0]} 이고, 뒷글자는 {str[-1]}입니다.')

# 문제2. 자연수 n이 주어질 때, 1부터 n까지 한 줄에 하나씩 출력
# n=int(input())
# for i in range(1,n+1):
#     print(i)

# 문제3. 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하세요.

# number=int(input())
# if number%2==0:
#     print("짝수네요")
# else:
#     print("홀수네요")

"""
문제4. 국어 영어 수학 과학점수 입력받고, 각각 90점이상, 80점 초과, 85점 초과, 80점이상일때 합격
합격이면 true, 아니면 false로 출력
"""
# a=int(input('국어 : '))
# b=int(input('영어 : '))
# c=int(input('수학 : '))
# d=int(input('과학 : '))

"""
문제5. 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 한 줄에 하나씩 출력하는 프로그램을 만드세요
"""
prices=input().split(";")
a=sorted(list(map(int,prices)))
while len(a):
    print(a.pop())

