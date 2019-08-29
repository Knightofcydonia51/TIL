import sys
sys.stdin = open('test.txt', 'r')

T=int(input())

for i in range(T):
    NMK=[int(x) for x in input().split()]
    N=NMK[0]; M=NMK[1]; K=NMK[2]
    #N:행 M:열
    colorMap=[[0 for x in range(M)] for y in range(N)] #열 5개 행 3개
    biggest=[0]

    for j in range(K):
        square=[int(x) for x in input().split()]
        validate = 0
        for k in range(square[0],square[2]+1,1):
            for u in range(square[1],square[3]+1,1):
                if colorMap[k][u]>square[4]:
                    validate+=1
        if validate==0:
            if square[4] not in biggest:
                biggest.append(square[4])
            for k in range(square[0],square[2]+1,1):
                for u in range(square[1],square[3]+1,1):
                    colorMap[k][u]=square[4]
        else:continue
    maxi = 0

    for idx in range(len(biggest)):
        ans=0
        for j in range(N):
            for k in range(M):
                if colorMap[j][k]==biggest[idx]:
                    ans+=1
        if len(biggest)==1:
            maxi=ans
            break
        else:
            if ans>maxi:
                maxi=ans
    print('#{} {}'.format(i+1,maxi))




