import sys, collections
sys.stdin=open('5658.treasureBox.txt')

alphabet=['A','B','C','D','E','F']

T=int(input())

for i in range(T):
    N,K = map(int,input().split())
    numbers=collections.deque([k for k in input()])
    divider=len(numbers)//4
    allnum = set([])
    tmp=''
    for k in range(divider):
        cnt= -1+divider
        for j in range(len(numbers)):
            tmp+=numbers[j]
            if j==cnt:
                cnt+=divider
                ten=0
                for x in range(divider):
                    if tmp[x] in alphabet:
                        for y in range(len(alphabet)):
                            if alphabet[y]==tmp[x]:
                                ten+=(10+y)*(16**(divider-1-x))
                    else:
                        ten+=int(tmp[x])*(16**(divider-1-x))

                allnum.add(ten)
                tmp=''
        numbers.appendleft(numbers.pop())

    allnum=sorted(list(allnum),reverse=True)
    print('#{} {}'.format(i+1,allnum[K-1]))



# 10 = 2
# 100 = 4
# 1000 = 8
# 10000 = 16

# 1000 =
# 100 = 256
# 10 = 16
# FF=255
# F0 = 240
# 1F7 = 256 + 240 + 7
