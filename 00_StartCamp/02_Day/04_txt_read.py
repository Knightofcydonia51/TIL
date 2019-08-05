#1-1. 파일 읽기(read - oldschool)

# f=open('ssafy.txt', 'r')
# all_text=f.read()
# print(all_text)
# f.close()

#1-2. 파일 읽기(read - new one)

# with open('with_ssafy.txt', 'r') as f:
#     all_text=f.read()
#     print(all_text)

#2-1. 파일 읽기(readlines() - oldschool)
# f=open('ssafy.txt', 'r')
# lines=f.readlines()
# for line in lines:
#     print(lines)
#     print(line)

# f.close()

#2-2. 파일 읽기(readlines() - new one)

with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print()
        print(line.strip())
