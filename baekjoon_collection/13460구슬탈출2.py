from pprint import pprint

N, M = map(int, input().split())

marble_board = []
for _ in range(N):
    marble_board.append(list(input()))

D = [(1, 0),(-1,0),(0,1),(0,-1)]
overlap_list = []
pprint(marble_board)

def gogo1(i, j, k):
    global flag, hallin
    while True:
        i = i + 1
        j = j
        if marble_board[i][j] == '#':
            return (i - 1, j)
        elif marble_board[i][j] == 'O':
            hallin = True
            return (i, j)
        else:
            flag = True

RB = [0, 0, 0, 0]
for i in range(N):
    for j in range(M):
        if marble_board[i][j] == 'R':
            RB[0] = i
            RB[1] = j
        if marble_board[i][j] == 'B':
            RB[2] = i
            RB[3] = j
overlap_list.append(RB)
print(overlap_list)

temp = [0, 0, 0, 0]
def backtracking(arr, cnt):
    cnt += 1
    R_i = arr[0]
    R_j = arr[1]
    B_i = arr[2]
    B_j = arr[3]
    for k in range(4):
        if k == 1:
            if R_i >= B_i:
                temp[0], temp[1] = gogo1(R_i, R_j)
                marble_board[R_i][R_j] = '.'
                marble_board[temp[0]][temp[1]] = 'R'
                temp[2], temp[3] = gogo1(B_i, B_j)
                marble_board[R_i][R_j] = '.'
                marble_board[temp[0]][temp[1]] = 'B'
                if :
                    continue
                else:


flag = False
hallin = False
cnt = 0
backtracking(RB, cnt)