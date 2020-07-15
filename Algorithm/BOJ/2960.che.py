import sys
sys.stdin=open('2960.che.txt')

def val():
    for i in range(len(numbers)):
        cnt = 0
        for k in range(1,numbers[i]+1):
            if numbers[i]%k==0:
                cnt+=1
        if cnt==2:
            P=k # 가장 작은 소수 P
        for k in range(len(numbers)):
            if numbers[k]%P==0: #P의 배수들을 set에 담음
                erased.add(numbers[k])
                if len(erased)==K: #set의 길이가 K번째에 도달하면, 해당 숫자 출력
                    print(numbers[k])
                    return

N,K=map(int,input().split())
numbers=[int(x) for x in range(2,N+1)]
anscnt=0
erased=set([])
val()
