import sys
sys.stdin=open('2382.microorganism.txt')

T=int(input())

for i in range(T):
    N,M,K=map(int,input().split())
    # 셀의 크기, 시간, 군집 개수
    micro=[list(map(int,input().split())) for i in range(K)]
    # y위치, x위치, 미생물 수, 이동방향


    sheet=[[(0,0,0) for x in range(N)]for y in range(N)]
    for y in range(N):
        for x in range(N):
            if y==0:
                sheet[y][x]= -1
            elif y<N-1:
                if x==0 or x==N-1:
                    sheet[y][x]= -1
            else:
                sheet[y][x]= -1


    for k in range(1,M+1):
        new=[]

        for m in range(len(micro)):
            y,x,num,direc=micro[m][0],micro[m][1],micro[m][2],micro[m][3]
            if direc==1: #상
                y-=1
            elif direc==2: #하
                y+=1
            elif direc==3: #좌
                x-=1
            else: #우
                x+=1

            if sheet[y][x]!= -1: #정상 땅일때
                if sheet[y][x][0]<k: #겹치지 않는 셀
                    new.append([y,x,num,direc,num]) # [4]의 값은 최신값
                    sheet[y][x]=(k,m,len(new)-1) #현재 시간, micro 내에서 자신의 인덱스, new 내에서 자신의 인덱스
                else: #겹치는 셀
                    microIndex=sheet[y][x][1]   # 3
                    newIndex=sheet[y][x][2]     # 3
                    new[newIndex][2] += num

                    if micro[microIndex][2]<num: # 갱신 필요
                        new[newIndex][4] = num
                        new[newIndex][3] = direc
                        sheet[y][x]=(k,m,newIndex)
            else:
                if direc == 1:  # 상
                    direc=2
                elif direc == 2:  # 하
                    direc=1
                elif direc == 3:  # 좌
                    direc=4
                else:  # 우
                    direc=3
                num=num//2
                new.append([y,x,num,direc])

        micro=new
    ans=0
    for j in range(len(micro)):
        ans+=micro[j][2]
    print('#{} {}'.format(i+1,ans))






