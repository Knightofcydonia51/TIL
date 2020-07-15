import sys
sys.stdin=open('4014.airstrip.txt')


T=int(input())

for i in range(T):
    N,X=map(int,input().split())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    ans=0
    for y in range(N):
        flag = 0
        q = [sheet[y][0]]
        visited = [0] * N
        for x in range(1, N):
            if flag==1:
                break
            else:
                tmp=q.pop()
                if tmp==sheet[y][x]:
                    q.append(sheet[y][x])
                else:
                    if sheet[y][x]==tmp+1: # 뒤로 X칸만큼 확인
                        for z in range(1,X+1):
                            if x-z>-1:
                                if sheet[y][x-z]==tmp:
                                    if visited[x-z]==0:
                                        visited[x-z]=1

                                    else:
                                        flag=1
                                        break
                                else: # X보다 짧아서 경사로 설치가 불가능한 케이스
                                    flag=1
                                    break
                            else: # 맵 바깥으로 가는 케이스
                                flag=1
                                break
                        if flag==0:
                            q.append(sheet[y][x])
                    elif sheet[y][x]==tmp-1: # 앞으로 X칸만큼 확인
                        for z in range(X):
                            if x + z <N:
                                if sheet[y][x + z] == tmp-1:
                                    if visited[x + z] == 0:
                                        visited[x + z]=1
                                    else:
                                        flag = 1
                                        break
                                else:  # X보다 짧아서 경사로 설치가 불가능한 케이스
                                    flag = 1
                                    break
                            else:  # 맵 바깥으로 가는 케이스
                                flag = 1
                                break
                        if flag==0:
                            q.append(sheet[y][x])
                    else: # 높이가 2 이상 차이날때
                        flag=1
                        break
        if flag==0:
            ans+=1

    for x in range(N):
        flag = 0
        q = [sheet[0][x]]
        visited = [0] * N
        for y in range(1, N):
            if flag == 1:
                break
            else:
                tmp = q.pop()
                if tmp == sheet[y][x]:
                    q.append(sheet[y][x])
                else:
                    if sheet[y][x] == tmp + 1:  # 뒤로 X칸만큼 확인
                        for z in range(1,X+1):
                            if y - z > -1:
                                if sheet[y-z][x] == tmp:
                                    if visited[y - z] == 0:
                                        visited[y - z] = 1
                                    else:
                                        flag = 1
                                        break
                                else:  # X보다 짧아서 경사로 설치가 불가능한 케이스
                                    flag = 1
                                    break
                            else:  # 맵 바깥으로 가는 케이스
                                flag = 1
                                break
                        if flag == 0:
                            q.append(sheet[y][x])
                    elif sheet[y][x] == tmp - 1:  # 앞으로 X칸만큼 확인
                        for z in range(X):
                            if y + z < N:
                                if sheet[y+z][x] == tmp - 1:
                                    if visited[y + z] == 0:
                                        visited[y + z] = 1
                                    else:
                                        flag = 1
                                        break
                                else:  # X보다 짧아서 경사로 설치가 불가능한 케이스
                                    flag = 1
                                    break
                            else:  # 맵 바깥으로 가는 케이스
                                flag = 1
                                break
                        if flag == 0:
                            q.append(sheet[y][x])
                    else:  # 높이가 2 이상 차이날때
                        flag=1
                        break
        if flag == 0:
            ans += 1
    print('#{} {}'.format(i+1,ans))


    # 가로 먼저 스캔
    # 각 줄별로 먼저 평탄한지 아닌지를 확인
    # 아니라면, 검증
    # 높이차가 2 이상 난다면 바로 다음 줄로 스킵
    # 높이차가 1 나는 구간이 있다면(abs=1), 그 구간 밑으로 X만큼의 여유가 있는지 확인
    # 있다면 활주로 건설+=1 하고 넘어감
