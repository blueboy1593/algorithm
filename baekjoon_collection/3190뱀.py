from pprint import pprint

N = int(input())
K = int(input())
snake_map = [ [0] * (N + 2) for _ in range(N + 2) ]
for _ in range(K):
    y, x = map(int, input().split())
    snake_map[y][x] = 2
L = int(input())
change_direction = [0] * 10002
for _ in range(L):
    X, C = input().split()
    X = int(X)
    change_direction[X + 1] = C
D = [(0,1),(1,0),(0,-1),(-1, 0)]
time = 0
direction = 0
snake_tail = [[1, 1]]

while True:
    time += 1
    if change_direction[time] != 0:
        if change_direction[time] == 'L':
            direction -= 1
        if change_direction[time] == 'D':
            direction += 1
        if direction == -1:
            direction = 3
        if direction == 4:
            direction = 0
    go = snake_tail[-1]
    go_y = go[0] + D[direction][0]
    go_x = go[1] + D[direction][1]
    
    if go_y == 0 or go_y == N + 1 or go_x == 0 or go_x == N + 1:
        break
    if snake_map[go_y][go_x] == 1:
        break
    if snake_map[go_y][go_x] == 2:
        snake_tail.append([go_y, go_x])
        snake_map[go_y][go_x] = 1
    else:
        snake_tail.append([go_y, go_x])
        snake_map[go_y][go_x] = 1
        tail = snake_tail.pop(0)
        tail_y = tail[0]
        tail_x = tail[1]
        snake_map[tail_y][tail_x] = 0
    
print(time)