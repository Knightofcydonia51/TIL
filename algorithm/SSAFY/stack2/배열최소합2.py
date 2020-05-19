def perm(n, k, cursum):
    global ans
    if ans < cursum: return
    ###############
    if k == n:
        if ans > cursum: ans = cursum
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, cursum + data[k][arr[k]]) # n은 3, k는 1씩 증가, cursum은 배열 탐색중
            arr[k], arr[i] = arr[i], arr[k]

import sys
sys.stdin = open('배열최소합2.txt', 'r')
T = int(input())

for tc in range(T):
    ans = 987654321
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = i
    data = [list(map(int,input().split())) for _ in range (N)]

    perm(N, 0, 0)
    print('#{} {}'.format(tc+1, ans))