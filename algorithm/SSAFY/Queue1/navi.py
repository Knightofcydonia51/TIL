import sys
sys.stdin=open('navi.txt')


def bfs(s):
    global flag
    visited[s]=1
    queue=[]
    queue.append(s)
    while len(queue)!=0:
        v=queue.pop(0)
        if v==99:
            flag+=1
            return
        for w in range(len(sheet)):
            if sheet[v][w]==1 and visited[w]==0:
                queue.append(w)
                visited[w]=1

V=100
for i in range(10):
    S,M=map(int,input().split())
    way=[int(x) for x in input().split()]
    sheet=[[0 for x in range(V+1)] for y in range(V+1)]
    visited=[0 for x in range(V+1)]

    for j in range(0,len(way),2):
        sheet[way[j]][way[j+1]]=1

    flag=0
    bfs(S)
    print('#{} {}'.format(i+1, flag))

