import time
start_time = time.time()

N=3
A=[0 for x in range(N)]
data=[x for x in range(1,N+1)]

def printSet(n):
    for i in range(n): # 각 부분 배열의 원소 출력
        if A[i]==1: # A[i]가 1이면 포함된 것이므로 출력.
            print("%d " % data[i], end="")
    print()
def powerset(n,k):
    if n==k:
        printSet(n)
    else:
        A[k]=1
        powerset(n,k+1)
        A[k]=0
        powerset(n,k+1)

powerset(N,0)
print(time.time() - start_time, 'seconds')





# import itertools
#
# chars = ['A', 'B', 'C']
# num=[1,2,3]
#
# p = itertools.permutations(chars, 2)  # 순열
# c = itertools.combinations(chars, 2)  # 조합
# n=itertools.permutations(num,1)
#
#
# print(list(p))
# print(list(c))
# print(list(n)[0][0])

# import itertools
#
# num=[1,2,3,4]
# permu=itertools.permutations(num,3)
# # print(list(permu))
#
# def powerset(n,k):
#     global ans2
#     if n==k:
#
#         ans=[]
#         for i in range(n):
#             if A[i]==1:
#                 ans.append(data[i])
#         if ans==[]:
#             pass
#         else:
#             ans2.append(ans)
#     else:
#         A[k]=1
#         powerset(n,k+1)
#         A[k]=0
#         powerset(n, k + 1)
#
#
# N=6
# A=[int(x) for x in range(N)] # 순서바꿔주는 리스트
# data=[int(x) for x in range(1,N+1)] # 돌리고 싶은 집합
# ans2=[]
# powerset(N,0)
# print(ans2)
#

