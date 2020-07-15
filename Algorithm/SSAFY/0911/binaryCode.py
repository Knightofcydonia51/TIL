import sys
sys.stdin=open('binaryCode.txt')

T=int(input())
decryptor=['1011000','1001100','1100100','1011110','1100010','1000110','1111010','1101110','1110110','1101000']

for i in range(T):
    N,M=map(int,input().split())
    code=''
    ans=''
    for k in range(N):
        wholetext=input()[::-1]
        if '1' in wholetext:
            text=wholetext
    for j in range(len(text)):
        if text[j]=='1':
            for u in range(56):
                code+=text[j+u]
            break

    for k in range(0,56,7):
        num = ''
        for j in range(7):
            num+=code[j+k]
        if num==decryptor[0]:
            ans+='0'
        if num==decryptor[1]:
            ans+='1'
        if num==decryptor[2]:
            ans+='2'
        if num==decryptor[3]:
            ans+='3'
        if num==decryptor[4]:
            ans+='4'
        if num==decryptor[5]:
            ans+='5'
        if num==decryptor[6]:
            ans+='6'
        if num==decryptor[7]:
            ans+='7'
        if num==decryptor[8]:
            ans+='8'
        if num==decryptor[9]:
            ans+='9'

    ans=ans[::-1]
    odd=0
    even=0
    for x in range(1,len(ans)+1):
        if x%2==0:
            even+=int(ans[x-1])
        else:
            odd+=int(ans[x-1])
    result=odd * 3 + even
    odd=odd+even
    if result%10==0:
        print('#{} {}'.format(i+1,odd))
    else:
        print('#{} 0'.format(i+1))