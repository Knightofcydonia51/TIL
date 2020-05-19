import sys
sys.stdin=open('arithmetic.txt')

def postOrder(node):
    if node!=0:
        postOrder(int(info[node][2]))
        postOrder(int(info[node][3]))
        if info[node][1] in arith:
            if info[node][1]=='+':
                ans.append(ans.pop()+ans.pop())
            elif info[node][1]=='-':
                first = ans.pop();second = ans.pop()
                ans.append(second-first)
            elif info[node][1]=='/':
                first = ans.pop();second = ans.pop()
                ans.append(second//first)
            else:
                ans.append(ans.pop()*ans.pop())
        else:
            ans.append(int(info[node][1]))

arith=['+','-','*','/']
for i in range(10):
    N=int(input())
    info = [[0 for x in range(5)]for y in range(N+1)]
    ans=[]
    for j in range(N):
        temp=[x for x in input().split()]
        if len(temp)==4:
            info[int(temp[0])][0]=int(temp[0])
            info[int(temp[0])][1]=temp[1]
            info[int(temp[0])][2]=temp[2]
            info[int(temp[0])][3] = temp[3]
        if len(temp)==2:
            info[int(temp[0])][0] = int(temp[0])
            info[int(temp[0])][1] = temp[1]
    postOrder(1)
    print('#{} {}'.format(i+1,ans[0]))