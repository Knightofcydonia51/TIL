import sys
sys.stdin=open("06.min_max_input.txt")

T=int(input())
for i in range(T):
    N=int(input())
    data=[int(x) for x in input().split()]
    maxi=0
    mini=99999999
    for k in data:
        if k>maxi:
            maxi=k
        if k<mini:
            mini=k
    print('#{} {}'.format(i + 1, maxi - mini))

