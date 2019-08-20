# def my_strrev(ary):
#     str=list(ary)
#     for i in range(len(str)//2):
#         str[i], str[len(str)-1-i]= str[len(ary)-1-i], str[i]
#     ary="".join(str)
#     return ary
#
#
# ary='abcde'
# ary=my_strrev(ary)
# print(ary)
#
# s='Reverse this strings'
# s=s[-1:0:-1]
# print(s)

def itoa(x):
    str=list()
    count=0
    i,y=0,0
    while 1:
        y=x%10
        str.append(chr(y+ord('0')))
        x //=10
        if x==0 : break
        i+=1
    str.reverse()
    str="".join(str)
    return str

