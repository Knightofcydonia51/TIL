def sosu(n):
    for i in range(1,n+1):
        if n%i==0 and i!=1 and i!=n:
            print('소수가 아닙니다.')
            break
        elif i==n:
            print('소수입니다.')
            break

sosu(13)