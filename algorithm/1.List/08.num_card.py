import sys
sys.stdin=open("08.num_card_input.txt")
# T=int(input())
# for i in range(T):
#     N=int(input())
#     data=input()
#     counts=[0]*10
#     for k in data:
#         counts[int(k)]+=1
#     for idx, j in enumerate(counts):
#         if j==max(counts):
#             maxest=idx
#     print('#{} {} {}'.format(i+1,maxest,max(counts)))





    # while data:
    #     C[data%10]+=1
    #     data //= 10

def find(data, C):

    for k in data:
        C[int(k)]+=1

    maxIndex = -1
    for i in range(10):
        if C[maxIndex]<= C[i]:
            maxIndex=i
    return maxIndex

T=int(input())
for test_case in range(T):
    C=[0]*10
    N=int(input())

    data=input()
    ans=find(data,C)

    print("#{} {} {}".format(test_case, ans, C[ans]))