import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint

sero, garo = map(int, input().split())
cheeze_map = [list(map(int, input().split())) for _ in range(sero)]
check_map = [ [0] * garo for _ in range(sero) ]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cheeze_num = 0
cnt = 0

def cheeze_delete():
    global cheeze_num
    cheeze_num = 0
    queue = [[0, 0]]
    visited = [[False] * garo for _ in range(sero)]
    visited[0][0] = True
    while queue:
        for _ in range(len(queue)):
            a = queue.pop(0)
            for i in range(4):
                y = a[0]
                x = a[1]
                idy = y + dy[i]
                idx = x + dx[i]
                if 0 <= idy < sero and 0 <= idx < garo:
                    if visited[idy][idx] == False:
                        if cheeze_map[idy][idx] == 0:
                            visited[idy][idx] = True
                            queue.append([idy, idx])
                        if cheeze_map[idy][idx] == 1:
                            visited[idy][idx] = True
                            cheeze_map[idy][idx] = 2
    for i in range(sero):
        for j in range(garo):
            if cheeze_map[i][j] == 2:
                cheeze_map[i][j] = 0
                cheeze_num += 1

while cheeze_map != check_map:
    cnt += 1
    cheeze_delete()

print(cnt)
print(cheeze_num)