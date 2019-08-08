def tentotwo(n):
    l=[]
    while 1:
        quo = int(n / 2)
        l.insert(0, str(n % 2))
        n=int(n/2)
        if quo==1:
            l.insert(0,str(quo))
            ans=''.join(l)
            break
    return ans

print(tentotwo(9))