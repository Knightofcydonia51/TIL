# import sys
# sys.stdin=open('17281.baseball.txt')
#
# def comb(r,k): # 빈칸의 포인터, 풀의 포인터
#     global maxi
#     if r==0:
#         pass #야구 실행
#
#     else:
#         if r>k:
#             return
#         else:
#             T[r-1]=A[k-1]
#             comb(r-1,k-1) #선택시
#             comb(r,k-1) #선택안할시
#
#
# # 타순을 정하고, 타순이 정해지면 야구 실행
# #
#
# N= int(input())
# innings=[list(map(int,input().split())) for x in range(N)]
# ans=0
# for i in range(len(innings)):
#     maxi=0
#     A=innings[i]
#     T=[0]*9
# #     comb,maxi


A=[1,2,3,4]
A.append()
print(A)