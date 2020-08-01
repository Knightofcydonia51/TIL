# 4번 단기기억상실증

user_input = [i for i in input().split()]
answer=[]
val=set([])
for i in range(1,len(user_input)+1):
    for k in range(i):
        answer.append(user_input[k])

    if len(set(answer))>5:
        while len(val)<5:
            if answer[-1] not in val:
                val.add(answer[-1])
                print(answer.pop(),end=" ")
            else:
                answer.pop()
        print()
    else:
        while answer:
            if answer[-1] not in val:
                val.add(answer[-1])
                print(answer.pop(),end=" ")
            else:
                answer.pop()
        print()
    val=set([])