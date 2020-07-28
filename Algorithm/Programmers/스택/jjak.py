def solution(s):
    answer = 0
    stack=[]
    for i in s:
        if stack:
            if stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    if stack:
        return 0
    else:
        return 1

s="cdcd"
#s="abcdefgxyz"
print(solution(s))