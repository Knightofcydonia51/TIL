import sys
sys.stdin=open('phone_book.txt')



def solution(phone_book):
    answer = True

    for i in range(len(phone_book)-1):
        for k in range(i+1,len(phone_book)):
            if len(phone_book[i])<=len(phone_book[k]):
                for j in range(len(phone_book[i])):
                    if phone_book[i][j]!=phone_book[k][j]:
                        break
                    if j==len(phone_book[i])-1:
                        answer=False
                        return answer
    return answer


li=["123", "456", "789", "4567","11111","22222"]
li.sort()
print(li)
print(solution(sorted(li)	))



