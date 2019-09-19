
def merge(left,right):
    result=[]
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


# A=[11,45,23,81,28,34]
A=[11,45,22,81,23,34,99,22,17,8]
# A=[1,1,1,1,1,0,0,0,0,0]
print(merge_sort(A))
