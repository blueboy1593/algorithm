N = int(input())
dragon_curve = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve.append([y, x, d, g])
print(dragon_curve)

dragon_map = [ [0] * 100 for _ in range(100) ]
# print(dragon_map)

def curve_record(i, j, k, n):
    if k == n:
        return
    y = dragon_list[0][0]
    x = dragon_list[0][1]
    new_ymid = i + x - j
    new_xmid = j + i - y
    if [new_ymid, new_xmid] not in dragon_list:
        dragon_list.append([new_ymid, new_xmid])
    for m in range(1, len(dragon_list)):
        y = dragon_list[m][0]
        x = dragon_list[m][1]
        new_y = i + x - j
        new_x = j + i - y
        if [new_y, new_x] not in dragon_list:
            dragon_list.append([new_y, new_x])
    k += 1
    curve_record(new_ymid, new_xmid, k, n)

for dragon in dragon_curve:
    dragon_list = []
    if dragon[3] == 0:
        dragon_map[dragon[0]][dragon[1]] = 1
    elif dragon[3] == 1:
        dragon_map[dragon[0]][dragon[1]] = 1
        if dragon[2] == 0:
            dragon_map[dragon[0]][dragon[1] + 1] = 1
        if dragon[2] == 1:
            dragon_map[dragon[0] - 1][dragon[1]] = 1
        if dragon[2] == 2:
            dragon_map[dragon[0]][dragon[1] - 1] = 1
        if dragon[2] == 3:
            dragon_map[dragon[0] + 1][dragon[1]] = 1
    else:
        n = dragon[3]
        dragon_map[dragon[0]][dragon[1]] = 1
        dragon_list.append([dragon[0], dragon[1]])
        if dragon[2] == 0:
            dragon_map[dragon[0]][dragon[1] + 1] = 1
            dragon_list.append([dragon[0], dragon[1] + 1])
            curve_record(dragon[0], dragon[1] + 1, 1, n)
        if dragon[2] == 1:
            dragon_map[dragon[0] - 1][dragon[1]] = 1
            dragon_list.append([dragon[0] - 1, dragon[1]])
            curve_record(dragon[0] - 1, dragon[1], 1, n)
        if dragon[2] == 2:
            dragon_map[dragon[0]][dragon[1] - 1] = 1
            dragon_list.append([dragon[0], dragon[1] - 1])
            curve_record(dragon[0], dragon[1] - 1, 1, n)
        if dragon[2] == 3:
            dragon_map[dragon[0] + 1][dragon[1]] = 1
            dragon_list.append([dragon[0] + 1, dragon[1]])
            curve_record(dragon[0] + 1, dragon[1], 1, n)
    if dragon_list:
        for yong in dragon_list:
            yy = yong[0]
            xx = yong[1]
            dragon_map[yy][xx] = 1

for i in range(100):
    for j in range(100):
        if dragon_map[i][j] == 1:
            print(i, j)