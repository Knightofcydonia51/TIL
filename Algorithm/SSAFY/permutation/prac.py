
def comb(r,k):
    if len(arr)-k<n-r:return  # 고를 수 있는 숫자의 개수 < 고를 수 있는 남은 칸
    if r==n:
        print(T)
    else:
        if k<5 and r<n:
            T[r]=arr[k]
            comb(r+1,k+1)
            comb(r,k+1)
# lenarr-(lenarr-n)<r ==> 이러면안돼
arr=list(range(1,6))

n=3
T=[0]*n
comb(0,0)
