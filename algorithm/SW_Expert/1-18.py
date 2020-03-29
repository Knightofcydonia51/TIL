a=range(1,200)
ans=""
for i in a:
    if i%7==0 and i%5 is not 0:
        ans+=str("{},".format(i))
print(ans[:-1])