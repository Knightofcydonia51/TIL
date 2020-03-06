import sys
sys.stdin=open('1952.swimmingPool.txt')


def oneYear(step,cost):
    global mini
    if cost>mini:
        return
    if step>=11:
        if mini>cost:
            mini=cost
        return
    else:
        oneYear(step+1,cost+day*plan[step+1])
        oneYear(step + 3, cost + three)
        if plan[step + 1]:
            oneYear(step + 1, cost + month)

T=int(input())
for i in range(T):
    day,month,three,year=map(int,input().split())
    plan=[int(x) for x in input().split()]
    con=0
    mini=year
    oneYear(-1,0)
    print(mini)


# 하루 이용권
# 1달 이용권
# 3달 이용권
# 1년 이용권


# 달값/하루 보다 많은 날을 이용한 달은 달값으로 계산 - 값이 1보다 작으면 그냥 무조건 달값으로
# 위에 해당하는 달이 3달 연속 있을 경우 3달 값이랑 비교 - 값이 1보다 작으면 그냥 3달값으로 계산
# 위에 해당하는 분기가 4분기일 경우 1년 값이랑 비교 -값이 1보다 작으면 그냥 년값
