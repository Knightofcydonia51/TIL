import sys
sys.stdin=open('inorder.txt')

for i in range(10):
    N=int(input())
    info=[[0 for x in range(4)]for y in range(N)]
    for j in range(N):
        temp=input().split()
        if len(temp)==4:
            info[j][0]=int(temp[0])
            info[j][1] = temp[1]
            info[j][2] = int(temp[2])
            info[j][3]= int(temp[3])
        elif len(temp)==3:
            info[j][0] = int(temp[0])
            info[j][1] = temp[1]
            info[j][2] = int(temp[2])
        elif len(temp)==2:
            info[j][0] = int(temp[0])
            info[j][1] = temp[1]

    print(info)
