number=input()
a=""
for i in range(0,10):
    a+=str(number.count("{}".format(i)))+" "
print("0 1 2 3 4 5 6 7 8 9")
print(a)