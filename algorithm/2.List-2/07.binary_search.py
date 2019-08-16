import sys
sys.stdin=open("07.binary_search.txt")

T=int(input())
for i in range(T):
    PAB=[int(x) for x in input().split()]
    P=PAB[0]; Pa=PAB[1]; Pb=PAB[2];
    A_right=P; B_right=P
    A_left=1
    B_left=1
    A=0
    B=0
    win=''
    while True:
        if A==1 and B==1:
            win='0'
            break
        elif A==1:
            win='A'
            break
        elif B==1:
            win='B'
            break
        wallA=(A_left+A_right)//2
        if wallA>Pa:
            A_right=wallA
        elif wallA<Pa:
            A_left=wallA
        if wallA==Pa:
            A+=1
        wallB=(B_left+B_right)//2
        if wallB > Pb:
            B_right=wallB
        elif wallB<Pb:
            B_left=wallB
        if wallB==Pb:
            B+=1

    print('#{} {}'.format(i+1, win))