topni = [0]
for _ in range(4):
    topni.append(list(map(int, input())))
# print(*topni, sep='\n')
K = int(input())
touringways = []
for _ in range(K):
    a, b = map(int, input().split())
    touringways.append((a, b))

for touring in touringways:
    visited = [True] + [False] * 4
    top, way = touring
    visited[top] = True
    stack = [(top, way)]
    while stack:
        a, b = stack.pop()
        if a + 1 <= 4:
            if visited[a + 1] == False:
                if topni[a][2] != topni[a + 1][6]:
                    stack.append((a + 1, -b))
                    visited[a + 1] = True
        if a - 1 >= 1:
            if visited[a - 1] == False:
                if topni[a][6] != topni[a - 1][2]:
                    stack.append((a - 1, -b))
                    visited[a - 1] = True
        if b == 1:
            temp = topni[a]
            topni[a] = [temp.pop()] + temp
        if b == -1:
            temp = topni[a]
            topni[a] = temp + [temp.pop(0)]

result = 0
for i in range(1, 5):
    if topni[i][0] == 1:
        result += 2 ** (i - 1)
print(result)