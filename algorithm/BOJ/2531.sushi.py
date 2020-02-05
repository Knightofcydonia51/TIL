import sys
sys.stdin=open('2531.sushi.txt')

N,d,k,c=map(int,input().split())
sushi=[int(input()) for x in range(N)]

maxi=0
for i in range(N):
    eat = set([])
    cnt = 0
    for j in range(k):
        if i<N-k+1:
            eat.add(sushi[i+j])
        else:
            if i+j<N:
                eat.add(sushi[i + j])
            else: #초과시
                eat.add(sushi[cnt])
                cnt+=1
            # i가 N-k를 초과한 수만큼 ( i- (N-k)
    eat.add(c)
    if maxi<len(eat):
        maxi=len(eat)

print(maxi)

