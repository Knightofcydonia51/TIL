import sys
sys.stdin=open("numSpin.txt")


T=int(input())

for i in range(T):
    N=int(input())
    numbers=[[x for x in input().split()]for y in range(N)]
    ans=[]
    for x in range(N):
        temp =''
        temp2=''
        temp3=''
        for y in range(N-1,-1,-1): #2 1 0
            temp+=numbers[y][x]
            temp2+=numbers[N-1-x][y]
            temp3+=numbers[N-y-1][N-1-x]
        ans.append(temp); ans.append(temp2); ans.append(temp3)
    print("#{}".format(i + 1))
    for k in range(N):
        for j in range(3):
            print(ans[j+(k*3)], end=" ")
        print("")