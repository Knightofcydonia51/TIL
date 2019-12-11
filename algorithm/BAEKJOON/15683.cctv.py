

# 각 cctv를 돌려보면서 그때마다 사각지대의 개수를 측정
# min을 돌려 최소크기 출력
# 0은 사각지대, 6은 벽, 1~5는 cctv
import collections
import sys
sys.stdin=open('15683.cctv.txt')




# for문으로 모든 카메라의 좌표와 카메라 종류, 종류에 따른 경우의 수 저장 (ex:종류가 1번이면 4 저장)
# 모든 경우의 수들을 더해서 검증 돌릴 for문의 횟수를 저장
# 경우의 수만큼의 수열 만들기
# for문 : if list[0]==1:  if list[2](경우의수)==4:list[1](카메라좌표) 에서 시작
# 해서 왼쪽 다칠하고 1빼고,
#

#연산자(방향) 리스트 = for문 돌려서 각 카메라 종류별로 담김/. (이 리스트의 내부 합만큼 dfs)
# 카메라리스트...에 담겨야하는건 좌표, 카메라 종류, 방향값
# dfs(0,카메라리스트[0]=info)
# 경우의 수가 다 돌았다면, info에는 모든 경우의 수의 좌표값과 그 카메라의 방향값, 종류가 담겨 있을 것이다.
# 각 카메라별 방향값을 담고있는 list=ari
# info[[종류, 방향값, 좌표],[],[]]
# cameralist[[종류, 방향값, 좌표],[] ]
# for i in len(ari)
# ari[i]-=1
# if cameralist[0][0]==1:
#   info.append([0번카메라의 종류,cameralist[i][1],cameralist[i][2]])
#   dfs(d+1,info)

def dfs(d,info):
    # global cameraList
    if len(info)==len(cameraList):
        print(info)
        info=[]
        d=0
        for k in range(len(cameraList)):
            cameraList[k][3]=1
        print('gigigi')

    for i in range(len(cameraList)):
        cameraList[i][1] -= 1
        if cameraList[i][0]==1 and cameraList[i][1]+1 and cameraList[i][3]:
            info.append([cameraList[i][0],cameraList[i][1],cameraList[i][2]])
            cameraList[i][3]=0
            dfs(d+1,info)
        elif cameraList[i][0]==2 and cameraList[i][1]+1 and cameraList[i][3]:
            info.append([cameraList[i][0],cameraList[i][1],cameraList[i][2]])
            cameraList[i][3] = 0
            dfs(d+1,info)
        elif cameraList[i][0]==3 and cameraList[i][1]+1:
            info.append([cameraList[i][0],cameraList[i][1],cameraList[i][2]])
            dfs(d+1,info)
        elif cameraList[i][0]==4 and cameraList[i][1]+1:
            info.append([cameraList[i][0],cameraList[i][1],cameraList[i][2]])
            dfs(d+1,info)
        elif cameraList[i][0]==5 and cameraList[i][1]+1 and cameraList[i][3]:
            info.append([cameraList[i][0],cameraList[i][1],cameraList[i][2]])
            cameraList[i][3] = 0
            dfs(d+1,info)
        cameraList[i][1]+=1


N,M=map(int, input().split())
sheet=[[int(x) for x in input().split()]for y in range(N)]
cctvNum=[1,2,3,4,5]
cameraList=collections.deque([])
watch=0

for y in range(N):
    for x in range(M):
        if sheet[y][x] in cctvNum:
            direction = 0
            if sheet[y][x]==1:
                direction=4
                cameraList.append([sheet[y][x],direction,(y,x),1])
            elif sheet[y][x] == 2:
                direction = 2
                cameraList.append([sheet[y][x], direction, (y, x), 1])
            elif sheet[y][x] == 3:
                direction = 4
                cameraList.append([sheet[y][x],direction,(y,x),1])
            elif sheet[y][x] == 4:
                direction = 4
                cameraList.append([sheet[y][x],direction,(y,x),1])
            elif sheet[y][x] == 5:
                direction = 1
                cameraList.append([sheet[y][x],direction,(y,x),1])
limit=0
for i in range(len(cameraList)):
    limit+=cameraList[i][1]
print(limit)
dfs(0,[])