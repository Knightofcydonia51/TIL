import sys
sys.stdin=open("7510.continuitySum.txt")

T=int(input())

for i in range(T):
    num=int(input())
    hap=0
    ans=0
    for k in range(1,num+1):
        hap = 0
        for j in range(k,num+1):
            hap+=j
            if hap==num:
                ans+=1
                break
            elif hap>num:
                break
    print('#{} {}'.format(i+1,ans))