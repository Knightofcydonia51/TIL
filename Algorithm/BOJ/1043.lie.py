import sys
sys.stdin=open('1043.lie.txt')


# 모든 파티를 순회하며 해당 파티에 진실을 아는 사람이 있었는지를 본다.
# 만약 있었다면, 해당 파티의 두번째 값을 51로 바꾼다.
# 체크를 마친 후에는 처음부터 파티를 순회하며 두번째 값이 51이 아닐 경우, 구라를 친다.

def val(i):
    global ans
    if len(party[i])==1:
        return
    for k in range(1, len(party[i])): # 범위가 0부터 시작할수도 있다
        if party[i][k] in people:
            return
    ans+=1

def rumor(i):
    for j in range(1, len(party[i])):
        people.add(party[i][j])
        trueList.append(i)


N,M = map(int, input().split())
people=[int(x) for x in input().split()]
people=set(people[1:])
party=[list(map(int,input().split())) for x in range(M)]
trueList=[]


for j in range(M):
    for i in range(M):
        if i in trueList:
            continue
        for k in range(0, len(party[i])):
            if len(party[i])==1:
                break
            else:
                if k>0:
                    if party[i][k] in people:
                        print(people)
                        rumor(i)


ans=0
for i in range(M):
    val(i)

print(ans)
