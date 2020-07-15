import sys
sys.stdin=open('10to2.txt')

T=int(input())

for i in range(T):
    N=float(input())
    cal=N
    binary=''
    while True:
        if len(binary)>12:
            binary='overflow'
            break
        cal=cal*2
        if cal//1>=1:
            binary+='1'
            cal = cal % 1
            if cal==0:
                break
        else:
            binary+='0'

    print('#{} {}'.format(i+1,binary))
