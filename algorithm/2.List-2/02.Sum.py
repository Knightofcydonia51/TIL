import sys
sys.stdin=open("02.Sum.txt")

def hangyeol(l):
    x_max=0
    y_max=0
    for y in range(len(arr)):
        hang_sum = 0
        yeol_sum = 0
        for x in range(len(arr)):
            hang_sum+=arr[y][x]
            yeol_sum+=arr[x][y]
        if hang_sum>x_max:
            x_max=hang_sum
        if yeol_sum>y_max:
            y_max=yeol_sum
    return x_max if x_max>y_max else y_max

def diag(l):
    diag_max=0
    diag_sum_left=0
    diag_sum_right=0
    for xy in range(len(arr)):
        diag_sum_left+=arr[xy][xy]
        diag_sum_right+=arr[len(arr)-1-xy][len(arr)-1-xy]
    return diag_sum_left if diag_sum_left>diag_sum_right else diag_sum_right

arr=[0*100]*100
for i in range(10):
    N=int(input())
    for k in range(100):
        arr[k]=[int(x) for x in input().split()]
    print("#{} {}".format(i+1,hangyeol(arr) if hangyeol(arr)>diag(arr) else diag(arr)))




