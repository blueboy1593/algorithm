N, M, D = map(int, input().split())
castle = [0] * N
for i in range(N):
    castle[i] = list(map(int, input().split()))
maxmax = 0

# def hwalssogi(x, list, m):
#     if 0 <= x - m < M:
#         if list[x - m] == 1:
#             return x - m
#     elif 0 <= x + m < M:
#         if list[x + m] == 1:
#             return x + m
#     else:
#         hwalssogi(x, list, m + 1)

comb_list = []
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            comb_list.append([i, j, k])

for comb in comb_list:
    cnt = 0
    a = comb[0]
    b = comb[1]
    c = comb[2]
    print(a, b, c)
    for i in range(N):
        temp = castle[i]
        enemy_dict = {a: 16, b: 16, c: 16}
        for j in range(M):
            if temp[j] == 1:
                if abs(j - a) < abs(enemy_dict[a] - a):
                    enemy_dict[a] = j
                if abs(j - b) < abs(enemy_dict[b] - b):
                    enemy_dict[b] = j
                if abs(j - c) < abs(enemy_dict[c] - c):
                    enemy_dict[c] = j
        archer_set = set()
        print(enemy_dict)
        for value in enemy_dict.values():
            if 0 <= value < 16:
                archer_set.add(value)
        print(archer_set)
        temp_cnt = len(archer_set)
        cnt += temp_cnt
    if cnt > maxmax:
        maxmax = cnt


# print(castle)
print(comb_list)
print(maxmax)