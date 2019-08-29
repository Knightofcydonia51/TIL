import sys
sys.stdin=open("1974.sudoku.txt")


T=int(input())
validate=[1,2,3,4,5,6,7,8,9]


def validater(sudo):
    global ans
    for y in range(9):
        line = []
        line2=[]
        for x in range(9):
            line.append(sudo[y][x])
            line2.append(sudo[x][y])
        if sorted(line)!=validate or sorted(line2)!=validate:
            ans = 0
            return ans

    for y in range(3):
        for x in range(3):
            line3 = []
            for z in range(3):
                for m in range(3):
                    line3.append(sudo[z+3*y][m+3*x])
            if sorted(line3)!=validate:
                ans=0
                return ans

for i in range(T):
    ans=1
    sudoku=[[int(x) for x in input().split()]for y in range(9)]
    validater(sudoku)
    print('#{} {}'.format(i+1,ans))



