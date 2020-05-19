#
# numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand="left"
#
# leftkey=[1,4,7]
# rightkey=[3,6,9]
# middlekey=[2,5,8,0]
# pad=[[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
#
# def delta(y,x,obj):
#     q=[(y,x,0)]
#     while q:
#         y,x,step=q.pop(0)
#         if pad[y][x]==obj:
#             return step,y,x
#         for i in [[1,0],[-1,0],[0,-1],[0,1]]:
#             ny=y+i[0]
#             nx=x+i[1]
#             if -1<ny<4 and -1<nx<3:
#                 q.append((ny,nx,step+1))
#
#
# def solution(numbers, hand):
#     answer = ''
#     lthumb=(3,0)
#     rthumb=(3,2)
#
#     for i in numbers:
#         if i in leftkey:
#             answer+='L'
#             if i==1:
#                 lthumb=(0,0)
#             elif i==4:
#                 lthumb=(1,0)
#             else:
#                 lthumb=(2,0)
#         elif i in rightkey:
#             answer+='R'
#             if i == 3:
#                 rthumb = (0, 2)
#             elif i == 6:
#                 rthumb = (1, 2)
#             else:
#                 rthumb = (2, 2)
#         else:
#             rloca,y,x=delta(rthumb[0], rthumb[1], i)
#             lloca,y,x=delta(lthumb[0], lthumb[1], i)
#             if rloca>lloca: #오른쪽손가락이 더 멀때
#                 answer+='L'
#                 lthumb=(y,x)
#             elif rloca<lloca: #왼쪽손가락이 더 멀때
#                 answer+='R'
#                 rthumb=(y,x)
#             else: # 같을때
#                 if hand=='left':
#                     answer+='L'
#                     lthumb=(y,x)
#                 else:
#                     answer+='R'
#                     rthumb=(y,x)
#     return answer
#
# print(solution(numbers,hand))




# ["+","-","*"]

def solution(expression):
    answer = 0
    for i in expression:
        if i=="*":

        elif i=="-":

        elif i=="+":

    return answer





#
# gems=["x","y","y","y","z","x","y","y","z","x","y","z","x","y","z"]
#
# def solution(gems):
#     answer = []
#
#     allgems=set([])
#     for i in gems:
#         if i in allgems:
#             continue
#         else:
#             allgems.add(i)
#
#     if len(allgems)==1:
#         answer=[1,1]
#         return answer
#
#     else:
#         # listgems=list(allgems)
#         # loca=[]
#         # for i in range(len(listgems)):
#         #     loca.append((listgems[i],0))
#
#         anslist=[]
#         loca={}
#         buying=[]
#         i=0
#         start=0
#         while i<len(gems):
#             if gems[i] in buying:
#                 loca['{}'.format(gems[i])]=i+1
#                 i+=1
#             else:
#                 buying.append(gems[i])
#                 loca['{}'.format(gems[i])] = i + 1
#                 i+=1
#                 if len(buying)==len(allgems):
#                     ans=sorted(list(loca.values()))
#                     anslist.append([ans[0],ans[-1],abs(ans[-1]-ans[0])])
#                     loca={}
#                     buying=[]
#                     start+=1
#                     i=start
#         anslist.sort(key=lambda anslist:anslist[2])
#         answer=[anslist[0][0],anslist[0][1]]
#         return answer
#
# print(solution(gems))



board=[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(y,x,N,board):
    D = [[987654321] * N for i in range(N)]
    q=[]
    q.append((y,x,-1,-500))
    D[0][0]=0
    while q:
        y,x,handle,cost=q.pop(0)
        for i in range(4): # 하 상 좌 우

            ny = y + dy[i]
            nx = x + dx[i]
            if -1<ny<N and -1<nx<N and board[ny][nx]!=1:


                if i==0:
                    if handle!=0:
                        corner=1
                    else:
                        corner = 0

                elif i==1:
                    if handle!=1:
                        corner = 1
                    else:
                        corner = 0

                elif i==2:
                    if handle!=2:
                        corner=1
                    else:
                        corner = 0

                else:
                    if handle!=3:
                        corner = 1
                    else:
                        corner = 0

                if D[ny][nx] >=(cost+100)+corner*500:
                    D[ny][nx] = (cost+100)+corner*500
                    q.append((ny, nx,i,(cost+100)+corner*500))
    print(D)
    return D[N - 1][N - 1]
#
#
# def solution(board):
#     answer = 0
#     answer=bfs(0,0,len(board),board)
#
#     return answer
#
# solution(board)


