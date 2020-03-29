a=input().split(',')
def longer(a):
    if  len(a[0])>len(a[1]):
    	return a[0]
    else:
        return a[1].strip()
print(longer(a))