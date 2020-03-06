import sys
sys.stdin=open('2112.film.txt')

import copy

def val(l,flag):
    for x in range(W):
        tmp = [l[0][x]]
        cnt = 1
        for y in range(1, D):
            if cnt == K:
                break
            else:
                if tmp.pop() == l[y][x]:
                    tmp.append(l[y][x])
                    cnt += 1
                else:
                    if y < D - 1:
                        tmp.append(l[y][x])
                        cnt = 0
                    else:
                        return flag
    flag=1
    return flag

def powerset(k):
    if k==D:
        test = copy.deepcopy(sheet)
        for j in range(D):
            if A[j]==1:
                for u in range(W):
                    test[j][u]=1



    else:
        A[k]=1
        powerset(k+1)
        A[k]=0
        powerset(k + 1)





T=int(input())


for i in range(T):
    D,W,K=map(int,input().split())
    sheet=[[int(x) for x in input().split()]for y in range(D)]
    # 사전 테스트
    if val(sheet,0)==1:
        print('#{} 1'.format(i+1))
    else:
        A = [0] * D
        if K==1:
            ans=0
        else:
            powerset(0)