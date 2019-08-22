s=[]

def push(item):
    s.append(item)

def pop():
    if s:
        s.pop()
    else:
        return

def isEmpty():
    return True if len(s)==0 else False

def check_matching(data):
    for i in data:
        if i=='(':
            push(i)
        elif i==')':
            if isEmpty(): return False
            pop()
    if not isEmpty():return False
    else: return True
print(check_matching('()()((()))'))
print(check_matching('()()((())))'))