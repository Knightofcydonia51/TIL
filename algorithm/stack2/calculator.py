import sys
sys.stdin=open("calculator.txt")

cal=['*','+']

for i in range(10):
    length=input()
    sik=input()
    stack=[]
    num=[]
    for j in sik:
        if j not in cal and j!='(' or j!=')': #숫자일때
            num.append(j)
        else:
            if j=='(':
                num.append(j)
            


    print(num)


    # for j in num:
    #     if j not in cal:
    #         stack.append(int(j))
    #     else:
    #         a=stack[-1]
    #         stack.pop()
    #         b=stack[-1]
    #         stack.pop()
    #         if j=='+':
    #             stack.append(a+b)
    #         else:
    #             stack.append(a*b)
    # print(stack)





    # 먼저 순회를 전부 다 해서 괄호의 갯수를 세서 저장.
    # 그 괄호의 갯수에 도달할때까지 다시 스캔.
    # 도달하면 그 안의 내용들 계산해서 저장 후 pop?
