def factorial(n):
    num=1
    for i in range(1,n+1):
        num=i*num
    return num
print(factorial(int(input())))