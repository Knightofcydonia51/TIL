import sys
sys.stdin=open("07.pizza.txt")
T=int(input())
for i in range(T):
    N, M = map(int, input().split())
    pizzas=[int(x) for x in input().split()]
    hwaduk=[]

    for j in range(N):
        hwaduk.append(pizzas.pop(0))

    while len(hwaduk)!=1:
        for j in range(N):
            hwaduk[0]=hwaduk[0]//2
            hwaduk.append(hwaduk.pop(0))
            print(hwaduk)
        if hwaduk[0]==0:
            hwaduk.pop(0)
            if len(pizzas)!=0:
                hwaduk.insert(0,pizzas.pop(0)) #위치, 넣을꺼
                print("피자", pizzas)


# for tc in range(T):
#     N,M=list(map(int,input().split()))
#     pizza=[[0]*2 for _ in range(M)]
#     for i in range(1,M+1):
#         pizza[i-1][0]= i
#     data=list(map(int,input().split()))
#     for j in range(M):
#         pizza[j][1]=data[j]
#     hadok=[0]*N
#     for i in range(len(hadok)):
#         hadok[i]=pizza.pop(0)
#
#     while len(hadok)!=1:
#         hadok[0][1]= hadok[0][1]//2
#         if hadok[0][1] ==0 and len(pizza) !=0:
#             hadok.pop(0)
#             hadok.append(pizza.pop(0))
#         elif hadok[0][1] ==0 and len(pizza) ==0:
#             hadok.pop(0)
#         else:
#             back=hadok.pop(0)
#             hadok.append(back)
#     print("#{} {}".format(tc+1,hadok[0][0]))