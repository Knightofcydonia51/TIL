import sys
sys.stdin=open("binarySearch2.txt")

def binary_find(start,end,find,cnt):
    global flag
    mid=(start+end)//2
    if info_N[mid] == find:
        flag+=1
        # data.append(find)
        return
    if  (cnt==0 or cnt==2) and info_N[mid] > find:
        return binary_find(start,mid-1,find,1)
    elif (cnt==0 or cnt==1) and info_N[mid] < find:
        return binary_find(mid+1,end,find,2)

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    info_N=list(map(int,input().split()))
    info_M = list(map(int, input().split()))
    flag=0
    info_N=sorted(info_N)
    data=[]
    for i in range(len(info_M)):
        if info_M[i] in info_N:
            if info_M[i]==info_N[(len(info_N)-1)//2]:
                flag+=1
                data.append(info_M[i])
            else:
                binary_find(0,len(info_N)-1,info_M[i],0)
    print("#{} {}".format(tc,flag))




