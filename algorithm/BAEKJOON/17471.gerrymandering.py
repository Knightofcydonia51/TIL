import collections
import sys
sys.stdin = open('17471.gerrymandering.txt')

def bfs(sheet,v):
    visit=[0 for x in range(N)]
    q=collections.deque([])
    q.append(v)
    while q:
        v = q.popleft()
        for w in range(N):
            if sheet[v-1][w]==1 and visit[w]==0:
                q.append(w)
                

def powerset(n,k):
    if n==k:
        first=[]
        second=[]
        for i in range(n):
            if A[i]==1:
                first.append(i)
            else:
                second.append(i)
        if first==[]:
            pass
        else:
            G = [[0 for x in range(N)] for y in range(N)]
            for i in range(len(first)):
                for k in range(1,info[first[i]][0]+1):
                    G[first[i]][info[first[i]][k]-1] = 1
                    G[info[first[i]][k]-1][first[i]] = 1

            G2= [[0 for x in range(N)] for y in range(N)]
            for i in range(len(second)):
                for k in range(1,info[second[i]][0]+1):
                    G[second[i]][info[second[i]][k]-1] = 1
                    G[info[second[i]][k]-1][second[i]] = 1



    else:
        A[k]=1
        powerset(n,k+1)
        A[k]=0
        powerset(n, k + 1)


N=int(input())
people=[int(x) for x in input().split()]
info=[list(map(int,input().split())) for _ in range(N)]
A=[int(x) for x in range(N)]

powerset(N,0)

# for i in range(len(info)):
#     for k in range(1,len(info[i])):
#         G[i][info[i][k]-1]=1
#         G[info[i][k]-1][i]=1
#
# for y in range(len(G)):
#     print(G[y])



# powerset(N,0)

#부분집합을 돌리고, 부분집합에 속하는 집합과 속하지 않는 집합으로 나눈 후,
# 각각의 집합에서 합을 구하며 bfs를 돌려 서로 연결되있지도 판별한다.


