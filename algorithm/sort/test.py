ary=[5,2,7,1,3,8,9,3,5,2]

def selectionSort(ary):
    for i in range(len(ary)):
        mini=i;
        for j in range(i+1,len(ary),1):
            if ary[j]<ary[mini]:
                mini=j
        ary[i], ary[mini]=ary[mini],ary[i]

selectionSort(ary)
print(ary)


def recselectionSort(ary,s,e):
    if s==e:
        return
    else:
        mini=s
        for j in range(s+1,e,1):
            if ary[j]<ary[mini]:
                mini=j
        ary[s],ary[mini]=ary[mini],ary[s]
        recselectionSort(ary,s+1,e)