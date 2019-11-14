import sys
sys.stdin=open('makeNumber.txt')

def dfs(d,ans):
    global mini, maxi
    if d == N-1:
        if ans<mini:
            mini=ans
        if ans>maxi:
            maxi=ans
    for k in range(len(ari)):
        ari[k] -= 1

        if k == 0 and ari[0]>0:
            dfs(d+1,ans+num[d+1])
        elif k == 1 and ari[1]>0:
            dfs(d + 1, ans-num[d+1])
        elif k==2 and ari[2]>0:
            dfs(d + 1, ans * num[d+1])
        elif k==3 and ari[3]>0:
            dfs(d + 1, int(ans / num[d+1]))

        ari[k] += 1
T=int(input())

for i in range(T):
    N=int(input())
    ari=[int(x) for x in input().split()]
    num=[int(x) for x in input().split()]

    maxi=(-987654321)
    mini=987654321
    dfs(0,num[0])
    print('#{} {}'.format(i+1,abs(maxi-mini)))