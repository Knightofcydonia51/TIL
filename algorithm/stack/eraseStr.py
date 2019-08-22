import sys
sys.stdin=open("eraseStr.txt")

T=int(input())
for i in range(T):
    text=input()
    step = 0
    while 1:
        string = ''
        if step==len(text):
            break
        step = 0
        for idx,k in enumerate(text):
            step += 1
            if k==string:
                text=text[:idx-1]+text[idx+1:]
                break
            string=k
    print('#{} {}'.format(i+1,len(text)))
