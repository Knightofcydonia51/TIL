
arr=[0,1,1,1,0,0,0, 1,0,0,0,0,0,1]

for i in range(2):
    n=0
    for j in range(i*7, i*7+7, 1):
        n=n*2+arr[j]
    print(n,end=" ")
print()