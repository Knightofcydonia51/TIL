ans=""
for i in range(1,101):
    if i%2==1:
        ans+=str("{}, ".format(i))
print(ans[:-2])