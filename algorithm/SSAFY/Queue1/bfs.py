# def bfs(v): #v=시작점
#     queue=[]
#     queue.append(v)
#     visited[v]=1
#     print(v, end=" ")
#     while len(queue)!=0:
#         v=queue.pop(0)
#         for w in range(1,V+1):
#             if G[v][w]==1 and visited[w]==0:
#                 queue.append(w)
#                 visited[w]=1    # visited[v+1]
#                 print(w,end=" ")
#
# V=7 #노드수
# E=8 #간선수
# nodes=[1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7] #간선정보
#
# G=[[0 for x in range(V+1)]for y in range(V+1)] # 맵
# visited=[0 for x in range(V+1)]
#
# for i in range(0,len(nodes),2): # 간선정보 입력
#     G[nodes[i]][nodes[i+1]]=1
#     G[nodes[i+1]][nodes[i]] = 1
#
# for i in range(V+1):
#     print("{} {}".format(i, G[i]))
# bfs(1)


#------------------------------------------------------시작점과 가장 멀리 있는 노드와 거리를 구하고 싶을때

def bfs(v): #v=시작점
    queue=[]
    queue.append(v)
    visited[v]=1
    print(v, end=" ")
    while len(queue)!=0:
        v=queue.pop(0)
        for w in range(1,V+1):
            if G[v][w]==1 and visited[w]==0:
                queue.append(w)
                visited[w]= visited[v]+1
                print(w,end=" ")

V=7 #노드수
E=8 #간선수
nodes=[1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7] #간선정보

G=[[0 for x in range(V+1)]for y in range(V+1)] # 맵
visited=[0 for x in range(V+1)]

for i in range(0,len(nodes),2): # 간선정보 입력
    G[nodes[i]][nodes[i+1]]=1
    G[nodes[i+1]][nodes[i]] = 1

for i in range(V+1):
    print("{} {}".format(i, G[i]))
bfs(1)
print()
print(visited)
print(visited.index(max(visited)))
# d
