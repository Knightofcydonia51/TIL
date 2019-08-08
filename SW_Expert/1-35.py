man1=input()
man2=input()
ones=input()
seconds=input()

def RSP(*args):
    weapons=["가위","바위","보"]
    if args[2]==args[3]:
        print('비겼습니다!')
    elif weapons[weapons.index(ones)-1]==weapons[weapons.index(seconds)]:
        print('{}가 이겼습니다!'.format(args[2]))
    else:
        print('{}가 이겼습니다!'.format(args[3]))

RSP(man1,man2,ones,seconds)