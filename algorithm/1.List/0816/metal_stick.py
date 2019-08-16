import sys
sys.stdin=open("metal_stick.txt")

T=int(input())
for i in range(T):
    num=int(input())
    boltnut=[int(x) for x in input().split()]
