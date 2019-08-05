#1. 평균을 구하세용

score={
    '수학':80,
    '국어':90,
    '음악':100
}

print(sum(score.values())/len(score))


#2. 전체 평균

score={
    'a': {
        '수학':80,
        '국어':90,
        '음악':100
    },
    'b': {
        '수학':80,
        '국어':90,
        '음악':100
    }
}

sum1=0
sum2=0
for i in score.values():
    for k in i.values():
        sum1+=k
        sum2+=1
print(sum1/sum2)


#3. 여러개
city={
    '서울':[-6,-10,5],
    '대전':[-3,-5,2],
    '광주':[0,-2,10],
    '부산':[2,-2,9]
}

#1. 도시별 최근 3일의 온도 평균은?
for value in city.values():
    print(sum(value)/len(value))


#2. 도시 중 최근 3일 중에 가장 추웠던, 가장 더웠던 곳은?
all=[]
for value in city.values():
    for tem in value:
        all+=value
print(max(all),min(all))

#3.서울은 영상 2도였던 적이 있나요?
