# # 4번 단기기억상실증
#
# user_input = [i for i in input().split()]
# answer=[]
# val=set([])
# for i in range(1,len(user_input)+1):
#     for k in range(i):
#         answer.append(user_input[k])
#
#     if len(set(answer))>5:
#         while len(val)<5:
#             if answer[-1] not in val:
#                 val.add(answer[-1])
#                 print(answer.pop(),end=" ")
#             else:
#                 answer.pop()
#         print()
#     else:
#         while answer:
#             if answer[-1] not in val:
#                 val.add(answer[-1])
#                 print(answer.pop(),end=" ")
#             else:
#                 answer.pop()
#         print()
#     val=set([])


#
#
# def solution(n, lost, reserve):
#     answer = 0
#
#
#
#     students=[0 for i in range(n+1)]
#
#     for i in range(len(students)):
#         if i in lost:
#             students[i]-=1
#         if i in reserve:
#             students[i]+=1
#
#     for i in range(1,len(students)):
#         if students[i]==-1:
#             for k in -1,1:
#                 if len(students)>i+k>0:
#                     if students[i+k]==1:
#                         students[i+k]=0
#                         students[i]=0
#
#
#     for i in range(1,len(students)):
#         if students[i]==0 or students[i]==1:
#             answer+=1
#
#     return answer
#
#
# solution(n=5,lost=[1,2,3,4,5], reserve=[])

# import copy
#
#
# def dfs(remain,sheet,loca,handle,step):
#     global answer
#     sheet=copy.deepcopy(sheet)
#     if remain==0:
#         # print(step,sheet)
#         if step<answer:
#             answer=step
#         else:
#             return
#     # print(sheet)
#     for i in range(1,len(sheet)):
#         step += 1
#         if -len(sheet)<loca+handle*i<len(sheet):
#             # print(loca+handle*i)
#             if sheet[loca+handle*i]==1:
#                 sheet[loca+handle*i]=0
#                 dfs(remain-1,sheet,loca+handle*1,handle*1,step) # 전진, 핸들방향 그대로
#                 dfs(remain - 1, sheet, loca+handle*-1, handle*-1,step) # 후진, 핸들방향 반대로
#
#
# def solution(name):
#     global answer
#     answer = 9999
#     alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     sheet=[0 for i in range(len(name))]
#
#     remain=0
#     cnt=0
#     for i in range(len(name)):
#         if name[i] is not "A":
#             for k in range(len(alphabet)):
#                 if alphabet[k] == name[i]:
#                     if k<14:
#                         cnt += k
#                     else:
#                         cnt+= 26-k
#
#             if i==0:
#                 continue
#             else:
#                 sheet[i]=1
#                 remain+=1
#
#     print(remain, cnt)kjnl
#     dfs(remain,sheet,0,1,0)
#     dfs(remain,sheet,0,-1,0)
#
#
#     print(answer+cnt)
#     return answer+cnt
#
# solution(name="BBBAAAB)")
# solution(name="ABABAAAAABA")

# def solution(strs):
#     answer = ""
#
#     strs=sorted(strs)
#
#     for i in strs[0]:
#         if strs[-1].startswith(answer+i):
#             answer+=i
#         else:
#             break
#
#     return answer
#
# solution(strs=["abc", "abcdefg", "abcdhfg"])

def changer(s):
    if len(s)==1:
        return "0"+s
    else:
        return s

def solution(p,n):
    answer = ""

    si=""
    bun=int(p[6]+p[7])
    cho=int(p[9]+p[10])

    if "PM" in p:
        si=12+int(p[3]+p[4])
    elif "AM" in p:
        si = int(p[3] + p[4])

    print(si)
    n_si=divmod(n,3600)
    n_bun=divmod(n_si[1],60)
    n_cho=n_bun[1]

    n_si=n_si[0]+si
    print(n_si)
    n_bun=n_bun[0]+bun
    n_cho=n_cho+cho


    if divmod(n_cho,60):

        n_bun+=divmod(n_cho, 60)[0]
        n_cho=divmod(n_cho, 60)[1]
    if divmod(n_bun,60):
        n_si+=divmod(n_bun, 60)[0]
        n_bun=divmod(n_bun, 60)[1]
    if divmod(n_si, 24):
        n_si = divmod(n_si, 24)[1]

    n_si=changer(str(n_si))
    n_bun=changer(str(n_bun))
    n_cho=changer(str(n_cho))

    answer=n_si+":"+n_bun+":"+n_cho
    print(answer)
    return answer

solution(p="PM 01:01:00", n=10)


# def solution(prices):
#
#     answer=0
#     maxi=0
#     for i in range(len(prices)):
#         for k in range(i,len(prices)):
#             if prices[k]-prices[i]>answer:
#                 answer=prices[k]-prices[i]
#     print(answer)
#
#     return answer
#
# solution(prices=[3, 4, 1, 5, 4])
#
#

def solution(prices):
    small = prices[0]
    answer  = 0
    for i in range(1,len(prices)):
        if prices[i] < small :
            small = prices[i]
        if answer < prices[i] - small :
            answer = prices[i] - small

    return answer


solution(prices=[3, 4, 1, 5, 4])