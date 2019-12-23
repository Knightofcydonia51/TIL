import sys

sero1_yx=[[0,0],[-1,0],[-1,0],[0,1]]
garo1_yx=[[0,0],[-1,0],[0,-1],[0,-1]]
rsero1_yx=[[0,0],[-1,0],[-1,0],[0,-1]]
rgaro2_yx=[]

def sero_stick(y,x):
    hap=0
    for i in range(4):
        hap+=sheet[y-i][x]
    return hap

def garo_stick(y,x):
    hap=0
    for i in range(4):
        hap+=sheet[y][x+i]
    return hap

def square(y,x):
    hap=0
    for i in range(2):
        for j in range(2):
            hap+=sheet[y+i][x+j]
    return hap

def sero1_niun(y,x): #  세로가 긴 ㄴ
    hap=0
    for i in range(4):
        hap+=sheet[y+sero1_yx[i][0]][x+sero1_yx[i][1]]
    return hap

def sero2_niun(y,x): # 세로가 긴 ㄱ (역방향탐색)
    hap=0
    for i in range(4):
        hap += sheet[y + rsero1_yx[i][0]][x + rsero1_yx[i][1]]
    return hap

def garo1_niun(y,x): # 가로가 긴 ㄴ 대칭
    hap=0
    for i in range(4):
        hap += sheet[y + garo1_yx[i][0]][x + garo1_yx[i][1]]
    return hap

def garo2_niun(y,x): # 가로가 긴 ㄱ 대칭
    hap=0
    for i in range(4):
        hap += sheet[y + sero1_yx[i][1]][x + sero1_yx[i][0]]
    return hap

def rsero1_niun(y,x): # 세로가 긴 ㄴ 대칭
    hap = 0
    for i in range(4):
        hap += sheet[y + rsero1_yx[i][0]][x + rsero1_yx[i][1]]
    return hap

def rsero2_niun(y,x):
    hap = 0
    for i in range(4):
        hap += sheet[y + garo1_yx[i][1]][x + garo1_yx[i][0]]
    return hap

def rgaro1_niun(y,x): # 가로 긴 ㄴ모양 (역방향탐색)
    hap = 0
    for i in range(4):
        hap += sheet[y + rsero1_yx[i][1]][x + rsero1_yx[i][0]]
    return hap

def rgaro2_niun(y,x): # 가로 긴 ㄱ모양
    

N,M=map(int,input())
sheet=[[int(x) for x in input().split()]for y in range(N)]




# 포인터 같은곳에 두고 델타 유효하지 않으면 리턴 0
# y축 N-1 까지는