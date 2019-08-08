def mul(n):
    try:
        list(map(int,a.split(',')))
        i=1
        cnt=n[0]
        while len(n)>i:
            cnt=cnt*n[i]
            i+=1
    except:
        return '에러발생'
    else:
        return cnt

a=input()
print(mul(a))