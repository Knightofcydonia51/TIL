# import sys
# sys.stdin=open('10844.stair.txt')
#
# N=int(input())
#
# for i in range


ans=0
for i in range(10000000,100000000):
    if abs(int(str(i)[0])-int(str(i)[1]))==1 and abs(int(str(i)[1])-int(str(i)[2]))==1 and  abs(int(str(i)[2])-int(str(i)[3]))==1 and  abs(int(str(i)[3])-int(str(i)[4]))==1 and abs(int(str(i)[4])-int(str(i)[5]))==1 and abs(int(str(i)[5])-int(str(i)[6]))==1 and abs(int(str(i)[6])-int(str(i)[7]))==1:
        ans+=1



print(ans)

# ans=0
# for i in range(10,100):
#     if abs(int(str(i)[0])-int(str(i)[1]))==1:
#         ans+=1

# 9 17 32 61 116 222 424
#  8  15 29 55 108
#    7  14 26 53