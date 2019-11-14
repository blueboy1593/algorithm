import sys
sys.stdin = open("1979_input.txt", "r")

def width_go(y, x):
    global cnt, word, K
    cnt += 1
    width_visited[y][x] = True
    try:
        if puzzle[y][x+1] == 1:
            width_go(y, x + 1)
        elif puzzle[y][x + 1] == 0:
            if cnt == K:
                word += 1
            return
    except IndexError:
        if cnt == K:
            word += 1
        pass

def height_go(y, x):
    global cnt, word, K
    cnt += 1
    height_visited[y][x] = True
    try:
        if puzzle[y + 1][x] == 1:
            height_go(y + 1, x)
        elif puzzle[y + 1][x] == 0:
            if cnt == K:
             
                word += 1
            return
    except IndexError:
        if cnt == K:
            
            word += 1
        pass

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [0] * N
    for i in range(N):
        puzzle[i] = list(map(int, input().split()))
    width_visited = [ [False]* N for _ in range(N)]
    height_visited = [ [False]* N for _ in range(N)]
    word = 0

    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                if width_visited[i][j] == False:
                    cnt = 0
                    width_go(i, j)
                if height_visited[i][j] == False:
                    cnt = 0
                    height_go(i, j)
    
    print("#%d %d" %(tc, word))