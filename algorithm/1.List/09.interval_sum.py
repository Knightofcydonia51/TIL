import sys
sys.stdin=open("interval_sum_input.txt")
T=int(input())
for i in range(T):
    NM = input().split(); M = int(NM[1])
    numlist=[int(x) for x in input().split()]
    interval_list=[]
    for k in range(len(numlist)-M+1):
        interval = 0
        for j in range(M):
            interval+=numlist[k+j]
        interval_list.append(interval)
    interval_list=sorted(interval_list)
    print("#{} {}".format(i+1,interval_list[-1]-interval_list[0]))
