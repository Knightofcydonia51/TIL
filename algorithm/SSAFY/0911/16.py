import sys
sys.stdin=open('16.txt')

text=input()

changer=['0000','0001', '0010', '0011', '0100', '0101', '0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
binary=''

for i in range(len(text)):
    if '0'<=text[i]<='9':
        binary+=changer[int(text[i])]
    else:
        if text[i] == "A":
            binary += (changer[10])
        if text[i] == "B":
            binary += (changer[11])
        if text[i] == "C":
            binary += (changer[12])
        if text[i] == "D":
            binary += (changer[13])
        if text[i] == "E":
            binary += (changer[14])
        if text[i] == "F":
            binary += (changer[15])
print(binary)


