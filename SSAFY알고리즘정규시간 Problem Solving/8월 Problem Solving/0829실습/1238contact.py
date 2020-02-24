import sys
sys.stdin = open("1238_input.txt", "r")

# 처음에 한번 해줘야한다.
def BFS(S):
    global cnt
    # if queue == [] and queue2 == [] and cnt != 0:
    #     if TF == True:
    #         TF = False
    #     else:
    #         return
    if cnt == 0:
        cnt += 1
    for i in range(101):
        if call_array[S][i] == 1 and visited[i] == 0:
            visited[i] = cnt
            queue.append(i)
            # TF = True

    if queue2 == []:
        if queue == [] and cnt != 1:
            return
        cnt += 1
        while queue:
            a = queue.pop(0)
            queue2.append(a)
        d = queue2.pop(0)
        BFS(d)
    else:
        c = queue2.pop(0)
        BFS(c)

T = 10
for tc in range(1, T+1):
    L, S = map(int, input().split())
    data = list(map(int, input().split()))
    call_array = [[0]*101 for _ in range(101)]
    visited = [0]*101
    queue = []
    queue2 = []
    # TF = False
    cnt = 0
    result = 0

    for i in range(L):
        if i % 2 == 0:
            call_array[data[i]][data[i+1]] = 1

    BFS(S)
    mm = max(visited)
    for j in range(101):
        if visited[j] == mm:
            result = j

    print("#%d %d" %(tc, result))