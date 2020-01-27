import sys
sys.stdin=open('15686.chicken.txt')

def powerset(k):
    cnt = 0
    for i in range(len(A)):
        if A[i]:
            cnt += 1
    if cnt > M:
        return
    global mini

    if len(store) == k:
        ans = []
        for i in range(len(store)):
            if A[i]:
                ans.append(store[i])
        if len(ans) == M:
            whioleDis = 0
            for i in range(len(house)):
                chickenDis = 100
                for k in range(len(ans)):
                    if abs(house[i][1] - ans[k][1]) + abs(house[i][0] - ans[k][0]) < chickenDis:
                        chickenDis = abs(house[i][1] - ans[k][1]) + abs(house[i][0] - ans[k][0])
                whioleDis += chickenDis
            if whioleDis < mini:
                mini = whioleDis

    else:
        A[k] = 1
        powerset(k + 1)
        A[k] = 0
        powerset(k + 1)


# 전체 치킨집 좌표에서 M개 부분집합만 제외하고 다 폐업시켜보면서 구하기
N, M = map(int, input().split())
city = [[int(x) for x in input().split()] for y in range(N)]
store = []
house = []
for y in range(N):
    for x in range(N):
        if city[y][x] == 2:
            store.append([y, x])
        elif city[y][x] == 1:
            house.append([y, x])

A = [0] * len(store)  # 순서바꿔주는 리스트
mini = 987654
powerset(0)
print(mini)