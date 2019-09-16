import sys
sys.stdin=open('hexaCode.txt')

T=int(input())
decryptor=['1123','']


for i in range(T):
    N, M = map(int, input().split())
    code=''
    for k in range(N):
        wholetext=input()[::-1]
        if wholetext.isdigit()==True:
            continue
        else:
            code=wholetext.replace('0','')
        print(code)

