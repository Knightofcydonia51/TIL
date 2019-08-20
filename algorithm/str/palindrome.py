import sys
sys.stdin=open("palindrome.txt")

for i in range(10):
    N=int(input())
    wholetext=''
    text=''
    ans=0
    for t in range(8):
        text=input()
        wholetext+=text
        for j in range(len(text)-N+1):
            pal=''
            pal2=''
            for k in range(N):
                pal+=text[j+k]
                pal2+=text[j+N-k-1]

            if pal==pal2:
                ans+=1

    for s in range(8):
        for j in range(len(text)-N+1):
            pal=''
            pal2=''
            for k in range(N):
                pal+=wholetext[s+j*8+(k*8)]
                pal2+=wholetext[s+j*8+((N-1-k)*8)]
            if pal==pal2:
                ans+=1
    print('#{} {}'.format(i+1,ans))
