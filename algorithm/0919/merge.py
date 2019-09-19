import sys
sys.stdin=open('merge.txt')

def merge(left,right):
    global cnt
    result=[]
    if left[-1]>right[-1]:cnt+=1
    while len(left) > 0 or len(right) >0:

        if len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left)>0:
            result.append(left.pop(0))
        elif len(right)>0:
            result.append(right.pop(0))
    return result

def merge_sort(m):
    if len(m)==1:return m

    left=[]
    right=[]
    middle=len(m)//2

    for x in range(middle):
        left.append(m[x])
    for x in range(middle,len(m),1):
        right.append(m[x])
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)


T=int(input())
for i in range(T):
    N=int(input())
    num=[int(x) for x in input().split()]
    cnt=0
    print('#{} {} {}'.format(i+1,merge_sort(num)[N//2],cnt))
