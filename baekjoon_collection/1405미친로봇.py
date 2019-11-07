N, e, w, s, n = map(int, input().split())
robot_map = [ [0] * 31 for _ in range(31) ]
e_chance = e / 100
w_chance = w / 100
s_chance = s / 100
n_chance = n / 100
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
total_chance = 0
probability = [s_chance, n_chance, e_chance, w_chance]

def backtracking(i, j, chance, cnt):
    global total_chance
    if cnt == N:
        total_chance += chance
        # print(chance)
        return
    else:
        for k in range(4):
            idy = i + dy[k]
            jdx = j + dx[k]
            if robot_map[idy][jdx] == 0:
                robot_map[idy][jdx] = 1
                backtracking(idy, jdx, chance*probability[k], cnt + 1)
                robot_map[idy][jdx] = 0

robot_map[15][15] = 1
backtracking(15, 15, 1, 0)
print(total_chance)