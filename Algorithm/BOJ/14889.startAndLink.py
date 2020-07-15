import sys
sys.stdin=open('14889.startAndLink.txt')

def cal(t,stat):
    for y in t:
        for x in t:
            if y == x:
                continue
            else:
                stat += sheet[y][x]
    return stat

def comb(r,k):
    global mini
    if mini == 0:
        return
    if N-k < team-r :return
    if r==team:
        start_stats=0
        link_stats=0
        start=[]
        link=[]
        for i in range(N):
            if i in T:
                start.append(i)
            else:
                link.append(i)
        start_stats=cal(start,start_stats)
        link_stats=cal(link,link_stats)
        ans=abs(start_stats-link_stats)

        if mini>ans:
            mini=ans

    else:
        if r<team and k<N:
            T[r]=data[k]
            comb(r+1,k+1)
            comb(r,k+1)

N = int(input( ))
sheet=[[int(x) for x in input().split()]for y in range(N)]
team=N//2
T=[0]*team
data=[int(x) for x in range(N)]
mini=987654321
comb(0,0)
print(mini)


