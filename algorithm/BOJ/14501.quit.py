import sys
sys.stdin=open('14501.quit.txt')

def powerset(n,k):
    global maxi
    if n==k:
        ans=[]
        time = [0] * N
        ans = 0
        for i in range(n):
            if A[i]==1:
                #남은 시간이 현재 선택 상담 시간보다 작다면 여기서 리턴
                if i+data[i][0]>N:return
                for k in range(data[i][0]):
                    if time[i+k]==1:return
                    else:time[i+k]=1
                ans+=data[i][1]
        if ans==0:
            pass
        else:
           if maxi<ans:
               maxi=ans
    else:
        A[k]=1
        powerset(n,k+1)
        A[k]=0
        powerset(n,k+1)


N=int(input())
A=[int(x) for x in range(N)]
data= [list(map(int, input().split())) for _ in range(N)]
maxi=0
powerset(N,0)
print(maxi)
