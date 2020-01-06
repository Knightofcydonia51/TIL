import collections
import sys
sys.stdin = open('17471.gerrymandering.txt')

def bfs(v,graph):
    visit=[0 for x in range(N)]
    visit[v] = 1
    q=collections.deque([v])
    g=[v]
    while q:
        v=q.popleft()
        for w in graph:
            if G[v][w]==1 and visit[w]==0:
                q.append(w)
                visit[w]=1
                g.append(w)
    return sorted(g)

def powerset(n,k):
    global mini
    if n==k:
        first=collections.deque([])
        second=collections.deque([])
        for i in range(n):
            if A[i]==1:
                first.append(i)
            else:
                second.append(i)
        if not first or not second:
            pass
        else:
            a,b=bfs(first[0],first),bfs(second[0],second)

            if list(first)==a and list(second)==b:
                peopleA = 0
                peopleB = 0
                for i in a:
                    peopleA+=people[i]
                for i in b:
                    peopleB+=people[i]
                if abs(peopleA-peopleB)<mini:
                    mini=abs(peopleA-peopleB)
    else:
        A[k]=1
        powerset(n,k+1)
        A[k]=0
        powerset(n, k + 1)

N=int(input())
people=[int(x) for x in input().split()]
info=[list(map(int,input().split())) for _ in range(N)]
A=[int(x) for x in range(N)]
G = [[0 for x in range(N)] for y in range(N)]

for i in range(len(info)):
    for k in range(1,len(info[i])):
        G[i][info[i][k]-1]=1
        G[info[i][k]-1][i]=1

# for y in range(len(G)):
#     print(G[y])
ans= -1
mini=9999
powerset(N,0)
if mini==9999:
    mini= -1
print(mini)






# powerset(N,0)

#부분집합을 돌리고, 부분집합에 속하는 집합과 속하지 않는 집합으로 나눈 후,
# 각각의 집합에서 합을 구하며 bfs를 돌려 서로 연결되있지도 판별한다.



