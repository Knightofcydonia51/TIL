import sys
sys.stdin=open("08.special_sort.txt")

T=int(input())
for i in range(T):
    N=int(input())
    a=[int(x) for x in input().split()]
    ans=''
    for k in range(0,len(a)-1):
        min=k
        for j in range(k+1, len(a)):
            if a[min]>a[j]:
                min=j
        a[k], a[min]=a[min], a[k]
    for x in range(5):
        ans+=" "+str(a[(len(a)-1-x)])
        ans+=" "+str(a[x])
    print('#{}{}'.format(i+1,ans))