N = int(input())
dragon_curves = []
for _ in range(N):
    dragon_curves.append(tuple(map(int, input().split())))

# 101짜리 맵 만들기
dragon_map = [ [0] * 101 for _ in range(101) ]

D = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for curve in dragon_curves:
    x, y, d, g = curve
    yy = y + D[d][0]
    xx = x + D[d][1]
    dragon_map[y][x] = 1
    dragon_map[yy][xx] = 1
    # 시작점
    dotS = (y, x)
    # 축
    dotT = (yy, xx)
    # print(dotS, dotT)
    if g == 0:
        continue
    else:
        # s = (a, b)
        # t = (c, d)
        # new dot = (c + d - b, c + d + a) 엄청 헷갈리는데 좌표계가 y랑 x는 플마가 반대라서 등호는 다른게 맞아.
        dot_list = [dotT]
        for _ in range(g):
            c, d = dotT
            new_dot_list = []
            for dot in dot_list:
                a, b = dot
                # new_dot = (c + d - b, d + a - c) y, x를 헷갈렸네
                new_dot = (c + b - d, d + c - a) # 시간 꽤 많이 썼는데 그래도 얻은거 많다고 생각.
                if new_dot not in dot_list:
                    new_dot_list.append(new_dot) # 여기 조심해야될 수도...?
            a, b = dotS
            dotT = (c + b - d, d + c - a)
            new_dot_list.append(dotT)
            dot_list = dot_list + new_dot_list
        for dragon_dot in dot_list:
            dy, dx = dragon_dot
            dragon_map[dy][dx] = 1
        # print(dot_list)
# 여기까지가 드래곤맵에 dot 그리기
# print(*dragon_map, sep='\n')

result = 0
# 사각형 세기
for i in range(100):
    for j in range(100):
        if dragon_map[i][j] == 1 and dragon_map[i][j + 1] == 1 and dragon_map[i + 1][j] == 1 and dragon_map[i + 1][j + 1] == 1:
            result += 1

print(result)