import sys
sys.stdin=open('1713.candidate.txt')
import collections


N=int(input())
recommend=int(input())
students=[int(x) for x in input().split()]
photo=[students[0]]
recomlist=[0]


for i in range(1,len(students)):
    if len(photo)<N:
        if students[i] in photo:
            for k in range(len(photo)):
                if photo[k]==students[i]:
                    recomlist[k]+=1
        else:
            photo.append(students[i])
            recomlist.append(0)
    else: # 사진틀이 다 채워짐
        if students[i] in photo:
            for k in range(len(photo)):
                if photo[k] == students[i]:
                    recomlist[k] += 1
        else:  # 추천 수가 가장 적은 학생 가려내기
            tmp=[]
            for j in range(len(recomlist)):
                if recomlist[j]==min(recomlist):
                    tmp.append([recomlist[j],j])
            photo.pop(tmp[0][1])
            photo.append(students[i])
            recomlist.pop(tmp[0][1])
            recomlist.append(0)

for i in sorted(photo):
    print(i, end=" ")