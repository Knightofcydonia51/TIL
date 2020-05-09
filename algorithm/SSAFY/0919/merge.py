import sys
sys.stdin=open('merge.txt')

def merge(left,right):
    global cnt
    result=[]
    i,j=0,0
    if left[-1]>right[-1]:cnt+=1
    while len(left) > i or len(right) >j:
        if len(left)>i and len(right)>j:
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        elif len(left)>i:
            result.append(left[i])
            i+=1
        elif len(right)>j:
            result.append(right[j])
            j+=1
    return result

def merge_sort(m):
    if len(m)==1:return m

    middle=len(m)//2

    left=m[0:middle]
    right=m[middle:len(m)]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge(left,right)


T=int(input())
for i in range(T):
    N=int(input())
    num=[int(x) for x in input().split()]
    cnt=0
    print('#{} {} {}'.format(i+1,merge_sort(num)[N//2],cnt))
