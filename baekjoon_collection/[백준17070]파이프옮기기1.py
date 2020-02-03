N = int(input())
home = []
for _ in range(N):
    home.append(list(map(int, input().split())))

# 생각해보니 visited가 필요가 없는 문제인거같은데...?
# visited = [ [ False ] * N for _ in range(N) ]
# visited[0][0] = True
# visited[0][1] = True
type = 0
result = 0

# 단순히 방향 처리를 바꾸는 것만으로... 시간 안에 풀 수 있다고..?
# 이 문제는 review하기 좋은듯. 신기한 문제라고 생각..

# def gogopipe(i, j, type):
#     global result
#     if i == N - 1 and j == N - 1:
#         result += 1
#         return
#     if type == 0 or type == 1:
#         if j + 1 < N:
#             if home[i][j + 1] == 0:
#                 gogopipe(i, j + 1, 0)
#     if i + 1 < N and j + 1 < N:
#         # 이게 없으면 시간초과가 나네.
#         if home[i + 1][j] == home[i][j + 1] == home[i + 1][j + 1] == 0:
#             gogopipe(i + 1, j + 1, 1)
#     if type == 1 or type == 2:
#         if i + 1 < N:
#             if home[i + 1][j] == 0:
#                 gogopipe(i + 1, j, 2)
#
# gogopipe(0, 1, 0)
# print(result)

def gopipepipe(i, j, type):
    global result
    if i == N - 1 and j == N - 1:
        result += 1
        return
    # 아래는 가로 1자 처리 방법.
    if type == 0:
        if j + 1 < N:
            if home[i][j + 1] == 0:
                gopipepipe(i, j + 1, 0)
        if i + 1 < N and j + 1 < N:
            if home[i + 1][j] == home[i][j + 1] == home[i + 1][j + 1] == 0:
                gopipepipe(i + 1, j + 1, 1)
    # 대각선으로 온 상황에서 처리 방법.
    if type == 1:
        if j + 1 < N:
            if home[i][j + 1] == 0:
                gopipepipe(i, j + 1, 0)
        if i + 1 < N and j + 1 < N:
            if home[i + 1][j] == home[i][j + 1] == home[i + 1][j + 1] == 0:
                gopipepipe(i + 1, j + 1, 1)
        if i + 1 < N:
            if home[i + 1][j] == 0:
                gopipepipe(i + 1, j, 2)
    # 세로로 내려간 상황에서 처리 방법.
    if type == 2:
        if i + 1 < N and j + 1 < N:
            if home[i + 1][j] == home[i][j + 1] == home[i + 1][j + 1] == 0:
                gopipepipe(i + 1, j + 1, 1)
        if i + 1 < N:
            if home[i + 1][j] == 0:
                gopipepipe(i + 1, j, 2)


gopipepipe(0, 1, 0)
print(result)

# https://home-body.tistory.com/475
# 여기 사이트에 있는 DP 방법대로 하면 좋음.