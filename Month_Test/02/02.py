import sys
sys.stdin=open("02.txt")

def Perm(n,k,my_reach):
    global my_result
    if my_reach>=my_result:
        return
    if k == n:
        my_result=my_reach
    else:
        for i in range(k,n):
            data[k],data[i]=data[i],data[k]
            for dd in range(k,n):
                my[k],my[dd]=my[dd],my[k]
                for l in range(len(info)):
                    for j in range(len(info[l])):
                        if info[l][j]==data[k]+1:
                            i_start = l
                            j_start = j
                        elif info[l][j]==my[k]:
                            i_finish = l
                            j_finish = j
                my_reach+=abs(i_finish - i_start)
                my_reach+=abs(j_finish - j_start)
                Perm(n,k+1,my_reach)
                my[k], my[dd] = my[dd], my[k]
            data[k], data[i] = data[i], data[k]



T=int(input())
for tc in range(1,T+1):
    _=int(input())
    info=[list(map(int,input().split())) for _ in range(10)]
    my_num=11
    my = [11, 12, 13, 14, 15, 16]
    for i in range(len(info)):
        for j in range(len(info)):
            if info[i][j]==9:
                info[i][j]=my_num
                my_num+=1
    data=[z for z in range(6)]
    my_result=987654321
    Perm(6,0,0)
    print("#{} {}".format(tc,my_result))