import sys
sys.stdin=open("palindrome3.txt")


def pal(wholetext, i):
    for s in range(N):
        for j in range(N - M + 1):
            pal1 = ''
            pal2 = ''
            pal3 = ''
            pal4 = ''
            for u in range(M):
                pal1 += wholetext[s * N + j + u]
                pal2 += wholetext[s * N + j + M - u - 1]
                pal3 += wholetext[s + j * N + (u * N)]
                pal4 += wholetext[s + j* N + ((M - 1 - u) * N)]
            if pal1 == pal2:
                print('#{} {}'.format(i + 1, pal1))
                return None
            elif pal3 == pal4:
                print('#{} {}'.format(i + 1, pal3))
                return None

T=int(input())
for i in range(T):
    NM=[int(x) for x in input().split()]
    N=NM[0]
    M=NM[1]
    wholetext=''
    for k in range(N):
        text = input()
        wholetext+=text
    pal(wholetext,i)

