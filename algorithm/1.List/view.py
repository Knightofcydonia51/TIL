import sys
sys.stdin=open("view_input.txt")
T=10
for i in range(T):
    N=int(input())
    arr = list(map(int,input().split(" ")))
    ans = 0
    for k in range(2,len(arr)-2):
        weight = 0
        if arr[k]>arr[k-2] and arr[k]>arr[k-1] and arr[k]>arr[k+1] and arr[k]>arr[k+2]:
            highest=sorted([arr[k-2],arr[k-1],arr[k+1],arr[k+2]])
            weight=arr[k]-highest[3]
        ans+=weight
    print("#{} {}".format(i+1, ans))

# 1조건 : n-1보다 1이상 커야함, 크면 weight에 가중.
        # 2조건 : n-2보다 1이상
        # 3조건 : n+1보다 1이상
        # 4조건 : n+2보다 1이상 커야함
        # 4개 만족했을시, ans+= 높이 만큼

        #
        # 만약 전 포인터와 전전포인터보다 1이상 크다면, 1,2조건 충족(동시에)