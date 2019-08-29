import sys
sys.stdin = open("07.minimum.txt")


# count = 0
# total = 0
# N = 10
# # 원소의 포함여부 저장 (0, 1)

def powerset(n, y, sol):      # n: 원소의 갯수, k: 현재depth

    global tc

    if n == y:          # Basis Part
        print(tc, sol)
    else:               # Inductive Part
        for k in range(N):
            if A[k] == 1:
                continue
            A[k] = 1        # k번 요소 O
            powerset(n, y + 1, sol+data[y][k])  # 다음 요소 포함 여부 결정
            A[k] = 0       # k번 요소 X

# print("호출회수 : {}".format(total) )

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = [0 for _ in range(N)]
    data = [list(map(int, input().split())) for _ in range(N)]
    powerset(N, 0, 0)