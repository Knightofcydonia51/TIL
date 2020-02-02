import sys
sys.stdin=open('2531.sushi.txt')

N,d,k,c=map(int,input().split())
sushi=[int(input()) for x in range(N)]

maxi=0
for i in range(N-k+1):
    eat = set([])
    for j in range(k):
        eat.add(sushi[i+j])
    eat.add(c)
    if maxi<len(eat):
        maxi=len(eat)

print(maxi)