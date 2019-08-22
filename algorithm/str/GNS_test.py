import sys
sys.stdin=open("GNS_test.txt")

T=int(input())
for i in range(T):
    N=input()
    text=input().split()
    numlist=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dict={}
    ans=''
    for num in text:
        if dict.get(num):
            dict[num]+=1
        else:
            dict[num]=1
    print('#{}'.format(i+1))
    for j in numlist:
        for k in range(dict.get(j)):
            print(j,end=' ')
            if k==dict.get(j)-1:
                print(j+' ')
