#1. 파일 쓰기(oldschool)

# f=open('ssafy.txt', 'w')
# for i in range(10):
#     f.write(f'This is line {i}.\n')
# f.close()

#2-1. 파일 쓰기(new one)

# with open('with_ssafy.txt','w') as f:
#     for i in range(10):
#         f.write(f'This is line {i}.\n')

#2-2. 파일쓰기(newest)

with open('writelines.txt', 'w') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])