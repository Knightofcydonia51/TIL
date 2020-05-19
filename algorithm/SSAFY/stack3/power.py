import sys
sys.stdin=open("power.txt")

def power(n,m):
    if m==1:
        return n
    else:
        return n*power(n,m-1)

for i in range(10):
    N=input()
    num=[int(x) for x in input().split()]
    print('#{} {}'.format(i+1,power(num[0],num[1])))

