import sys
sys.stdin=open('14502.lab.txt')

import copy

def bfs(y,x,sheet2,visited):

    q=[(y,x)]
    while q:
        y,x=q.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
            ny=y+i[0]
            nx=x+i[1]
            if -1<ny<N and -1<nx<M:
                if sheet2[ny][nx]==0 and visited[ny][nx]==0:
                    sheet2[ny][nx]=3
                    q.append((ny,nx))
                    visited[ny][nx]=1


def comb(n,r):
    global maxi
    if r==0:

        sheet2 = copy.deepcopy(sheet)
        visited = [[0 for y in range(M)] for y in range(N)]

        for i in range(3):
            sheet2[zeros[T[i]][0]][zeros[T[i]][1]]=1

        for i in range(len(virus)):
            bfs(virus[i][0],virus[i][1],sheet2,visited)

        # 0의 개수 세기
        num = 0
        for y in range(N):
            for x in range(M):
                if sheet2[y][x] == 0:
                    num += 1


        if maxi<num:
            maxi=num

    else:
        if n<r:
            return
        else:
            T[r-1]=A[n-1]
            comb(n-1,r-1)
            comb(n-1,r)



# 조합
# bfs 한개, 조합 1개
N,M = map(int,input().split())
sheet=[[int(x) for x in input().split()]for y in range(N)]

zeros=[]
virus=[]
maxi=0


for y in range(N):
    for x in range(M):
        if sheet[y][x]==0:
            zeros.append([y,x])
        elif sheet[y][x]==2:
            virus.append([y,x])

T=[0]*3
A=range(len(zeros)+1)

comb(len(zeros),3)
print(maxi)