import sys
sys.stdin=open("strNum.txt")

T=int(input())

for i in range(T):
    str1=input()
    str2=input()
    dict={}
    for j in str2:
        for k in str1:
            if j==k:
                if dict.get(k):
                    dict[k] += 1
                    break
                elif j in str1:
                    dict[k] = 1
                    break
    maxi = 0
    for u in str1:
        dict.get(u)
        if maxi<dict.get(u):
            maxi=dict.get(u)
    print('#{} {}'.format(i+1,maxi))




# def bruteForce(text, pattern):
#     for i in range(len(text)-len(pattern)+1):
#         cnt=0
#         for j in range(len(pattern)):
#             if text[i+j]!=pattern[j]:
#                 break
#             else:cnt+=1
#         if (cnt>=len(pattern)) : return i
#     return -1
#
#
# text="TTTTAACCA"
# pattern = "TTA"
# patternLength=len(pattern)
# textLength=len(text)
#
# print(bruteForce(text, pattern))