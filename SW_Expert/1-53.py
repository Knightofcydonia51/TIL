alpha={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
def aaa():
    for i in alpha.keys():
        print('{}: {}'.format(i, alpha.get(i)))
aaa()