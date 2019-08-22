import sys
sys.stdin=open("strSearch.txt",  'rt', encoding='UTF8')

for i in range(10):
    N=input()
    pattern=input()
    text=input()
    print("len:", len(text))
    for j in range(len(text)-1,len(pattern)-2,-1):
        print(j)
        # for k in range(len(pattern)):
        #     if text[j]!=pattern[len(pattern)-k-1]:



# text = 'a pattern matching algorithm'
# pattern = 'rithm'
# s = pattern[::-1]
# skip = list(range((len(pattern))))
# print(skip)
#
# print(s)
# i = len(pattern) - 1
# result = 0
#
# while i < len(text):
#     nxt = len(s)
#     j = 0
#     if s[j] == text[i]:
#         while j < len(s):
#             if s[j] != text[i - j]:
#                 break
#             j += 1
#         if j == len(s):
#             result = 1
#     else:
#         while j < len(s):
#             if s[j] == text[i]:
#                 nxt = min(j, nxt)
#                 break
#             j += 1
#     if result:
#         break
#     i += nxt
#
# print(result)