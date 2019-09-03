import sys
sys.stdin=open("stringCompare.txt")

T=int(input())

for i in range(T):
    str1=input()
    str2=input()
    if str1 in str2:
        print('#{} {}'.format(i+1,1))
    else:
        print('#{} {}'.format(i+1,0))