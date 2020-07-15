import sys
sys.stdin=open("testA.txt")

T=int(input())
dx=[0,0,-1,1]
dy=[1,-1,0,0]

for i in range(T):
    N=int(input())
    energy=0
    atoms=[[int(x) for x in input().split()]for y in range(N)]
    sheet=[[0 for x in range(6000)]for y in range(6000)]

    for k in range(2000):
        length=len(atoms)
        j = 0
        while j<length:
            # print(len(atoms))
            sheet[atoms[j][1]][atoms[j][0]]=0 #atoms[j]의 위치값 초기화
            print(atoms[j])
            if sheet[atoms[j][1]+dy[atoms[j][2]]][atoms[j][0]+dx[atoms[j][2]]]!=0:
                print("----------------boom------------",length,sheet[5][5])
                # print("boom",sheet[atoms[j][1]+dy[atoms[j][2]]][atoms[j][0]+dx[atoms[j][2]]])
                # print(j, atoms[j])
                # print(1, atoms[1])
                bye=sheet[atoms[j][1] + dy[atoms[j][2]]][atoms[j][0] + dx[atoms[j][2]]][1]
                energy+=atoms[j][3]+sheet[atoms[j][1]+dy[atoms[j][2]]][atoms[j][0]+dx[atoms[j][2]]][0]
                print(atoms[bye],atoms[j],bye,j)
                sheet[atoms[j][1] + dy[atoms[j][2]]][atoms[j][0] + dx[atoms[j][2]]]=0
                atoms.pop(bye)
                atoms.pop(j)
                length=len(atoms)
                continue
            atoms[j][0],atoms[j][1]=atoms[j][0]+dx[atoms[j][2]],atoms[j][1]+dy[atoms[j][2]]
            sheet[atoms[j][1]][atoms[j][0]] = [atoms[j][3],j]
            j+=1
    print(energy)



# list=[[0 for x in range(3)]for y in range(3)]
# hi=[[3 for x in range(3)]for y in range(3)]
# list[0][0]=[hi[0][0],1]
# print(list)