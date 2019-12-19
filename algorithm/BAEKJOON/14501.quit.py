import sys
sys.stdin=open('14501.quit.txt')

def powerset(r,k,ans):
    global maxi
    if ans > maxi:
        maxi = ans
    if r>=N:return
    if data[k][0] > N - r and k!=0:return
    if k==0 and data[k][0]>N-r:
        powerset(r+1,k+1,ans)
    else:
        # 남은 기간보다 상담 기간이 길때 return but k가 끝까지 순회하지 않았다면
        # 끝까지 봐야함
        for i in range(data[k][0]):
            T[r+i]=1
        powerset(r+data[k][0],k+data[k][0],ans+data[k][1])
        for i in range(data[k][0]):
            T[r + i] = 0
        powerset(r+1,k+1,ans)


N=int(input())
T=[0]*N
data= [list(map(int, input().split())) for _ in range(N)]
maxi=0
powerset(0,0,0)
print(maxi)