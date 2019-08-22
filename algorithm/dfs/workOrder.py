import sys
sys.stdin=open("workOrder.txt")

def dfs(v):
    visited[v]=1 # visited[1]=1
    print(v,end=" ") # 1

    for w in range(V+1):
        if G[v][w]==1 and visited[w]==0:
            dfs(w)

for i in range(1):
    V, E= map(int,input().split())
    temp=list(map(int,input().split())) # 1 4 1 3 2 3 2 5 4 6
    print(temp)

    G = [[0 for i in range(V + 1)] for j in range(V + 1)] #노드수 +1을 지도로 받음.
    visited = [0 for i in range(V + 1)]

    for k in range(0, len(temp), 2):
        G[temp[k+1]][temp[k]] = 1  # 거꾸로 입력받음.
        # 룰 : 거꾸로 입력받으면 뿌리를 알 수 있음.
        # 후위에 2번이상 위치해있는 놈은 제거
        # 그다음 for문으로 다 돌려서, 제일 뒤에 위치해 있는 애들을 전부 리스트에 담음.
        # 중복을 제거하면 뿌리만 남는다?


    for i in range(V + 1):
        print("{} {}".format(i, G[i]))

    dfs(1)





