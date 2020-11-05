N, S = map(int, input().split())
suyeol = list(map(int, input().split()))

visited = [False] * N
answer = 0

def backtracking(index, cnt):
    global answer
    print(visited)
    if cnt == S:
        if index != 0:
            answer += 1
        # return
    for i in range(index, N):
    # for i in range(N):
        if visited[i] == False:
            visited[i] = True
            backtracking(i + 1, cnt + suyeol[i])
            visited[i] = False

backtracking(0, 0)
print(answer)