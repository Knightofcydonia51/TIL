import sys
sys.stdin=open('17281.baseball.txt')

import collections
import copy


def game():
    global zeros
    global maxi
    bases=collections.deque([0,0,0])
    score=0
    out=0
    for i in range(zeros):
        T.append(0)
    T.appendleft(A[0])
    T[3], T[0] = T[0], T[3]
    print(T)
    for i in range(len(T)):
        if T[i]:
            bases.appendleft(1)
            if bases.pop():
                score += 1
            else:
                pass
            for k in range(T[i]-1):
                bases.appendleft(0)
                if bases.pop():
                    score += 1
                else:
                    continue

        else:
            out+=1
            if out==3:
                break

    if score>maxi:
        maxi=score


def perm(k):
    if k==len(T):
        game()
    else:
        for i in range(k,len(A)):
            T[k],T[i]=T[i],T[k]
            perm(k+1)
            T[k], T[i] = T[i], T[k]


N= int(input())
innings=[list(map(int,input().split())) for x in range(N)]
ans=0
maxi=0

for i in range(len(innings)):
    maxi=0
    A=innings[i]
    zeros=0
    T = collections.deque([])
    for k in range(1,9):
        if A[k]:
            T.append(A[k])
        else:
            zeros+=1

    perm(0)

print(maxi)





