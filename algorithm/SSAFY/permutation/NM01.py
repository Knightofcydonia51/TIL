# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#
# # 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
# # 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# # 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

import sys
sys.stdin=open('NM01.txt')

def perm(n, k, num):
    if k==M:
        ans.append(num)
    else:
        for i in range(k, n):
            A[i], A[k] = A[k], A[i]
            perm(n, k + 1,num+data[A[k]]+" ")
            A[i], A[k] = A[k], A[i]

T=int(input())
for i in range(T):
    N,M = map(int, input().split())
    A=[int(x) for x in range(N)]
    data=[str(x) for x in range(1,N+1)]
    ans=[]
    perm(N,0,"")
    ans.sort()
    for k in range(len(ans)):
        print(ans[k])




# s = []
# def PrintArr(n,string):
#     s.append(string)
#
# def perm(n, k, string):
#     if n-1 == k:
#         string = data[0] + string + data[len(data)-1]
#         PrintArr(n, string)
#     else:
#         for i in range(k, n-1):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(n, k+1, string + data[arr[k]])
#             arr[k], arr[i] = arr[i], arr[k]
# N = 5
# arr = [i for i in range(N)]
# data = [str(i) for i in range(1,N+1)]
# perm(N, 1, "")
#
# for i in range(len(s)):
#     print(s[i])


