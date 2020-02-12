import sys
sys.stdin=open('17281.baseball.txt')

from copy import deepcopy
from collections import deque

def game(T):
    base=deque([])
    out=0
    while out<3:
        for i in range(9):
            if T[i]:
                base.appendleft(1)
                for k in range(T[i]-1):
                    base.appendleft(0)
            else:
                out+=1
                if out==3:
                    break



def perm(k):
    global one
    if k==8:
        T=deepcopy(A)
        T.append(one)
        T[3],T[8]=T[8],T[3]
        base=[]



    else:
        for i in range(k,8):
            A[k],A[i]=A[i],A[k]
            perm(k+1)
            A[k], A[i] = A[i], A[k]

N= int(input())
innings=[list(map(int,input().split())) for x in range(N)]
ans=0

for i in range(len(innings)):
    maxi=0
    A=innings[i][1:]
    one=innings[i][0]
    perm(0)


