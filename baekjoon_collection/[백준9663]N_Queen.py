N = int(input())

chess_map = [ [ 0 ] * N for _ in range(N) ]
visited = [ [False] * N for _ in range(N) ]
answer = 0

def backtracking(i, j, cnt):
    global answer
    # 퀸 배치 개수가 N개일 때 답 하나 추가해주기
    if cnt == N:
        answer += 1
        return

    # visited를 해줄 요소들 찾기
    stack = []
    for y in range(N):
        for x in range(N):
            # 상하좌우 같을시
            if y == i or x == j:
                if not visited[y][x]:
                    visited[y][x] = True
                    stack.append((y, x))
            elif abs(y - i) == abs(x - j):
                if not visited[y][x]:
                    visited[y][x] = True
                    stack.append((y, x))

    # 다음 퀸 배치와 함께 백트래킹 함수 들어가기.
    # 이구간 로직은 필요없음.
    # for xx in range(j + 1, N):
    #     if not visited[i][xx]:
    #         backtracking(i, xx, cnt + 1)
    for yy in range(i + 1, N):
        for xx in range(N):
            if not visited[yy][xx]:
                backtracking(yy, xx, cnt + 1)
    
    # visited 지워주기
    for ii, jj in stack:
        visited[ii][jj] = False

for j in range(N):
    backtracking(0, j, 1)

print(answer)