def solution(n):
    answer = ''
    num=8



    while True:
        remain = n % num
        n = n//num
        if n<num:
            answer+=str(remain)+str(n)
            break
        else:
            answer+=str(remain)


    return answer[::-1]


n=200
print(solution(n))