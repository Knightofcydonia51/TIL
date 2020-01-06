import sys

# ㄴ
sero1_yx=[[0,0],[-1,0],[-1,0],[0,1]]
garo1_yx=[[0,0],[-1,0],[0,-1],[0,-1]]
rsero1_yx=[[0,0],[-1,0],[-1,0],[0,-1]]
rgaro2_yx=[[0,0],[0,1],[0,1],[1,0]]

# thunder
th_sero_yx=[[0,0],[1,0],[0,1],[1,0]]
th_garo_yx=[[0,0],[0,-1],[-1,0],[0,-1]]
th_rsero_yx=[[0,0],[1,0],[0,-1],[1,0]]

# ㅗ
mountain_garo_yx=[[0,0],[1,-1],[1,0],[1,1]]
mountain_left_yx=[[0,0],[-1,-1],[0,-1],[1,-1]]



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

def garo2_niun(y,x): # 가로가 긴 ㄱ 대칭 (역방향)
    hap=0
    for i in range(4):
        hap += sheet[y + sero1_yx[i][1]][x + sero1_yx[i][0]]
    return hap

def rsero1_niun(y,x): # 세로가 긴 ㄴ 대칭
    hap = 0
    for i in range(4):
        hap += sheet[y + rsero1_yx[i][0]][x + rsero1_yx[i][1]]
    return hap

def rsero2_niun(y,x): #세로가 긴 ㄱ 대칭 (역방향)
    hap = 0
    for i in range(4):
        hap += sheet[y + sero1_yx[i][0]][x + sero1_yx[i][1]]
    return hap

def rgaro1_niun(y,x): # 가로 긴 ㄴ모양 (역방향탐색)
    hap = 0
    for i in range(4):
        hap += sheet[y + rsero1_yx[i][1]][x + rsero1_yx[i][0]]
    return hap

def rgaro2_niun(y,x): # 가로 긴 ㄱ모양
    hap = 0
    for i in range(4):
        hap += sheet[y + rgaro2_yx[i][0]][x + rgaro2_yx[i][1]]
    return hap

def th_sero(y,x):
    hap=0
    for i in range(4):
        hap+=sheet[y+th_sero_yx[i][0]][x+th_sero_yx[i][1]]
    return hap

def th_garo(y,x):
    hap = 0
    for i in range(4):
        hap += sheet[y + th_garo_yx[i][0]][x + th_garo_yx[i][1]]
    return hap

def th_rsero(y,x):
    hap = 0
    for i in range(4):
        hap += sheet[y + th_rsero[i][0]][x + th_rsero_yx[i][1]]
    return hap

def th_rgaro(y,x): #
    hap = 0
    for i in range(4):
        hap += sheet[y + th_sero_yx[i][1]][x + th_sero_yx[i][0]]
    return hap

def mountain_garo(y,x):
    hap = 0
    for i in range(4):
        hap += sheet[y + mountain_garo_yx[i][0]][x + mountain_garo_yx[i][1]]
    return hap

def mountain_left(y,x):
    hap = 0
    for i in range(4):
        hap += sheet[y + mountain_left_yx[i][0]][x + mountain_left_yx[i][1]]
    return hap

def mountain_reverse(y,x):
    hap = 0
    for i in range(4):
        hap += sheet[y + mountain_left_yx[i][1]][x + mountain_left_yx[i][0]]
    return hap

def mountain_right(y,x):
    hap = 0
    for i in range(4):
        hap += sheet[y + mountain_garo_yx[i][1]][x + mountain_garo_yx[i][0]]
    return hap

N,M=map(int,input())
sheet=[[int(x) for x in input().split()]for y in range(N)]
for y in range(N):
    for x in range(M):
        sero_stick(y,x)
        garo_stick(y,x)
        square(y,x)



# 포인터 같은곳에 두고 델타 유효하지 않으면 리턴 0
# y축 N-1 까지는