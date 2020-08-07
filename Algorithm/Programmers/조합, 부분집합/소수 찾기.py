from itertools import permutations

def val(i):
    if i!=1:
        for k in range(2, i):
            if i%k==0:
                return 0
    else:
        return 0
    return 1

def solution(numbers):

    answer = 0
    numlist=set([])


    for i in range(1,len(numbers)+1):
        perm=permutations(numbers,i)
        for k in perm:
            num=""
            for j in k:
                num+=j
            if int(num):
                numlist.add(int(num))

    for i in list(numlist):
        if val(i)==1:
            answer+=1

    return answer

numbers="011"
print(solution(numbers))