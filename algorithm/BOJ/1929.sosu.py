import sys

sys.stdin=open("1929.sosu.txt")




M, N=map(int, input().split())
memo=[]

for i in range(1,int(N**0.5)+1):


