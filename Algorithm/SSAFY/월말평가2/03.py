import collections


#정상일시 총 괄호 쌍 수
# 비정상이면 -1

# 스택 4개 두고
#

inputString=input()
stack1=[]
stack2=[]
stack3=[]
stack4=[]
answer= 0

for i in inputString:
    if i=='(':
        stack1.append(i)
    elif i==')':
        if stack1:
            if stack1[-1]=='(':
                answer+=1
                stack1.pop()
        else:
            answer= -1
            break
    elif i=='[':
        stack2.append(i)
    elif i==']':
        if stack2:
            if stack2[-1]=='[':
                answer+=1
                stack2.pop()
        else:
            answer= -1
            break
    elif i=='{':
        stack3.append(i)
    elif i=='}':
        if stack3:
            if stack3[-1]=='{':
                answer+=1
                stack3.pop()
        else:
            answer= -1
            break

    elif i=='<':
        stack4.append(i)
    elif i=='>':
        if stack4:
            if stack4[-1]=='<':
                answer+=1
                stack4.pop()
        else:
            answer= -1
            break
    else:
        continue


if stack1 or stack2 or stack3 or stack4:
    answer= -1
print(answer)


# 다 끝났는데 stack들이 비워져있지 않을때


