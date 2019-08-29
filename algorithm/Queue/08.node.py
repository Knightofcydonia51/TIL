import sys
sys.stdin = open('08.node.txt', 'r')


def bfs(v):
    global flag
    queue=[]
    queue.append(v)
    visited[v]=1
    while len(queue)!=0:
        v=queue.pop(0)
        for w in range(V+1):
            if sheet[v][w]==1 and visited[w]==0:
                queue.append(w)
                visited[w]=visited[v]+1
                if w==G:
                    flag=visited[w]
                    return


    #S를 입력받고 시작
    #G가 들어왔을시, return하고 cnt 반환

T=int(input())

for i in range(T):
    V,E=map(int,input().split())
    nodes=''
    for j in range(E):
        node=input()
        nodes+=node+' '
    nodes=[int(x) for x in nodes.split()]
    sheet=[[0 for x in range(V+1)]for y in range(V+1)]
    visited=[0 for x in range(V+1)]
    S,G=map(int,input().split())

    for j in range(0,len(nodes),2):
        sheet[nodes[j]][nodes[j+1]]=1
        sheet[nodes[j+1]][nodes[j]]=1

    flag=0
    bfs(S)
    if visited[G]>0:
        print('#{} {}'.format(i+1,flag-1))
    else:
        print('#{} 0'.format(i + 1))




