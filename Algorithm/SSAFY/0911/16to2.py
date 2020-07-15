import sys
sys.stdin=open('16to2.txt')


T=int(input())
changer=['0000','0001', '0010', '0011', '0100', '0101', '0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']

for tc in range(T):
    N,hexa = input().split()
    binary=''
    for i in range(len(hexa)):
        if '0' <= hexa[i] <= '9':
            binary += changer[int(hexa[i])]
        else:
            if hexa[i] == "A":
                binary += (changer[10])
            if hexa[i] == "B":
                binary += (changer[11])
            if hexa[i] == "C":
                binary += (changer[12])
            if hexa[i] == "D":
                binary += (changer[13])
            if hexa[i] == "E":
                binary += (changer[14])
            if hexa[i] == "F":
                binary += (changer[15])
    print('#{} {}'.format(tc+1,binary))

