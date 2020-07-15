import sys
sys.stdin=open('sero.txt')


T=int(input())

for i in range(T):
    words=[[x for x in input()]for y in range(5)]
    maxi=max(len(z) for z in words)
    sheet = [['#' for x in range(maxi)] for y in range(5)]
    for y in range(len(words)):
        for x in range(len(words[y])):
            sheet[y][x]=words[y][x]
    ans=''
    for y in range(maxi):
        temp=''
        for x in range(5):
            temp+=sheet[x][y]
        ans+=temp
    ans=ans.replace('#','')
    print('#{} {}'.format(i+1,ans))

