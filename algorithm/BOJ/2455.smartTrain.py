import sys
sys.stdin=open('2455.smartTrain.txt')

maxi=0
human=0
for i in range(4):
    getOut, getIn=map(int,input().split())
    human+=(getIn-getOut)
    if human>maxi:
        maxi=human
print(maxi)

