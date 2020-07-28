
def convert(u):
    u=u[1:-1]
    a=""
    for i in u:
        if i=="(":
            a+=")"
        else:
            a+="("
    return a


def val(u):
    stack=[]
    for i in u:
        if i=="(":
            if stack:
                stack.append(i)
            else:
                stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True


def devider(p):

    num=[0,0]

    for i in p:
        if i=="(":
            num[0]+=1
        else:
            num[1]+=1
        if num[0]==num[1]:
            return p[:sum(num)],p[sum(num):]


def solution(p):
    answer = ''
    if p=="":
        return ""
    else:
        u,v=devider(p)
        if val(u):
            return u+solution(v)
        else:
            return "(" + solution(v) + ")" + convert(u)


p="()))((()"
print(solution(p))