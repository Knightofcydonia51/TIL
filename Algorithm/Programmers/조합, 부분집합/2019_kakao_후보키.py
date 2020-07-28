def comb(n,r,q,relation):
    global answer,setter
    if r==0:

        if check:
            for y in check:
                if set(y).issubset(set(T[:q])):
                    return


        val=set([])
        for i in range(len(relation)):
            text=""
            for k in range(q):
                text+=relation[i][T[k]]

            val.add(text)

        if len(val)==len(relation): # 중복이 없다는 것
            check.append(T[:q])
            answer += 1
        else:
            return

        return


    else:
        if n<r:
            return
        else:
            T[r-1]=A[n-1]
            comb(n-1,r-1,q,relation)
            comb(n-1,r,q,relation)


def solution(relation):
    global answer, setter
    answer = 0
    setter=[]
    for i in range(1, len(relation[0])+1):

        comb(len(relation[0]),i,i,relation)

    return answer


T = [0] * 8
A = range(0, 8)
check=[]

relation=[["a","1","4"],
["2","1","5"],
["a","2","4"]]
print(solution(relation))