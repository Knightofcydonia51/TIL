# for i1 in range(1,4):
#     for i2 in range(1,4):
#         if i2!= i1:
#             for i3 in range(1,4):
#                 if i3!=i1 and i3!= i2:
#                     print(i1,i2,i3)


# data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# result = 0
# maxHeight = 0
# for i in range(len(data)):
#    maxHeight = len(data) - (i+1)
#    for j in range (i+1, len(data), 1):
#        if data[i] <= data[j]:
#            maxHeight -= 1
#        if result < maxHeight:
#            result = maxHeight
# print(result)

# num=456789
# print(num%10)
# c=[0]*12
#
# for i in range(6):
#     c[num%10]+=1
#     num//=10
#     print(c)
#     print(num)
#
# # //=	왼쪽 변수에서 오른쪽 값을 나눈 몫의 결과를 왼쪽변수에 할당
#
# a=[55,7,78,12,42]
# for i in range(len(a)-1,0,-1):
#     for j in range(0,i):
#         if a[j]>a[j+1]:
#             a[j], a[j+1]=a[j+1], a[j]
# print(a)

# T=int(input())
# for tc in range(T):
#     row, col = map(int, input().split())
#     data=[[0 for _ in range(col)] for _ in range(row)]
#     print(data)
#     owndata=[[0]*5]*3
#     print(owndata)
#     for i in range(row):
#         data[i]=list(map(int,input().split()))
#     print(data)
#
#     for i in range(row):
#         for j in range(col):
#             print(data[i][j])
#     print(data)

#예제1
'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''
# def isWall(x,y):
#     if x<0 or x>=5 : return True
#     if y<0 or y>=5 : return True
#     return False
# def calAbs(y,x):
#     if y-x>0 : return y-x
#     else : return x-y
#
# arr=[0*5]*5
# for i in range(5):
#     arr[i]=list(map(int,input().split()))
# print(arr)
# dx=[0,0,-1,1]
# dy=[-1,1,0,0]
# sum=0
# print(len(arr))
# for x in range(len(arr)):
#     for y in range(len(arr[x])):
#         for i in range(4):
#             testX=x+dx[i]
#             testY=y+dy[i]
#             if isWall(testX, testY)==False:
# #                 sum+=calAbs(arr[x][y], arr[testX][testY])
# #
# # print("sum={}".format(sum))
#
# # arr=[[1,2,3],[4,5,6],[7,8,9]]
# #
# # #i:행의 좌표(len(arr))
# #j:열의 좌표(len(arr[0]))
# for i in range(3):
#     for j in range(3):
#         if i < j:
#             arr[i][j], arr[j][i]= arr[j][i], arr[i][j]
#
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end=" ")
#     print()

# bit=[0,0,0,0]
# for i in range(2):
#     bit[0]=i
#     for j in range(2):
#         bit[1]=j
#         for k in range(2):
#             bit[2]=k
#             for l in range(2):
#                 bit[3]=l
#                 print(bit)
#
# def printList(data, bit):
#    for i in range(len(bit)):
#        if bit[i]: print(data[i], end=" ")
#    print()

# arr=[1,2,3]
# n=len(arr)
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end= ",")
#     print()

# def sequentialSearch(a, n, key):
#     i=0
#     while i<n and a[i]!=key:
#         i+=1
#     if i<n : return i
#     else : return -1
#
# data=[4,9,11,23,2,19,7]
# key=119
# print(sequentialSearch(data, len(data), 119))

# def binarySearch(a, key):
#     start =0
#     end=len(a)-1
#     while start<=end:
#         middle=(start+end) // 2
#         if key==a[middle]:
#             return middle
#         elif key <a[middle]:
#             end=middle-1
#         else:
#             start=middle+1
#     return -1
#
# key=19
# data=[2,4,7,9,11,19,23]
# print(binarySearch(data,key))

# a=[4,9,11,2,34,77,54]
# def Selection(l):
#     for i in range(len(l)):
#         min=9999
#         for k in range(i+1,len(l)):
#             if l[k]<min:
#                 min=l[k]
#                 l[i],l[k]=l[k],l[i]
#     return l
# print(Selection(a))


