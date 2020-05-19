import sys
sys.stdin=open("palindrome2.txt")


def pal(wholetext, i):
    for N in range(100, 0, -1):
        for s in range(100):
            for j in range(100-N+1):
                pal1 = ''
                pal2 = ''
                pal3 = ''
                pal4 = ''
                for u in range(N):
                    pal1 += wholetext[s * 100 + j + u]
                    pal2 += wholetext[s * 100 + j + N - u - 1]
                    pal3 += wholetext[s + j * 100 + (u * 100)]
                    pal4 += wholetext[s + j * 100 + ((N - 1 - u) * 100)]
                if pal1 == pal2:
                    print('#{} {}'.format(i + 1,N))
                    return None
                elif pal3 == pal4:
                    print('#{} {}'.format(i + 1,N))
                    return None

for i in range(10):
    nothing=input()
    wholetext=''
    for k in range(100,0,-1):
        text = input()
        wholetext+=text
    pal(wholetext,i)