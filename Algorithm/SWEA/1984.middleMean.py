import sys
sys.stdin=open("1984.middleMean.txt")

T=int(input())

for i in range(T):
    numbers=[int(x) for x in input().split()]
    mini=99999
    maxi=0
    for idx,j in enumerate(numbers):
        if j<mini:
            mini=j
            minidx=idx
        if j>maxi:
            maxi=j
            maxidx =idx
    if maxidx>minidx:
        numbers.pop(maxidx); numbers.pop(minidx)
    else:
        numbers.pop(minidx); numbers.pop(maxidx)
    ans=round(sum(numbers)/len(numbers))
    print('#{} {}'.format(i+1,ans))