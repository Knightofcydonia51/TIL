import sys
sys.stdin=open('9205.Beer.txt')




t=int(input())

for i in range(t):
    n=int(input())
    sheet=[list(map(int,input().split())) for x in range(n+2)]
    print(sheet)







