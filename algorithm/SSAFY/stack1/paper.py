# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(4))
#
# def fibo(n):
#     if n<2:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
#
# print(fibo(8))

# def fibo2(n):
#     f=[0,1]
#     for i in range(2, n+1):
#         f.append(f[i-1]+f[i-2])
#     return f[n]
# print(fibo2(1000))

def f(k):
    if k <=1 :
        return 1
    else:
        return f(k-1) + 2*f(k-2)

import sys
sys.stdin = open("paper.txt")
T = int(input())

for t in range(1, T+1):
    N = int(input())

    print("#{} {}".format(t, f(N//10)))