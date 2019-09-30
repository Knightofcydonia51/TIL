import sys
sys.stdin = open("07.minimum.txt")
import time
start_time = time.time()

def perm(n,k,q):
    global min
    if q>=min:return
    if n==k:
        if q<min:
            min=q
    else:
        for i in range(k,n):
            A[i],A[k]=A[k],A[i]
            perm(n,k+1,q+sheet[A[k]][k])
            A[i], A[k] = A[k], A[i]

T=int(input())

for i in range(T):
    N=int(input())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    A=[int(x) for x in range(N)]
    min=98765
    perm(N,0,0)
    print('#{} {}'.format(i+1,min))
print(time.time() - start_time, 'seconds')




# count = 0
# total = 0
# N = 10
# # 원소의 포함여부 저장 (0, 1)

# def powerset(n, y, sol):      # n: 원소의 갯수, k: 현재depth
#     global min
#
#     if n == y:          # Basis Part
#         if min>=sol:
#             min=sol
#     else:               # Inductive Part
#         for k in range(N):
#             if A[k] == 1:
#                 continue
#             A[k] = 1        # k번 요소 O
#             powerset(n, y + 1, sol+data[y][k])  # 다음 요소 포함 여부 결정
#             A[k] = 0       # k번 요소 X
#
# # print("호출회수 : {}".format(total) )
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     A = [0 for _ in range(N)]
#     data = [list(map(int, input().split())) for _ in range(N)]
#     min=98765
#     powerset(N, 0, 0)
#     print(min)
#     print(time.time() - start_time, 'seconds')