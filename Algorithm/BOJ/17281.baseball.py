# import sys
# sys.stdin=open('17281.baseball.txt')
#
# import itertools
# import collections
# import copy
#
# # itertools.permutations(l,8)
#
# def game():
#     for i in range(len(innings)):
#         maxi = 0
#         A = innings[i]
#         zeros = 0
#         T = collections.deque([])
#         for k in range(1, 9):
#             if A[k]:
#                 T.append(A[k])
#             else:
#                 zeros += 1
#     global zeros
#     global maxi
#     bases=collections.deque([0,0,0])
#     score=0
#     out=0
#     if len(T)<3:
#         for i in range(3-len(T)):
#             T.append(0)
#
#     # 3보다 작으면 3- (len(T) 만큼 0이 추가되야함.
#     T.append(A[0])
#     print(T)
#     T[3], T[0] = T[0], T[3]
#     print(T)
#     for i in range(len(T)):
#         if T[i]:
#             bases.appendleft(1)
#             if bases.pop():
#                 score += 1
#             else:
#                 pass
#             for k in range(T[i]-1):
#                 bases.appendleft(0)
#                 if bases.pop():
#                     score += 1
#                 else:
#                     continue
#
#         else:
#             out+=1
#             if out==3:
#                 break
#
#     if score>maxi:
#         maxi=score
#
#
# def perm(k):
#     if k==len(T):
#         game()
#     else:
#         for i in range(k,len(A)):
#             T[k],T[i]=T[i],T[k]
#             perm(k+1)
#             T[k], T[i] = T[i], T[k]
#
#
# # 타순을 정한다.
# #
#
#
# N= int(input())
# innings=[list(map(int,input().split())) for x in range(N)]
# ans=0
# maxi=0
#
# perm(0)
#
# print(maxi)
#
#
#
#
#
#

import pandas as pd

data=[{ 'category_list': [{'category': '땡초김밥'}, {'category': '오뎅'}],'menu_list': [{'menu': '스페셜비빔밥', 'price': 5000}, {'menu': '양념오뎅', 'price': 3000}, {'menu': '참치비빔밥', 'price': 4500}, {'menu': '날치알 비빔밥', 'price': 4500}, {'menu': '치즈떡볶이(소)', 'price': 4000}, {'menu': '치즈떡볶이(대)', 'price': 5000}, {'menu': '양념우동', 'price': 4000}, {'menu': '양념라면', 'price': 3500}, {'menu': '날치알/참치김밥', 'price': 3000}, {'menu': '꼬마김밥', 'price': 4000}, {'menu': '김밥', 'price': 2500}, {'menu': '튀김오뎅', 'price': 2500}, {'menu': '잡채만두', 'price': 3000}, {'menu': '고기만두', 'price': 3000}, {'menu': '반반만두', 'price': 3000}, {'menu': '납작만두', 'price': 2500}]}]
stores = []  # 음식점 테이블
# reviews = []  # 리뷰 테이블


for d in data:
    print(d)
    categories = [c["category"] for c in d["category_list"]]
    menus = [m["menu"] for m in d["menu_list"]]
    prices=[p["price"] for p in d["menu_list"]]
    stores.append(
        [

        ]
    )

