import sys
sys.stdin=open("04.txt")

answer_sheet=input()
sheets=[x for x in input().split()]

print(answer_sheet)
print(sheets)

answer=0

for i in range(len(sheets)-1): #0123
    for k in range(i+1,len(sheets)): #1234
        sus= 0
        weight=0
        weight_max=0
        for j in range(len(sheets[i])):
            if sheets[k][j]==sheets[i][j]:
                if answer_sheet[j]!=sheets[i][j]:
                    weight+=1
                    sus+=1
                else:
                    weight_max = weight
                    weight = 0
                    continue
            else:
                weight_max=weight
                weight=0
                continue
        if weight_max < weight:
            weight_max = weight
        if answer<sus+(weight_max**2):
            answer=sus + (weight_max ** 2)

print(answer)

# if weight_max < weight:
#     weight_max = weight