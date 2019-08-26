import sys
sys.stdin=open("metal_stick.txt",  'rt', encoding='UTF8')


T=int(input())

for i in range(T):
    N=input()
    sticks=[int(x) for x in input().split()]
    nasa=[]
    mini=9999
    minidx=0
    ans=[]
    for j in range(0,len(sticks),2):
        nasa.append([sticks[j],sticks[j+1]])
    end=len(nasa)

    for idx,k in enumerate(nasa):
        if k[1]<mini:
            mini=k[1]
            minidx=idx
    ans.append(nasa[minidx]); na
    print(nasa[minidx])

    #2개씩 골라냄
    #가장 작은 후위 s를 가진 집합 색출
    #이 집합의 후위와 일치하는 전위를 가진 집합 색출
    #이 집합의 후위가 다시 가장 작은 후위 s가ㅏ 됨.



# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     screw_list = list(map(int, input().split()))
#     f, b = [], []
#     ans = []
#     start, index = 0, 0
#
#     for i in range(N * 2):
#         if i % 2 == 0:
#             f.append(screw_list[i])
#         else:
#             b.append(screw_list[i])
#
#     for i in range(len(f)):
#         if f[i] not in b:
#             start = f[i]
#             ans = [f[i]] + [b[i]]
#
#     while len(ans) < len(screw_list):
#         if ans[-1] == f[index]:
#             ans += [f[index]] + [b[index]]
#             index = 0
#         else:
#             index += 1
#
#     print('#{}'.format(tc), end=" ")
#     for a in ans:
#         print(a, end=" ")
#     print()