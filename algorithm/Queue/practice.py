def enQueue():
    a=[]
    return a

def isFull(item):
    global front,rear
    return (rear+1)

def isEmpty(item):
    return True if len(item)==0 else False

def enQueue(a,item):
    a.append(item)

def deQueue(a):
    return a.pop(a[0])

def Qpeek(a):
    return a[0]


size=100
Q=[0]*size
front, rear= -1, -1

