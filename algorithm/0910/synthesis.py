import sys
sys.stdin=open('synthesis.txt')

def parentOrder(node,cnt):
    if info[node][2]!=0:
        info[node][3]+=cnt
        parentOrder(info[node][2],cnt)

T=int(input())

for i in range(T):
    N,M,L=map(int,input().split())

    nodes = []
    if N % 2 == 0:  # N이 홀수라면 -> n=N//2   N이 짝수라면 -> N-1//2
        for j in range(1, N // 2):  # 1 2 1 3 2 4 2 5 3 6 3 7     n n*2 n n*2+1
            nodes.append(j);
            nodes.append(j * 2);
            nodes.append(j);
            nodes.append(j * 2 + 1)
        nodes.append(N // 2);
        nodes.append((N // 2) * 2);
    else:
        for j in range(1, (N // 2) + 1):
            nodes.append(j);
            nodes.append(j * 2);
            nodes.append(j);
            nodes.append(j * 2 + 1)
    info = [[0 for x in range(4)] for y in range(N + 1)]
    for j in range(0, len(nodes) - 1, 2):  # [0,0,0][2,3,0][4,5,1][6,7,1]
        if info[nodes[j]][0] == 0:
            info[nodes[j]][0] = nodes[j + 1]
            info[nodes[j + 1]][2] = nodes[j]
        else:
            info[nodes[j]][1] = nodes[j + 1]
            info[nodes[j + 1]][2] = nodes[j]
    for j in range(M):
        node,cnt=map(int,input().split())
        info[node][3]=cnt
        parentOrder(info[node][2],cnt)
    print('#{} {}'.format(i+1,info[L][3]))