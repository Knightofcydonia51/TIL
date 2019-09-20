import sys
sys.stdin=open("07.electric_bus_input.txt")
T=int(input())
def electric_bus():
    for i in range(T):
        charge = 0
        num=list(map(int,input().strip().split(' ')))
        K=num[0];N=num[1];M=num[2]
        station=list(map(int,input().strip().split(' ')))
        pointer=0
        fuel=K
        charge_point=(-1)
        while pointer<N:
            charge_point += 1
            last_point=station[charge_point]
            if last_point==station[-1]:
                last_point=N
            if fuel<0:
                break
            while pointer<last_point:
                fuel-=1
                pointer+=1
                if fuel<0:
                    charge=0
                    break
                if pointer==station[charge_point]:
                    if pointer==station[-1]:
                        if fuel>=N-station[-1]:
                            pass
                        else:
                            charge+=1
                            fuel=K
                    elif fuel>=station[charge_point+1]-station[charge_point]:
                        pass
                    else:
                        charge+=1
                        fuel=K
        print('#{} {}'.format(i+1, charge))
electric_bus()