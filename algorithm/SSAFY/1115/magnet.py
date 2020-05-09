from collections import deque as deq
import sys
sys.stdin=open('magnet.txt')


def checker(num,deq,dir):
    val=[0]*4
    val[num]=dir
    cnt=0
    origin=num
    while 1: #오른쪽
        if num<3:
            if deq[num][2] != deq[num + 1][6]:  # 오른쪽
                val[num + 1] = (-val[num])
                num+=1
            else:
                break
        else:
            break

    num=origin
    while 1:
        if num > 0:
            if deq[num][6] != deq[num - 1][2]:  # 왼쪽
                val[num - 1] = (-val[num])
                num-=1
            else:
                break
        else:
            break

    for i in range(len(val)):
        if val[i]==1:
            deq[i].appendleft(deq[i].pop())
        elif val[i]==(-1):
            deq[i].append(deq[i].popleft())


T=int(input())

for i in range(T):
    K=int(input())
    sheet=[deq(int(x) for x in input().split()) for y in range(4)]
    spin=[[int(x) for x in input().split()] for y in range(K)]
    ans = 0
    for j in range(K):
        check = []
        num,dir=spin[j][0]-1,spin[j][1] # 1이면 시계방향, -1이면 반시계

        checker(num,sheet,dir)

    for k in range(4):
        ans += sheet[k][0] << k

    print('#{} {}'.format(i+1, ans))