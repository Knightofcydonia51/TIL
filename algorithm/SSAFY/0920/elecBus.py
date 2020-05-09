import sys
sys.stdin=open('elecBus.txt')

T=int(input())

def bus(station, pointer, fuel, charge, next):
    while 1:
        for k in range(1, fuel + 1):
            if pointer+k==len(station)-1:
                return charge
            elif station[pointer + k] + k > station[next+pointer]+next:
                next = k
        fuel = station[pointer + next]
        charge += 1
        pointer += next
        next=0

for i in range(T):
    station=[int(x) for x in input().split()]
    N=station.pop(0)
    station.append(0)
    fuel=station[0]
    pointer=0;charge=0;next=0
    print('#{} {}'.format(i+1,bus(station, pointer, fuel, charge, next)))




