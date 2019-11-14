import sys
sys.stdin = open("17779_input.txt", "r")
from pprint import pprint

N = int(input())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

for x in range(N - 2):
    for y in range(1, N - 1):
        # 비효율적일 수 있지만 for문으로 그냥 다 검출해보자.
        for d1 in range(1, N - 2):
            for d2 in range(1, N - 2):
                new_city = [ [0] * N for _ in range(N) ]
                if x+d1+d2 < N and 0 <= y-d1 < y < y+d2 < N:
                    # 일단 정했지만 얼마든지 실수가 나올 수 있음.
                    # new_city[x][y] = 5

                    peak_N = (x, y)
                    for i in range(x):
                        for j in range(y):
                            new_city[i][j] = 1
                    for i in range(x):
                        if new_city[i][y] == 5:
                            break
                        else:
                            new_city[i][y] = 1
                    for d in range(d1):
                        new_city[x + d][y - d] = 5
                        for j in range(y - d):
                            new_city[x + d][j] = 1

                    peak_W = (x + d1, y - d1)
                    for d in range(d2):
                        new_city[x + d][y + d] = 5 

                    peak_E = (x + d2, y + d2)
                    for d in range(d2):
                        new_city[x + d1 + d][y - d1 + d] = 5
                    for d in range(d1):
                        new_city[x + d2 + d][y + d2 - d] = 5
                    peak_S = (x + d1 + d2, y - d1 + d2)
                    new_city[peak_S[0]][peak_S[1]] = 5

                    # 3번 지역 채우기
                    for i in range(x + d1, N):
                        for j in range(y - d1 + d2):
                            if new_city[i][j] == 5:
                                continue
                            else:
                                new_city[i][j] = 3

                    
                    pprint(new_city)
