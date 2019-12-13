import sys
sys.stdin=open('14501.quit.txt')

def powerset(r,k,ans):
    global maxi
    if ans > maxi:
        maxi = ans

    if r>=N or k>=N:return
    if data[k][0] > N - r: return
        # 남은 기간보다 상담 기간이 길때
        #남은 날짜보다 상담 기간이 길때?
        # powerset(r, k + 1, ans)
        # data 내에서 해당 데이터의 인덱스값으로부터 시작해서 일수만큼 반복
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