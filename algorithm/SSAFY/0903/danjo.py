import sys
sys.stdin=open("danjo.txt")

T=int(input())

for i in range(T):
    N=int(input())
    numbers=[int(x) for x in input().split()]
    danjo=[]
    for j in range(N-1):
        for k in range(j+1,N):
            num=str(numbers[j] * numbers[k]) # 단조보다 작은건 미리 가지치기
            if len(danjo)>=1 and int(num)<max(danjo):
                continue
            temp=''
            for l in range(len(num)):
                if temp<=num[l]:
                    temp=num[l]
                elif temp>num[l]:
                    break
                if l==len(num)-1:
                    danjo.append(int(num))

    if danjo:
        print('#{} {}'.format(i+1,max(danjo)))
    elif len(danjo)==0:
        print('#{} -1'.format(i + 1))

    # 1번째부터 N번째 수 사이 2개 수의 곱이 단조인 값 중 가장 큰 값

