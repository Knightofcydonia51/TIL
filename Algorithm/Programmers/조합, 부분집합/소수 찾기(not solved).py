def powerset(n,k,numbers):
    global A, answer
    if n==k:
        num=""
        for i in range(n):
            if A[i]==1:
                num+=numbers[i]
        if num:
           print(num)
           answer.add(int(num))

    else:
        A[k]=1
        powerset(n,k+1,numbers)
        A[k]=0
        powerset(n, k + 1, numbers)


def val(i):
    if i!=1:
        for k in range(2,i):
            if i%k==0:
                return 0
    else:
        return 0
    return 1

def solution(numbers):
    global A, answer
    answer = set([])
    A = [int(x) for x in range(len(numbers))]

    powerset(len(numbers), 0,numbers)

    ans=0

    for i in answer:
        if val(i):
            ans+=1
        else:
            continue

    return ans

print(solution(["1","7"]))
 # 순서바꿔주는 리스트
 # 돌리고 싶은 집합