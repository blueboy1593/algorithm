from pprint import pprint

N, M, y, x, K = map(int, input().split())
jido = []
for _ in range(N):
    jido.append(list(map(int, input().split())))
command_list = list(map(int, input().split()))

# 문제에서 그려준대로 주사위 구현 해보기.
dice = [ [0] * 3 for _ in range(4) ]
# 굴리기 방법에 따른 리스트 변경
def roll(num):
    if num == 1:
        temp = dice[1].pop()
        dice[1] = [dice[3][1]] + dice[1]
        dice[3][1] = temp
    elif num == 2:
        temp = dice[1].pop(0)
        dice[1] = dice[1] + [dice[3][1]]
        dice[3][1] = temp
    elif num == 3:
        arr = []
        for i in range(4):
            arr.append(dice[i][1])
        arr = arr + [arr.pop(0)]
        for i in range(4):
            dice[i][1] = arr[i]
    else:
        arr = []
        for i in range(4):
            arr.append(dice[i][1])
        arr = [arr.pop()] + arr
        for i in range(4):
            dice[i][1] = arr[i]
    # 이런 비효율적인 방법밖에 할 수가 없나...?
    # 나의 한계인가 파이썬의 한계인가
# print(command_list)
D = [0, (0,1), (0, -1), (-1,0), (1 , 0)]
for command in command_list:
    idy = y + D[command][0]
    jdx = x + D[command][1]
    if not (0 <= idy < N and 0 <= jdx < M):
        continue
    roll(command)
    print(dice[1][1])
    if jido[idy][jdx] == 0:
        jido[idy][jdx] = dice[3][1]
        # 이거는 제거되는 조건이 없네
        # 지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
        # dice[3][1] = 0
    else:
        dice[3][1] = jido[idy][jdx]
        jido[idy][jdx] = 0
    # pprint(dice)
    # pprint(jido)
    y = idy
    x = jdx