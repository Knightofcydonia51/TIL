import sys
sys.stdin=open('container.txt')

def cal():
    global ans
    weight = 0
    for k in range(len(container)):
        for j in range(len(truck)):
            if j + weight==len(truck):
                return
            j = weight + j
            if container[k]<=truck[j]:
                ans+=container[k]
                weight+=1
                break
            else:
                break

T=int(input())
for i in range(T):
    N,M=map(int, input().split())
    container=sorted([int(x) for x in input().split()],reverse=True)
    truck = sorted([int(x) for x in input().split()],reverse=True)
    ans = 0
    cal()
    print('#{} {}'.format(i+1,ans))


