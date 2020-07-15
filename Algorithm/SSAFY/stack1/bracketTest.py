import sys
sys.stdin=open("bracketTest.txt")

def push(i,s):
    s+=i

def isEmpty(s):
    return True if len(s)==0 else False

T=int(input())
for i in range(T):
    code=input()
    sheet=[]
    for j in code:
        if j=='(' or j=='{':
            push(j,sheet)
        elif j==')' and isEmpty(sheet)==False:
            if sheet[-1]=='(':
                sheet.pop()
            else:
                push(j,sheet)
        elif j=='}' and isEmpty(sheet)==False:
            if sheet[-1]=='{':
                sheet.pop()
        elif j=='}' or j==')' and isEmpty(sheet)==True:
            push(j,sheet)
    if isEmpty(sheet):
        print('#{} 1'.format(i+1))
    else:
        print('#{} 0'.format(i + 1))





























