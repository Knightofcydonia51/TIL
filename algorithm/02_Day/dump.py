import sys
sys.stdin=open("dump.txt")

# for i in range(10):
#     dump=int(input())
#     terrain=[int(x) for x in input().split()]
#     for k in range(dump):
#         terrain[terrain.index(max(terrain))]=max(terrain)-1
#         terrain[terrain.index(min(terrain))]=min(terrain)+1
#     print("#{} {}".format(i+1,max(terrain)-min(terrain)))

for i in range(10):
    dump=int(input())
    terrain=[int(x) for x in input().split()]
    for k in range(dump):
        maxi = 0
        mini = sys.maxsize
        maxidx = 0
        minidx = 0

        for idx, j in enumerate(terrain):
            if j>maxi:
                maxi=j
                maxidx=idx
            if j<mini:
                mini=j
                minidx=idx
        terrain[maxidx] -= 1
        terrain[minidx] += 1
        maxi = 0
        mini = sys.maxsize
        maxidx = 0
        minidx = 0

        for idx, j in enumerate(terrain):
            if j > maxi:
                maxi = j
                maxidx = idx
            if j < mini:
                mini = j
                minidx = idx

        if terrain[maxidx]-terrain[minidx]<=1:
            break
    print('#{} {}'.format(i+1,terrain[maxidx]-terrain[minidx]))





