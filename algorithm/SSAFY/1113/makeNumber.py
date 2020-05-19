import sys
sys.stdin=open('makeNumber.txt')


def dfs(d, ans):
    global mini, maxi
    if d == N - 1:
        if ans < mini:
            mini = ans
        if ans > maxi:
            maxi = ans
    for k in range(len(ari)):
        if k == 0 and ari[0] > 0:
            ari[0] -= 1
            dfs(d + 1, ans + num[d + 1])
            ari[0] += 1
        elif k == 1 and ari[1] > 0:
            ari[1] -= 1
            dfs(d + 1, ans - num[d + 1])
            ari[1] += 1
        elif k == 2 and ari[2] > 0:
            ari[2] -= 1
            dfs(d + 1, ans * num[d + 1])
            ari[2] += 1
        elif k == 3 and ari[3] > 0:
            ari[3] -= 1
            dfs(d + 1, int(ans / num[d + 1]))
            ari[3] += 1


T = int(input())

for i in range(T):
    N = int(input())
    ari = [int(x) for x in input().split()]
    num = [int(x) for x in input().split()]

    maxi = (-999999999)
    mini = 999999999
    dfs(0, num[0])
    print('#{} {}'.format(i + 1, abs(maxi - mini)))
