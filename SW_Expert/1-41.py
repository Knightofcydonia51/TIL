a=input().split(',')
i=0
while i<len(a):
    a[i]=int(a[i].strip())
    i+=1

def square(n):
    return n**2

print('square({}) => {}'.format(a[0],square(a[0])))
print('square({}) => {}'.format(a[1],square(a[1])))