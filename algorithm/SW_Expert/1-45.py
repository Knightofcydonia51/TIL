import datetime

name=input()
age=int(input())
now=(datetime.datetime.now().year)
def cal(name, age):
	ans=now+(100-age)
	print('{}(은)는 {}년에 100세가 될 것입니다.'.format(name, ans))
cal(name, age)