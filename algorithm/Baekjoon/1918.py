import sys
sys.stdin=open("tomato.txt")

ans= -1
N=int(input())
people=[int(x) for x in input().split()]
node=[list(map(int, input().split())) for _ in range(N)]
