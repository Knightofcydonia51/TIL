RSP=["가위","바위","보"]
Man1=input()
Man2=input()
if Man1==Man2:
    print('Result : Draw')
elif RSP[RSP.index(Man1)-1]==RSP[RSP.index(Man2)]:
    print('Result : Man1 Win!')
else:
    print('Result : Man2 Win!')
print(RSP.index(Man1))
