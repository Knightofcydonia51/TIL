a=input()
if a.isalpha():
    b = a.islower()
    if b:
        print("{}(ASCII: {}) => {}(ASCII: {})".format(a, ord(a), a.upper(), ord(a.upper())))
    elif b==False:
        print("{}(ASCII: {}) => {}(ASCII: {})".format(a, ord(a), a.lower(), ord(a.lower())))
else:
    print(a)