import sys
sys.stdin=open("04.forth.txt")

T=int(input())
oper=['+','*','/','-','.']

for i in range(T):
    sik=input().split()
    ans = []
    for j in sik:
        if j not in oper:
            ans.append(int(j))
        elif j in oper:
            if j=='.':
                if len(ans)!=1:
                    print('#{} error'.format(i+1))
                else:
                    print('#{} {}'.format(i+1, ans.pop()))
            elif len(ans)>=2:
                if j=='/':
                    a=ans.pop()
                    b=ans.pop()
                    ans.append(b//a)
                elif j=='*':
                    a = ans.pop()
                    b = ans.pop()
                    ans.append(b * a)
                elif j == '+':
                    a = ans.pop()
                    b = ans.pop()
                    ans.append(b + a)
                elif j == '-':
                    a = ans.pop()
                    b = ans.pop()
                    ans.append(b - a)
            elif len(ans) == 1 and j!='.':
                print('#{} error'.format(i + 1))
                break