l=[1,2,3,4,3,2,1]
def deleter(list2):
    list2=list(set(list2))
    return list2

print(l)
print(deleter(l))