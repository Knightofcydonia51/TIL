ans=""
for i in range(100,301):
    a=int(i/100)
    if a%2==0:
        b=int(i/10)
        if b%2==0:
            if i%2==0:
                ans+=str("{},".format(i))
print(ans[:-1])