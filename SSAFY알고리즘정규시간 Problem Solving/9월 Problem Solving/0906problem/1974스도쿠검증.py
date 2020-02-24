import sys
sys.stdin = open("1974_input.txt")

def find_sero():
    global result
    for j in range(9):
        bin = set()
        for i in range(9):
            bin.add(sudoku[i][j])
        if len(bin) != 9:
            result = 0
            return

def find_3x3():
    global result
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            bin = set()
            for k in range(3):
                for l in range(3):
                    bin.add(sudoku[i + k][j + l])
            if len(bin) != 9:
                result = 0
                return

T = int(input())
for tc in range(1, T + 1):
    N = 9
    result = 1
    sudoku = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        sudoku.append(temp)
        check = set(temp)
        if len(check) != 9:
            result = 0
    if result == 1:
        find_sero()
    if result == 1:
        find_3x3()
    print("#%d %d" %(tc,result))
