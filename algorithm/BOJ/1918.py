N = 4
cnt = 0
def dfs():
    global cnt
    print(1)
    cnt += 1
    if cnt < N:
        dfs()
dfs()

