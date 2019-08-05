a = int(input())
list=[]
for i in range(1,a+1):
    if a % i == 0:
        list.append(i)
        print("{}(은)는 {}의 약수입니다.".format(i,a))
    if list.__len__()==2:
        print("{}(은)는 {}과 {}로만 나눌 수 있는 소수입니다.".format(a,list[0],list[1]))
