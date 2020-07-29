def solution(s):

    all=[]
    num=[]
    text=""
    flag=0
    for i in s[1:-1]:
        if i=="{":
            flag=1
            continue
        elif i=="}":
            flag=0
            num.append(int(text))
            all.append(num)
            num = []
        elif i==",":
            if flag==1:
                num.append(int(text))
                text = ""
                continue
            else:
                text = ""
                continue
        else:
            text+=i


    all=sorted(all,key=lambda x:len(x))

    answer=[all[0][0]]
    for i in range(len(all)):
        for k in range(len(all[i])):
            if all[i][k] not in answer:
                answer.append(all[i][k])

    return answer

s="{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))