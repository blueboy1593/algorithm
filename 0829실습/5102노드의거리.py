import sys
sys.stdin = open("5102_input.txt", "r")

def nodego():
    global cnt
    while queue:
        for j in range(len(queue)):
            a = queue.pop(0)
            # print(visited)
            # print("a는", a)
            # print(queue)
            for i in range(len(line)):
                if a == line[i]:
                    if i % 2 == 0:
                        if visited[line[i+1]] == False:
                            visited[line[i + 1]] = True
                            queue.append(line[i + 1])
                    elif i % 2 == 1:
                        if visited[line[i - 1]] == False:
                            visited[line[i - 1]] = True
                            queue.append(line[i - 1])
        cnt += 1
        if visited[G] == True:
            return
    cnt = 0
    # 길이 없는 경우도 있네 그지같게 ㅡㅡ

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    line = []
    for _ in range(E):
        a, b = map(int, input().split())
        line.append(a)
        line.append(b)
    S, G = map(int, input().split())
    queue = [S]
    visited = [False] * (V+1)
    visited[S] = True
    cnt = 0

    nodego()
    result = cnt
    if S == G:
        result = 0
    print('#' + str(tc) + ' ', end = '')
    print(result)