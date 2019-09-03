import sys

sys.stdin = open('05.spin.txt', 'r')

T = int(input())

for i in range(T):
    NM=input().split()
    N=NM[0]; M=int(NM[1])
    Q=input().split()
    for k in range(M):
        Q.append(Q.pop(0))
    print("#{} {}".format(i+1,Q[0]))


