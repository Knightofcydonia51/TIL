def fib_loop(n):
    result=[1,1]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
    print(result)
    return result[-1]

fib_loop(int(input()))