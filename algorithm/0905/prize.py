import sys
sys.stdin=open('prize.txt')

T=int(input())

for i in range(T):
    M, N=input().split()
    M = list(M)
    maxnum={}
    for m in range(int(N)):
        temp = list(M)
        for j in range(len(M)):
            for k in range(j+1,len(M)):
                temp[j],temp[k]=temp[k],temp[j]
                print(i+1,j,k,temp) #7 5 7 1 4 8
