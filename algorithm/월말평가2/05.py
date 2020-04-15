import sys
sys.stdin=open("05.txt")

def fix(num,weight,step):
    global max
    if step==len(road):
        if max<weight:
            max=weight
        return
    else:
        for i in range(step,len(road)):
            if road[i]=="0":
                if num==n:
                    if max < weight:
                        max = weight
                    return
                else:
                    fix(num+1,weight+1,i+1)
                    fix(num,0,i+1)
                    return
            else:
                weight+=1

max=0
road=input()
n=int(input())
fix(0,0,0)
print(max)