def solution(arrangement):
    answer = 0
    stack=[]
    weight=0
    flag=0

    for i in arrangement:
        if i=="(":
            if stack:
                if stack[-1]=="(":
                    flag=1
                    weight+=1
                    answer+=1
                    stack.append(i)
                elif stack[-1]==")":
                    stack.append(i)



            else:
                stack.append(i)


        elif i == ")":
            if stack[-1]=="(": # 레이저
                answer+=weight*1
                stack.append(i)

            elif stack[-1]==")":
                weight-=1
                stack.append(i)

                if not weight:
                    flag=0
                    stack=[]

    return answer

#쇠막대기 / 레이저 문제

# 레이저 쏠 때 쇠막대기 안인지 여부 flag
# flag는 stack[-1]이 "(" 일때, i="(" 라면 1로 한다.
# weight는 stack[-1]이 ")" 면서, i가 ")"일때 감소,
# flag가 1이면서 stack[-1]이 "(" 일때, i="(" 라면 증가
# weight 감소 직후 weight가 0인지 검사하고, 만약 0이라면 스택 초기화, flag도 0으로 초기화



#

arrangement="()(((()())(())()))(())"
print(solution(arrangement))
