
def solution(n, words):
    answer = [0,0]


    clear=[words[0]]
    text=words[0][-1]

    for i in range(1,len(words)):
        if text==words[i][0]:
            text=words[i][-1]
        else:
            qua, remain = divmod(i + 1, n)
            if remain == 0:
                remain = n
                qua -= 1
            return [remain, qua + 1]

        if words[i] in clear:
            qua,remain=divmod(i+1,n)
            if remain==0:
                remain=n
                qua-=1
            return [remain,qua+1]
        else:
            clear.append(words[i])

    return answer


words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
n=3
print(solution(n, words))
